import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "dashdot",
    version = "0.0.0",
    author = "Saran",
    author_email = "rsarans186@gmail.com",
    description = "A dotfiles manager to cure my sucky workflow",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/Try3D/dashdot",
    project_urls = {
        "Bug Tracker": "https://github.com/Try3D/dashdot/issues",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.6"
)
