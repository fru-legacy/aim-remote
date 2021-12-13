from setuptools import setup, find_packages

setup(
    name='aim-remote',
    version='0.0.1',
    packages=find_packages(include=['aimremote', 'aimremote.*']),
    install_requires=[
        'aim',
        'fastapi>=0.65.0,<0.68.0',
        'click>=7.0',
        'asyncio',
        'uvicorn',
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'aim-remote=aimremote.cli:cli'
        ],
    },
)

# Execute locally using:
# python -m aim-remote.cli up --security-token Passtoken12345
# python ./aimremote/cli.py up --security-token Passtoken12345
