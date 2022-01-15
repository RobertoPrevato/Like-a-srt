![Build](https://github.com/RobertoPrevato/Like-a-srt/workflows/Build/badge.svg)
[![pypi](https://img.shields.io/pypi/v/like-a-srt.svg)](https://pypi.python.org/pypi/like-a-srt)
[![versions](https://img.shields.io/pypi/pyversions/like-a-srt.svg)](https://github.com/RobertoPrevato/like-a-srt)
[![license](https://img.shields.io/github/license/RobertoPrevato/like-a-srt.svg)](https://github.com/RobertoPrevato/like-a-srt/blob/main/LICENSE)

# Like a SRT
CLI to generate SRT subtitles automatically from audio files, using [Azure Speech](https://azure.microsoft.com/en-us/services/cognitive-services/speech-services/#overview).

```bash
pip install like-a-srt
```

![Drawing](https://gist.githubusercontent.com/RobertoPrevato/b9f5162bfe6082876ec2d9811cc554b0/raw/9317c60cd5913c35a24103ef0cfd9c1e8e28c0e8/like-a-srt-800px.png)

## Getting started

**Requirements**

* Python 3.9
* An Azure Speech service

How to use:
1. configure environmental variables (recommended: create an `.env` file as in
   the example below)
2. install the CLI (e.g. installing the package using `pip`, in a Python virtual environment)
3. generate subtitles in `.srt` format using the command `las gen -s example.wav`

Example `.env` file, to configure the necessary environmental variables:

```ini
SPEECH_SUBSCRIPTION="<YOUR_AZURE_SPEECH_SUBSCRIPTION>"
SPEECH_ENDPOINT="<YOUR_AZURE_SPEECH_ENDPOINT>"
```

Example endpoint value: `https://westeurope.api.cognitive.microsoft.com/sts/v1.0/issuetoken`.

---

Example: generate a subtitles file `example.srt` from a source file
`example.wav`:

```bash
las gen -s example.wav
```

---

To create a .wav file from a source video, it's possible to use
[`ffmpeg`](https://www.ffmpeg.org):

```bash
ffmpeg -i source.mp4 destination.wav
```
