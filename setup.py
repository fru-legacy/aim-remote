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
        'uvicorn'
    ],
    entry_points={
        'console_scripts': [
            'aimremote=aimremote.cli:cli'
        ],
    },
)
