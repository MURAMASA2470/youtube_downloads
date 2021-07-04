import youtube_dl
import ffmpeg
import sys
import os
import glob

def dl(URL):
	options = {
		'format': 'bestaudio[ext=mp3]/bestaudio[ext=m4a]/bestaudio'
	}
	with youtube_dl.YoutubeDL(options) as ydl:
		ydl.download([URL])

def mp4to3(filename):
  root, ext = os.path.splitext(filename)
  if ext not in ['.m4a']: return
  newname = '%s.mp3' % root
  stream = ffmpeg.input(filename)
  stream = ffmpeg.output(stream, newname, format='mp3', audio_bitrate=320)
  ffmpeg.run(stream)
  os.remove(filename)

def main():
	format = input('Format(mp3 or mp4): ')
	url = input('URL: ')
	if format == 'mp4':
		cmd = 'youtube-dl -f mp4 {URL} --no-check-certificate'.format(URL = url)
		os.system(cmd)
	else:
		dl(url)
		filenames = glob.glob('./*.m4a')
		for filename in filenames:
			mp4to3(filename)

main()