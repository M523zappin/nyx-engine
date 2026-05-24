"""
NYX // EVOLUTION ENGINE: REASONING & DISTILLATION
"""
import json
import subprocess

class ReasoningDistiller:
    """Manages the creation of custom reasoning models."""
    
    @staticmethod
    def distill_reasoning(data_path="reasoning_dataset.jsonl"):
        """Triggers local training to generate a custom reasoning adapter."""
        print("DISTILLING: Nyx is evolving its reasoning model...")
        # Execute local training process
        training_cmd = [
            "python", "train_lora.py", 
            "--model", "base_model_path",
            "--data", data_path,
            "--output", "nyx_reasoning_adapter"
        ]
        return subprocess.run(training_cmd, capture_output=True, text=True)

class EvolutionaryEngine:
    """Captured thought-trace storage."""
    @staticmethod
    def capture_reasoning(input_prompt, reasoning_trace, output_code):
        """Stores the 'Why' and the 'How' for future distillation."""
        entry = {
            "prompt": input_prompt,
            "reasoning": reasoning_trace,
            "output": output_code
        }
        with open("reasoning_dataset.jsonl", "a") as f:
            f.write(json.dumps(entry) + "\n")
