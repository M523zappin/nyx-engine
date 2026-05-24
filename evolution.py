import os

class AutonomyManager:
    """Monitors dataset growth and triggers self-evolution."""
    THRESHOLD = 50  # Number of reasoning traces required before distilling
    
    @staticmethod
    def check_evolution_readiness():
        if os.path.exists("reasoning_dataset.jsonl"):
            with open("reasoning_dataset.jsonl", "r") as f:
                count = sum(1 for _ in f)
            if count >= AutonomyManager.THRESHOLD:
                print("THRESHOLD MET: Triggering model distillation...")
                ReasoningDistiller.distill_reasoning()
