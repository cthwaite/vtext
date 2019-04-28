from setuptools import find_packages, setup
from setuptools_rust import RustExtension


with open("./requirements.txt", "rt") as fh:
    install_requires = fh.read().splitlines()

setup(
    version="0.1.0a1",
    rust_extensions=[
        RustExtension(
            "vtext._lib",
            "./Cargo.toml",
            rustc_flags=["--cfg=Py_3"],
            features=["numpy/python3"],
        )
    ],
    long_description_content_type="text/markdown",
    install_requires=install_requires,
    packages=find_packages(),
)
