from setuptools import setup

from likeasrt import version


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="like-a-srt",
    version=version,
    description="Project template",
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/RobertoPrevato/PythonTemplate",
    author="RobertoPrevato",
    author_email="roberto.prevato@gmail.com",
    keywords="template",
    license="MIT",
    packages=["likeasrt"],
    entry_points={
        "console_scripts": ["like-a-srt=likeasrt.main:main", "las=likeasrt.main:main"]
    },
    install_requires=[
        "click",
        "essentials",
        "azure-cognitiveservices-speech==1.19.0",
    ],
    include_package_data=True,
)
