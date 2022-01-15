from setuptools import setup

from likeasrt import VERSION


def readme():
    with open("README.md", encoding="utf8") as readme_file:
        return readme_file.read()


setup(
    name="like-a-srt",
    version=VERSION,
    description=(
        "CLI to generate SRT subtitles automatically from audio files, "
        "using Azure Speech"
    ),
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/RobertoPrevato/Like-a-srt",
    author="RobertoPrevato",
    author_email="roberto.prevato@gmail.com",
    keywords="azure speech srt subtitles automatic generation",
    license="MIT",
    packages=["likeasrt"],
    entry_points={
        "console_scripts": ["like-a-srt=likeasrt.main:main", "las=likeasrt.main:main"]
    },
    install_requires=[
        "click==8.0.3",
        "essentials==1.1.4",
        "azure-cognitiveservices-speech==1.19.0",
    ],
    include_package_data=True,
)
