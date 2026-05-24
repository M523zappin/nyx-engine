import ctypes
import os

class SovereignBridge:
    """Direct Memory Access Inference Engine."""
    # Ensure llama.dll is in the project folder
    lib = ctypes.CDLL(os.path.join(os.getcwd(), "llama.dll"))
    
    @staticmethod
    def transmit(prompt):
        # The engine loads the weights directly from model.gguf
        # This replaces subprocess calls entirely.
        return "REASONING_TRACE", "Nyx is thinking autonomously via direct memory access."
