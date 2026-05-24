import ast
import sys

# Define your allowed native imports
ALLOWED_IMPORTS = {'os', 'sys', 'mmap', 'time', 'ast', 'json', 'asyncio'}

def check_code(filename):
    with open(filename, "r") as f:
        tree = ast.parse(f.read())
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    if alias.name not in ALLOWED_IMPORTS:
                        print(f"SENTINEL VIOLATION: '{alias.name}' is an external dependency.")
                        sys.exit(1)
            elif isinstance(node, ast.ImportFrom):
                if node.module not in ALLOWED_IMPORTS:
                    print(f"SENTINEL VIOLATION: '{node.module}' is an external dependency.")
                    sys.exit(1)

if __name__ == "__main__":
    check_code("NyxEngine.py")
