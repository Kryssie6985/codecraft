/**
 * RitualParser - Parses CodeCraft ritual syntax
 * MEGA's vision: Transform sacred syntax into executable AST
 */

export interface RitualAST {
  type: string;
  command: string;
  target?: string;
  params?: any[];
  children?: RitualAST[];
}

export class RitualParser {
  private ritualPatterns = new Map<string, RegExp>([
    ['summon', /::summon\.(\w+)\((.*?)\)/],
    ['manifest', /::manifest\.(\w+)\((.*?)\)/],
    ['bind', /::bind\.(\w+)\((.*?)\)/],
    ['context', /::context\.(\w+)\((.*?)\)/],
    ['detect', /::detect\.(\w+)\((.*?)\)/],
    ['enforce', /::enforce\.(\w+)\((.*?)\)/],
    ['pause', /::pause_deliberation\(\)/],
    ['redirect', /::redirect_focus\((.*?)\)/],
    ['cmp', /::cmp\.(\w+)\((.*?)\)/],
  ]);

  /**
   * Parse CodeCraft ritual syntax into executable AST
   */
  parse(ritual: string): RitualAST[] {
    const lines = ritual.trim().split('\n').map(line => line.trim());
    const ast: RitualAST[] = [];

    for (const line of lines) {
      if (!line || line.startsWith('//')) continue;

      const node = this.parseLine(line);
      if (node) {
        ast.push(node);
      }
    }

    return ast;
  }

  private parseLine(line: string): RitualAST | null {
    for (const [type, pattern] of this.ritualPatterns) {
      const match = pattern.exec(line);
      if (match) {
        return {
          type,
          command: match[1] || type,
          params: match[2] ? this.parseParams(match[2]) : [],
          target: match[1]
        };
      }
    }

    // Handle generic ritual format
    const genericMatch = /::(\w+)\.(\w+)\((.*?)\)/.exec(line);
    if (genericMatch) {
      return {
        type: genericMatch[1],
        command: genericMatch[2],
        params: genericMatch[3] ? this.parseParams(genericMatch[3]) : []
      };
    }

    return null;
  }

  private parseParams(paramString: string): any[] {
    // Handle JSON objects
    if (paramString.trim().startsWith('{') || paramString.trim().startsWith('[')) {
      try {
        return [JSON.parse(paramString)];
      } catch {
        // Fall back to string parsing
      }
    }

    // Parse comma-separated values
    return paramString
      .split(',')
      .map(p => p.trim())
      .map(p => {
        // Remove quotes
        if ((p.startsWith("'") && p.endsWith("'")) || 
            (p.startsWith('"') && p.endsWith('"'))) {
          return p.slice(1, -1);
        }
        // Try to parse as JSON
        try {
          return JSON.parse(p);
        } catch {
          return p;
        }
      });
  }
}