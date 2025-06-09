import subprocess
import sys
import shlex  # For safely splitting shell arguments

def setup_env():
    command = ["uv", "sync", "--all-groups"]


    print(f"Executing command: {' '.join(shlex.quote(arg) for arg in command)}")

    try:
        import os
        print("path is", os.getcwd())
        env = {"HOST": os.environ.get("HOST","127.0.0.1"), **os.environ}  # Inherit existing environment variables
        process = subprocess.Popen(command, stdout=sys.stdout, stderr=sys.stderr, env=env)
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










def main ():
  setup_env()



main()
