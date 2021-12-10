from setuptools import setup, find_packages

setup(
    name='aim-remote',
    version='0.0.1',
    packages=find_packages(include=['aim-remote', 'aim-remote.*']),
    install_requires=[
        'aim'
    ]
)
