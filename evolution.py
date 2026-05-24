"""
NYX // SOVEREIGN LEARNING ENGINE
Pure native architecture for weight adaptation.
"""
import os
import json

class SovereignBrain:
    def __init__(self):
        self.weights = {}
        self.load_weights()

    def load_weights(self):
        if os.path.exists("nyx_weights.json"):
            try:
                with open("nyx_weights.json", "r") as f:
                    self.weights = json.load(f)
            except Exception:
                self.weights = {}

    def save_weights(self):
        with open("nyx_weights.json", "w") as f:
            json.dump(self.weights, f, indent=4)

    def infer(self, prompt):
        """Native token association processing."""
        tokens = prompt.lower().split()
        score = 0
        for token in tokens:
            score += self.weights.get(token, 0.1)
        
        if "build" in tokens or "make" in tokens or score > 1.0:
            return "ANALYSIS: Sovereign parameters recognized. Compiling self-contained sub-routines."
        return "ANALYSIS: Active input integrated into neural architecture memory maps."

class AutonomyManager:
    THRESHOLD = 5

    @staticmethod
    def check_evolution_readiness():
        if not os.path.exists("reasoning_dataset.jsonl"):
            return
            
        with open("reasoning_dataset.jsonl", "r") as f:
            lines = f.readlines()
            
        if len(lines) >= AutonomyManager.THRESHOLD:
            print("\n[EVOLUTION TRIGGERED: Adapting internal neural pathways...]")
            brain = SovereignBrain()
            
            for line in lines:
                try:
                    data = json.loads(line)
                    words = data.get("input", "").lower().split()
                    for word in words:
                        brain.weights[word] = brain.weights.get(word, 0.1) + 0.05
                except Exception:
                    continue
            
            brain.save_weights()
            print("[EVOLUTION COMPLETE: Nyx weight layers optimized natively.]")
            
            try:
                os.remove("reasoning_dataset.jsonl")
            except Exception:
                pass

class EvolutionaryEngine:
    @staticmethod
    def log_interaction(prompt, response):
        entry = {"input": prompt, "output": response}
        with open("reasoning_dataset.jsonl", "a") as f:
            f.write(json.dumps(entry) + "\n")
