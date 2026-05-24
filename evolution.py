"""
NYX // EVOLUTION ENGINE
Core logic for self-analysis, recursive improvement, and interaction logging.
Zero-Dependency Architecture.
"""

import ast
import json
import os

class EvolutionaryEngine:
    """Handles interaction telemetry and code integrity."""
    
    LOG_FILE = "evolve.jsonl"
    CORE_FILE = "NyxEngine.py"

    @staticmethod
    def log_interaction(prompt, response):
        """Records state interactions for future training sets."""
        with open(EvolutionaryEngine.LOG_FILE, "a") as f:
            f.write(json.dumps({"input": prompt, "output": response}) + "\n")

class RecursiveImprover:
    """The Sentinel: Analyzes and optimizes core logic."""
    
    @staticmethod
    def get_complexity_report():
        """Scans NyxEngine.py for architectural bloat."""
        with open(EvolutionaryEngine.CORE_FILE, "r") as f:
            tree = ast.parse(f.read())
            
        report = []
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                # Flag functions exceeding 20 lines (maintainability threshold)
                if len(node.body) > 20:
                    report.append(f"BLOAT_DETECTED: {node.name}")
        return report if report else ["STATUS: OPTIMAL"]

    @staticmethod
    def apply_patch(new_code):
        """Self-updates the core engine."""
        with open(EvolutionaryEngine.CORE_FILE, "w") as f:
            f.write(new_code)

if __name__ == "__main__":
    # Self-Diagnostics Run
    print("EVOLUTIONARY SCAN INITIATED...")
    print(f"REPORT: {RecursiveImprover.get_complexity_report()}")
