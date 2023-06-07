from setuptools import setup

setup(
    name="FetchYoutube",
    version="1.0.0",
    description="Fetch channel_id, videos, transcript from a youtube channel",
    author="Priyanshu Panwar",
    author_email="priyanshu009ch@gmail.com",
    packages=["FetchYoutube"],
    install_requires=[
        "scrapetube",
        "youtube-transcript-api",
        "requests",
        "beautifulsoup4",
    ],
)
