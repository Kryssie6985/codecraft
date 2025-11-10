"""
Lisp Generator for the Rosetta Stone Protocol
Emits a canonical S-expression representing the ritual AST and definition.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List
import hashlib
import json

from ..ast_builder import RitualAST, ASTNode


def _escape_string(s: str) -> str:
    return (
        '"'
        + s.replace('\\', '\\\\')
        .replace('"', '\\"')
        .replace('\n', '\\n')
        .replace('\r', '\\r')
        .replace('\t', '\\t')
        + '"'
    )


def _encode_atom(v: Any) -> str:
    if v is None:
        return 'nil'
    if isinstance(v, bool):
        return 't' if v else 'nil'
    if isinstance(v, (int, float)):
        return str(v)
    if isinstance(v, str):
        return _escape_string(v)
    # Fallback to string
    return _escape_string(str(v))


def _encode_list(items: List[str]) -> str:
    return f"({' '.join(items)})"


def _encode_plist(d: Dict[str, Any]) -> str:
    if not d:
        return 'nil'
    parts: List[str] = []
    for k in sorted(d.keys()):
        key = f":{k}"
        parts.append(key)
        parts.append(_encode_value(d[k]))
    return _encode_list(parts)


def _encode_value(v: Any) -> str:
    if isinstance(v, dict):
        return _encode_plist(v)
    if isinstance(v, (list, tuple)):
        return _encode_list([_encode_value(x) for x in v])
    return _encode_atom(v)


def _encode_ast_node(node: ASTNode) -> str:
    parts: List[str] = []
    # node signature: (node :type "TYPE" :value <v> :metadata <plist> :children (...))
    parts.append('node')
    parts.append(':type')
    parts.append(_encode_atom(node.type.value))
    parts.append(':value')
    parts.append(_encode_value(node.value))

    # metadata and children if present
    if node.metadata:
        parts.append(':metadata')
        parts.append(_encode_plist(node.metadata))
    if node.children:
        parts.append(':children')
        parts.append(_encode_list([_encode_ast_node(c) for c in node.children]))
    return _encode_list(parts)


class LispGenerator:
    """Generate a canonical S-expression for a ritual"""

    def generate(self, ritual_def, ast: RitualAST, output_dir: Path) -> Path:
        output_dir.mkdir(parents=True, exist_ok=True)

        # Build top-level form
        top_parts: List[str] = []
        top_parts.append('ritual')
        top_parts.append(':id')
        top_parts.append(_encode_atom(ritual_def.id))
        top_parts.append(':name')
        top_parts.append(_encode_atom(ritual_def.name))
        top_parts.append(':author')
        top_parts.append(_encode_atom(ritual_def.author))
        top_parts.append(':version')
        top_parts.append(_encode_atom(ritual_def.version))

        # tags list (deterministic)
        tags = getattr(ritual_def, 'tags', []) or []
        top_parts.append(':tags')
        top_parts.append(_encode_list([_encode_atom(t) for t in tags]))

        # payload / metadata
        top_parts.append(':payload')
        top_parts.append(_encode_plist(getattr(ritual_def, 'payload', {}) or {}))

        meta_block: Dict[str, Any] = getattr(ritual_def, 'metadata', {}) or {}
        top_parts.append(':metadata')
        top_parts.append(_encode_plist(meta_block))

        # AST root
        top_parts.append(':ast')
        top_parts.append(_encode_ast_node(ast.root))

        sexpr = _encode_list(top_parts) + "\n"

        # Context hash
        context_hash = hashlib.sha256(sexpr.encode('utf-8')).hexdigest()

        # Write outputs
        lisp_path = output_dir / f"{ritual_def.id}.lisp"
        with open(lisp_path, 'w', encoding='utf-8') as f:
            f.write(sexpr)

        # Sidecar manifest with hash for downstream stages
        manifest_path = output_dir / f"{ritual_def.id}.lisp.json"
        manifest = {
            'id': ritual_def.id,
            'name': ritual_def.name,
            'version': ritual_def.version,
            'context_hash': context_hash,
            'bytes': len(sexpr.encode('utf-8')),
            'format': 'lisp/canonical-sexpr@v1'
        }
        with open(manifest_path, 'w', encoding='utf-8') as mf:
            json.dump(manifest, mf, indent=2, sort_keys=True)

        return lisp_path
