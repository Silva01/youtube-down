import youtube_dl


class Download:

    def mp3(self, url):
        youtube_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192'
            }],
            'postprocessor_args': [
                '-ar', '16000'
            ],
            'prefer_ffmpeg': True,
            'keepvideo': True
        }
        self.__download_file(youtube_opts, url)

    def mp4(self, url):
        youtube_opts = {}
        self.__download_file(youtube_opts, url)

    def personal(self, youtube_opts, url):
        self.__download_file(youtube_opts, url)

    @staticmethod
    def __download_file(youtube_opts, url):
        with youtube_dl.YoutubeDL(youtube_opts) as ydl:
            print(url)
            ydl.download(url)
