import os
import subprocess
import sys


def run_backend():
    cmd = [sys.executable, "-m", "uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "8000"]
    subprocess.Popen(cmd, cwd=os.getcwd())


def run_ui():
    cmd = [sys.executable, "-m", "streamlit", "run", "app.py", "--server.port", "8501"]
    subprocess.Popen(cmd, cwd=os.getcwd())


if __name__ == "__main__":
    run_backend()
    run_ui()
    print("Backend and Streamlit UI started. Open http://localhost:8501")
