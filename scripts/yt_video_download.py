# Works on Python 3.10.4
# Before running script install following
# pip install pytube
# pip3 install pytube
# pip install pytube3
# pip install --upgrade youtube-dl

from __future__ import unicode_literals
import youtube_dl

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?...'])