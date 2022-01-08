from foo import version
from setuptools import setup


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="foo",
    version=version,
    description="Project template",
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/RobertoPrevato/PythonTemplate",
    author="RobertoPrevato",
    author_email="roberto.prevato@gmail.com",
    keywords="template",
    license="MIT",
    packages=["foo"],
    entry_points={"console_scripts": ["foo=foo.main:main"]},
    install_requires=["click", "essentials"],
    include_package_data=True,
)
