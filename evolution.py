import ast

class RecursiveImprover:
    """The engine Nyx uses to rewrite its own logic."""
    def analyze_self(self):
        with open("NyxEngine.py", "r") as f:
            tree = ast.parse(f.read())
            # Nyx inspects its own function complexity
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    # Flag functions that are becoming too complex
                    if len(node.body) > 20:
                        return f"CRITICAL: {node.name} requires refactoring."
        return "System state: Optimal."

    def apply_patch(self, patch_code):
        # Nyx commits changes to its own codebase
        with open("NyxEngine.py", "w") as f:
            f.write(patch_code)
