import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="securedrop-qubesproxy",
    version="0.0.1",
    author="Kushal Das",
    author_email="kushal@freedom.press",
    description="Python API for accesing SecureDrop API in QubesOS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="GPLv3+",
    install_requires=["requests",],
    python_requires=">=3.5",
    url="https://github.com/freedomofpress/securedrop-qubesproxy",
    packages=setuptools.find_packages(exclude=["docs", "tests"]),
    data_files=[('bin', [("sd-network-proxy"),]),],
    classifiers=(
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
    ),
)
