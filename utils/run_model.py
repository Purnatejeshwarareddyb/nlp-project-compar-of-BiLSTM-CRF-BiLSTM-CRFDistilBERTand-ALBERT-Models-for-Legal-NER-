"""
Model execution handler for Legal NER System Hub
Author: B. Purna Tejeshwara Reddy
"""

import subprocess
import sys
import os
from pathlib import Path

# Model paths relative to the root legal_ner_project directory
model_paths = {
    "CRF": "crf_model_training/main.py",
    "BiLSTM": "bilstm_model_training/main.py",
    "BiLSTM+CRF": "bilstm_crf_model_training/main.py",
    "ALBERT": "Legal_NER_ALBERT/main.py",
    "DistilBERT": "DistilBERT_Model_training/main.py"
}

# Store running processes
active_processes = {}


def run_model(model_name):
    """
    Launch a model's main.py file in a separate process

    Args:
        model_name (str): Name of the model to run

    Returns:
        subprocess.Popen: The process object, or None if failed
    """
    if model_name not in model_paths:
        print(f"Error: Unknown model '{model_name}'")
        return None

    model_path = model_paths[model_name]

    # Resolve the absolute path (from current working directory)
    full_path = Path(model_path).resolve()

    # Check if file exists
    if not full_path.exists():
        print(f"Error: Model file not found at {full_path}")
        print(f"Current working directory: {os.getcwd()}")
        return None

    try:
        # Get the directory of the model
        model_dir = full_path.parent

        # Launch the model in a new process
        process = subprocess.Popen(
            [sys.executable, str(full_path)],
            cwd=str(model_dir),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        # Store the process
        active_processes[model_name] = process

        print(f"✓ Successfully launched {model_name} model (PID: {process.pid})")
        return process

    except Exception as e:
        print(f"Error launching {model_name}: {str(e)}")
        return None


def is_model_running(model_name):
    """Check if a model is currently running"""
    if model_name in active_processes:
        process = active_processes[model_name]
        return process.poll() is None
    return False


def stop_model(model_name):
    """Stop a running model"""
    if model_name in active_processes:
        process = active_processes[model_name]
        if process.poll() is None:
            process.terminate()
            print(f"✓ Stopped {model_name} model")
            del active_processes[model_name]
            return True
    return False


def stop_all_models():
    """Stop all running models"""
    for model_name in list(active_processes.keys()):
        stop_model(model_name)