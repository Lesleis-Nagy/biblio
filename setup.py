from setuptools import setup, find_packages

setup(
    name="biblio",
    version="0.0.0",
    packages=find_packages(
        where="lib",
        include="biblio/*"
    ),
    package_dir={"": "lib"},
    install_requires=[
        "typer",
        "sqlalchemy",
        "rich",
        "PyQt5",
        "Pillow",
        "numpy"
    ],
    entry_points="""
    [console_scripts]
    biblio=biblio.entry_point:main
    """
)
