# youtube_downloads

Download videos or music from Youtube using youtube_dl and ffmpeg

## Environment

- python 3.x

## Installation

```
python -m pip install youtube_dl ffmpeg ffmpeg-python
```


## Using　

### Easy to Use
```
python ./ydl.py
> Format(mp3 or mp4): "Enter the format you want to convert here"
> URL: "Enter the URL you want to download here"
```

### Options
```
usage: ydl.py [-h] [-f FORMAT] [-u URI] [-l LIST]

  -h, --help           : show this help message and exit

  -f, --format Format  : Select the file format (mp3 or mp4) to download.

  -u, --uri URI        : Specify the URI of the media to download.

  -l, --list LIST      : Specify a text file for the URL list.
                         Bulk download resources from the list of URLs.

```

## How to deal with slow download speed

### In the case of Mac and Linux

```bash
# Get the SHA hash of the latest commit from git

hash=$(git ls-remote https://github.com/ytdl-org/youtube-dl.git | head -n 1 | cut -c 1-40)

wget https://github.com/ytdl-org/youtube-dl/archive/$hash.zip

unzip -n $hash.zip && cd youtube-dl-$hash

python -m pip uninstall -y youtube_dl && python -m pip install .

cd .. && rm -r youtube-dl-$hash
```

### In the case of Windows

```bash
# Get the SHA hash of the latest commit from git

$hash=$(git ls-remote https://github.com/ytdl-org/youtube-dl.git | Select-Object -First 1).Substring(0, 40)

Invoke-WebRequest -Uri https://github.com/ytdl-org/youtube-dl/archive/$hash.zip -outfile ./youtube-dl-$hash.zip

Expand-Archive -Path .\youtube-dl-$hash.zip -DestinationPath ./ ; cd youtube-dl-$hash

python -m pip uninstall -y youtube_dl ; python -m pip install .

cd .. ; rm -r youtube-dl-$hash

```

