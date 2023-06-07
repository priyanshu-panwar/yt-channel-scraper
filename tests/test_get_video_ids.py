import pytest
from yt_channel_scraper import YoutubeScraper


def test_get_video_ids():
    url = "https://www.youtube.com/channel/UC16niRr50-MSBwiO3YDb3RA"
    scraper = YoutubeScraper(url)
    video_ids = scraper.get_video_ids(limit=10)
    assert len(video_ids) == 10  # Check if 10 video IDs are returned
