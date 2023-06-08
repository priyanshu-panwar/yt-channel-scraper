from pytube import YouTube


class YoutubeDownloader:
    def __init__(self, link: str) -> None:
        self.yt = YouTube(link)
        self.title = self.yt.title
        self.views = self.yt.views
        self.length = self.yt.length

    def download_highest_resolution(self):
        ys = self.yt.streams.get_highest_resolution()
        print(":: Downloading ::")
        ys.download()
        print(":: Download completed ::")

    def get_download_streams(self):
        stream = str(self.yt.streams.filter(progressive=True))
        stream = stream[1:]
        stream = stream[:-1]
        return stream.split(", ")

    def download_stream(self, tag: str):
        ys = self.yt.streams.get_by_itag(tag)
        print(":: Downloading ::")
        ys.download()
        print(":: Download completed ::")
