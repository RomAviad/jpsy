from setuptools import find_packages, setup

setup(
    name="jpsy",
    author="Aviad Rom",
    version="0.1.0",
    packages=find_packages(),
    description="Enforcing Language Naming Conventions",
    long_description=open("README.md").read(),
    url="https://github.com/RomAviad/jpsy",
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Development Status :: 4 - Beta"
    ]
)
