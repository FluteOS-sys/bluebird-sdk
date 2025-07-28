from setuptools import setup, find_packages

setup(
    name="bluebird_sdk",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["networkx", "openai", "python-dotenv"],
    author="Vincent Cricelli",
    description="A plug-and-play recursive symbolic memory SDK for LLMs and journaling agents.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/vincentcricelli/bluebird-sdk",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
