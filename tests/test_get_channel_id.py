import pytest
from yt_channel_scraper import YoutubeScraper


# Test get_channel_id() function
def test_get_channel_id():
    url = "https://www.youtube.com/channel/UC16niRr50-MSBwiO3YDb3RA"
    scraper = YoutubeScraper(url)
    channel_id = scraper.get_channel_id(url)
    assert (
        channel_id == "UC16niRr50-MSBwiO3YDb3RA"
    )  # Check if correct channel ID is returned
