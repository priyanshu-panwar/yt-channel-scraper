import pytest
from ..yt_channel_scraper.yt_channel_scraper import YoutubeScraper


# Test get_video_transcript() function
def test_get_video_transcript():
    url = "https://www.youtube.com/channel/UC16niRr50-MSBwiO3YDb3RA"
    scraper = YoutubeScraper(url)
    video_transcripts = scraper.get_video_transcript(video_id="VIDEO_ID")
    assert len(video_transcripts) == 1  # Check if transcript for one video is returned
