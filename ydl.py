import youtube_dl
import ffmpeg
import sys
import os
import glob
import argparse
import re

# Download and convert
def dl(url, format):
  options = {
    'nocheckcertificate:': True
	}
  if format == 'mp3':
    options['format'] = 'bestaudio[ext=mp3]/bestaudio[ext=m4a]/bestaudio'
    youtube_dl.YoutubeDL(options).download([url])

    filenames = glob.glob('./*.m4a')
    for filename in filenames:
      mp4to3(filename)
  else:
    options['format'] = 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4/best'
    youtube_dl.YoutubeDL(options).download([url])

# Conver to mp3
def mp4to3(filename):
  root, ext = os.path.splitext(filename)
  if ext not in ['.m4a']: return
  newname = '%s.mp3' % root
  stream = ffmpeg.input(filename)
  stream = ffmpeg.output(stream, newname, format='mp3', audio_bitrate=320)
  ffmpeg.run(stream)
  os.remove(filename)

# Batch download
def dl4List(args):
  try:
    file = open(args.list, 'r', encoding='UTF-8')
    urls = file.readlines()
    for url in urls:
      dl(url, args.format)
    file.close()
  except FileNotFoundError as e:
    print('[Error] => File Not Found: ', e)
  finally:
    sys.exit()

# validate to args
def validateArgs(args):
  err = None
  if (args.format and args.format not in ['mp3', 'mp4']):
      err = 'Incorrect format. Possible values are mp3 or mp4'
  if (args.uri and not re.match('((https?)?://)?[^/]+/', args.uri)):
      err = '\'{uri}\' is not a valid URL'.format(uri = args.uri)

  if (err is not None):
      print('[Error] => {error}'.format(error = err))
      sys.exit()

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('-f', '--format', help='Select the file format (mp3 or mp4) to download.')
  parser.add_argument('-u', '--uri', help='Specify the URI of the media to download.')
  parser.add_argument('-l', '--list', help='Specify a text file for the URL list.')
  args = parser.parse_args()

  validateArgs(args)

  if args.list:
    dl4List(args)

  format = args.format if (args.format) else input('Format(mp3 or mp4): ')
  url = args.uri if (args.uri) else input('URL: ')

  dl(url, format)

main()