from setuptools import setup

setup(
    name="di_autoloader",
    version="0.1.3",
    description="Dependency Injector Autoloader",
    author="Eliseev Alexey",
    license="MIT",
    url="https://github.com/cs-eliseev/di_autoloader",
    packages=["di_autoloader"],
    package_dir={"di_autoloader": "di_autoloader"},
    install_requires=[
        "dependency-injector>=4.45.0"
    ],
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.5",
)