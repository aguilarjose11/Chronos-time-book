import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Chronos-time-book",  # Replace with your own username
    version="0.0.1",
    author="Jose E. Aguilar Escamilla",
    author_email="joseaguilar@ou.edu",
    description="A time management package to keep track of worked hours with \
    a cli interface. ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aguilarjose11/Chronos-time-book.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=(
        "urwid>=2.1.0",
    )
)
