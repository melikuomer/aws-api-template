import subprocess
import sys
import shlex  # For safely splitting shell arguments
import os
from typing import Dict, List

def run_command(command: List[str], env: Dict[str,str]={}, cwd: str=None):
    """
    Runs a shell command and returns the exit code.  If the exit code is non-zero, the program exits.
    """

    print(f"Executing command: {' '.join(shlex.quote(arg) for arg in command)}")
    try:
        process = subprocess.Popen(command, stdout=sys.stdout, stderr=sys.stderr, env=env, cwd=cwd)
        process.wait()
        if process.returncode != 0:
            print(f"Error during command execution (exit code: {process.returncode})")
            sys.exit(1)
        return process.returncode
    except FileNotFoundError as e:
        print(f"Error: Command not found - {e.filename}. Make sure it's in your PATH.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


def setup_env():
    command = ["uv", "sync", "--all-groups"]
    env = {"HOST": os.environ.get("HOST","127.0.0.1"), **os.environ}  # Inherit existing environment variables
    print("path is", os.getcwd())
    return_code = run_command(command, env=env)
    if return_code == 0:
        print("Development deployment configuration synthesized successfully.")


def init_git():
    command = ["git", "init"]
    env = { **os.environ}  # Inherit existing environment variables
    print("path is", os.getcwd())
    return_code = run_command(command, env=env)
    if return_code == 0:
        print("Git repository initialized successfully.")


def initial_commit():
    command = ["git", "add", "."]
    env = { **os.environ}  # Inherit existing environment variables
    print("path is", os.getcwd())
    return_code = run_command(command, env=env)
    if return_code != 0:
        return

    command = ["git", "commit", "-m", "Initial commit"]
    env = { **os.environ}  # Inherit existing environment variables
    print("path is", os.getcwd())
    return_code = run_command(command, env=env)
    if return_code == 0:
        print("Initial commit created successfully.")






def main ():
  setup_env()
  init_git()
  initial_commit()


main()
