# yt-channel-scraper
[![📦️Upload PyPi Package](https://github.com/priyanshu-panwar/yt-channel-scraper/actions/workflows/publish.yml/badge.svg)](https://github.com/priyanshu-panwar/yt-channel-scraper/actions/workflows/publish.yml) [![🧪Test](https://github.com/priyanshu-panwar/yt-channel-scraper/actions/workflows/test.yml/badge.svg)](https://github.com/priyanshu-panwar/yt-channel-scraper/actions/workflows/test.yml)

```
All in one Youtube Tool for Python.
```

Helps you fetch the following things of a youtube channel:
- channel_id
- videos (video_ids)
- video transcripts
- download videos

## channel_id
```
from yt_channel_scraper import YoutubeScraper

fy = YoutubeScraper("channel-link")
print(fy.get_channel_id())
```

## videos
```
from yt_channel_scraper import YoutubeScraper

fy = YoutubeScraper("channel-link")
print(fy.get_video_ids(limit=20)) # limit is number of latest videos you need
```

## video transcripts
```
from yt_channel_scraper import YoutubeScraper

fy = YoutubeScraper("channel-link")
v_ids = fy.get_video_ids(limit=20)
print(fy.get_video_transcript()) # fetch video transcripts of all videos
print(fy.get_video_transcript(video_id="video-id")) # fetch video transcript of single video
```

## download videos
```
from yt_channel_scraper import YoutubeDownloader

yd = YoutubeDownloader("video-link")
print(yd.get_download_streams()) # show the available streams to download with tags
yd.download_stream("tag") # give the tag from available streams whichever to download
yd.download_highest_resolution() # download highest resolution available
```