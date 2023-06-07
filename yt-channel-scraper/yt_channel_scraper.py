import scrapetube
from youtube_transcript_api import YouTubeTranscriptApi
import requests
from bs4 import BeautifulSoup


class YoutubeScraper:
    def __init__(self, url: str):
        try:
            self.channel_id = self.get_channel_id(url)
        except Exception:
            raise Exception("Channel Not Found")
        self.video_ids = []

    def get_video_ids(self, limit: int = 20):
        videos = scrapetube.get_channel(self.channel_id)
        cnt = 0
        for video in videos:
            self.video_ids.append(video["videoId"])
            cnt += 1
            if cnt >= limit:
                break
        return self.video_ids

    def __get_video_transcript_util(self, video_id: str):
        raw_transcript = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = ""
        for t in raw_transcript:
            transcript += t["text"] + " "
        return transcript

    def get_video_transcript(self, video_id: str = None):
        if video_id != None:
            return self.__get_video_transcript_util(video_id)
        transcripts = []
        for v_id in self.video_ids:
            transcripts.append(self.__get_video_transcript_util(v_id))
        return transcripts

    def get_channel_id(self, url: str):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        canonical_link = soup.find("link", rel="canonical")
        href_value = canonical_link.get("href")
        return href_value.split("/channel/")[1]
