import shutil
from aws_cdk import (
  aws_lambda as lambda_,
)
from constructs import Construct

from ..config import LAMDA_PYTHON_VERSION

import os

def generate_dependencies_layer(scope: Construct)-> lambda_.LayerVersion:

  layer_directory = 'dist'
  python_directory = os.path.join(layer_directory, 'python')

  # Define the output directory
  output_dir = os.path.join(os.getcwd(), python_directory) # Ensure absolute path

  # Ensure the output directory exists
  os.makedirs(output_dir, exist_ok=True)

  # Use uv pip install to install dependencies directly into the output directory
  print(f"Removing existing files from {python_directory}")
  shutil.rmtree(python_directory, ignore_errors=True)
  os.makedirs(output_dir, exist_ok=True)

  #  --only-binary=:all:  forces uv to install only pre-built wheels and error if not available
  # --upgrade forces the latest version to be installed
  command = f" uv pip install . --target {layer_directory}/python --python-platform x86_64-manylinux2014 --python-version {{cookiecutter.python_version}}"

  print(f"Running command: {command}")
  os.system(command)

  layer_code = lambda_.Code.from_asset(layer_directory)


  return lambda_.LayerVersion(scope, "APILayerDependenciesLayer",
      code=layer_code, # Use the variable here
      compatible_runtimes=[LAMDA_PYTHON_VERSION],
      description="Dependencies for API Layer"
  )
