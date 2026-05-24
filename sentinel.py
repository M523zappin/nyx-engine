"""
NYX // SENTINEL GATEKEEPER
Ensures Zero-Dependency integrity.
"""
import ast

ALLOWED_IMPORTS = {'os', 'sys', 'mmap', 'time', 'ast', 'json', 'asyncio', 'sentinel', 'evolution'}

def check_code(filename):
    try:
        with open(filename, "r") as f:
            tree = ast.parse(f.read())
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    if alias.name not in ALLOWED_IMPORTS:
                        print(f"\nSENTINEL VIOLATION: '{alias.name}' is an external dependency.")
                        return False
            elif isinstance(node, ast.ImportFrom):
                if node.module not in ALLOWED_IMPORTS:
                    print(f"\nSENTINEL VIOLATION: '{node.module}' is an external dependency.")
                    return False
        return True
    except Exception:
        return False
