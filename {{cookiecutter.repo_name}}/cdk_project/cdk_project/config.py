from aws_cdk import(
    aws_lambda as lambda_,

)

LAMDA_PYTHON_VERSION = lambda_.Runtime.PYTHON_{{ cookiecutter.python_version.replace('.', '_') }}
