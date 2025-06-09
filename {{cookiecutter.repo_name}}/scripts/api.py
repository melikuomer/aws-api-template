# my_package/deployment_scripts.py
import subprocess
import sys
import shlex  # For safely splitting shell arguments

def start_app():
    base_command = ["uv", "run", "-m", "api.handler"]
    user_arguments = sys.argv[1:]  # Get arguments passed to the Python script

    full_command = base_command + user_arguments

    print(f"Executing command: {' '.join(shlex.quote(arg) for arg in full_command)}")

    try:
        import os

        env = {"HOST": os.environ.get("HOST","127.0.0.1"), **os.environ}  # Inherit existing environment variables
        process = subprocess.Popen(full_command, stdout=sys.stdout, stderr=sys.stderr, env=env)
        process.wait()
        if process.returncode != 0:
            print(f"Error during deployment (exit code: {process.returncode})")
            sys.exit(1)
        else:
            print("Development deployment configuration synthesized successfully.")
    except FileNotFoundError as e:
        print(f"Error: Command not found - {e.filename}. Make sure it's in your PATH.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
