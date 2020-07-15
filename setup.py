from setuptools import setup

install_requires = ["abjad", "abjad-ext-rmakers", "quicktions"]

setup(
    name="tsmakers",
    version="0.1dev",
    packages=["tsmakers"],
    install_requires=install_requires,
    license="Creative Commons Attribution-Noncommercial-Sharalike license",
    long_description=open("README.md").read(),
)
