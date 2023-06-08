from setuptools import setup
from pathlib import Path

readme_file = Path(__file__).resolve().parent / "README.md"
with open(readme_file, encoding="utf-8") as f:
    readme_content = f.read()

setup(
    name="yt-channel-scraper",
    version="0.1.1",
    description="All in one Youtube Solution for python. Scrap, Fetch, Download anything from a Youtube Channel, Video.",
    long_description=readme_content,
    long_description_content_type="text/markdown",
    author="Priyanshu Panwar",
    author_email="priyanshu009ch@gmail.com",
    packages=["yt_channel_scraper"],
    project_urls={
        "Source": "https://github.com/priyanshu-panwar/yt-channel-scraper",
    },
    install_requires=[
        "scrapetube",
        "youtube-transcript-api",
        "requests",
        "beautifulsoup4",
        "pytube",
    ],
)
