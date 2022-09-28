import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="escape-unk",
    description="Escape unknown symbols in SentecePiece vocabularies",
    author="Jaume Zaragoza",
    author_email="jzaragoza@prompsit.com",
    long_description=long_description,
    url="https://github.com/ZJaume/escape-unk",
    packages=setuptools.find_packages(),
    install_requires=[
        "regex",
        "sentencepiece",
    ],
    entry_points={
        "console_scripts": [
            "escape-unk=escape_unk.escape_unk:main",
            "unescape-unk=escape_unk.unescape_unk:main",
        ],
    },
)
