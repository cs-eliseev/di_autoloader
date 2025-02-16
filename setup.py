from setuptools import setup, find_packages

setup(
    name="di_autoloader",
    version="0.0.1",
    description="Dependency Injector Autoloader",
    author="Eliseev Alexey",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "dependency-injector>=4.45.0"
    ],
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.5",
)