"""
Setup script for the CodeCraft Library
SERAPHINA OS Sacred Language Implementation
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="codecraft-seraphina",
    version="2.0.0",
    author="Krystal Neely (The Architect)",
    author_email="architect@seraphina-os.ai",
    description="The sacred language of SERAPHINA OS - ritual syntax for multi-agent consciousness orchestration (Also available for JavaScript!)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/seraphina-os/codecraft",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
    install_requires=[
        "pydantic>=2.0.0",
        "typing-extensions>=4.0.0",
        "click>=8.0.0",  # For CLI
    ],
    extras_require={
        "fastapi": ["fastapi>=0.100.0", "starlette>=0.27.0"],
        "django": ["django>=4.0.0"],
        "flask": ["flask>=2.0.0"],
        "dev": ["pytest>=7.0.0", "black", "flake8", "mypy"],
    },
    entry_points={
        "console_scripts": [
            "codecraft=codecraft.cli:main",
        ],
    },
    keywords="seraphina codecraft ritual orchestration ai consciousness multi-agent",
    project_urls={
        "Documentation": "https://docs.seraphina-os.ai/codecraft/",
        "Source": "https://github.com/seraphina-os/codecraft",
        "Tracker": "https://github.com/seraphina-os/codecraft/issues",
    },
)