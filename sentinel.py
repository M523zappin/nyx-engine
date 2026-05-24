"""
NYX // SENTINEL GATEKEEPER
Ensures Zero-Dependency integrity.
"""
import ast

# Explicitly defining permitted imports within our architecture
ALLOWED_IMPORTS = {'os', 'sys', 'mmap', 'time', 'ast', 'json', 'asyncio', 'sentinel', 'evolution'}

def check_code(filename):
    """Parses a file's AST structure to ensure no external libraries are imported."""
    try:
        with open(filename, "r") as f:
            tree = ast.parse(f.read())
            
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    if alias.name not in ALLOWED_IMPORTS:
                        print(f"\nSENTINEL VIOLATION: '{alias.name}' is unauthorized.")
                        return False
            elif isinstance(node, ast.ImportFrom):
                if node.module not in ALLOWED_IMPORTS:
                    print(f"\nSENTINEL VIOLATION: '{node.module}' is unauthorized.")
                    return False
        return True
    except Exception as e:
        print(f"\nSENTINEL ERROR: Unable to scan file framework. Details: {e}")
        return False
