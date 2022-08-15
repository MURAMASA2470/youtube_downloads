# youtube_downloads

Download videos or music from Youtube using youtube_dl and ffmpeg

## Environment

- python 3.x

## Installation

```
python -m pip install youtube_dl ffmpeg
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

```
wget https://github.com/ytdl-org/youtube-dl/archive/d231b56717c73ee597d2e077d11b69ed48a1b02d.zip

unzip d231b56717c73ee597d2e077d11b69ed48a1b02d.zip

cd youtube-dl-d231b56717c73ee597d2e077d11b69ed48a1b02d

python -m pip uninstall youtube_dl
python -m pip install .
```
