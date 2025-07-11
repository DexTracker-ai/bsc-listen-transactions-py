from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="bsc-listen-transactions",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A Python library for listening to real-time BSC and other DEX transactions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/bsc-listen-transactions",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Office/Business :: Financial",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    install_requires=[
        "websockets>=11.0.3",
    ],
    keywords=[
        "bsc",
        "blockchain",
        "cryptocurrency",
        "dex",
        "trading",
        "websocket",
        "real-time",
        "transactions",
        "defi"
    ],
    project_urls={
        "Bug Reports": "https://github.com/yourusername/bsc-listen-transactions/issues",
        "Source": "https://github.com/yourusername/bsc-listen-transactions",
    },
)
