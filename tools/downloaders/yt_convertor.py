# yt_convertor.py
#
# This is the same download/conversion logic used by the standalone
# yt2mp3 pipx CLI, restructured to match this repo's shared-converter-class
# pattern (see ffm_convertor.py).

import shutil

from yt_dlp import YoutubeDL


class YTConvertor:
    @staticmethod
    def check_ffmpeg_installed():
        """Return True if ffmpeg is found on PATH, False otherwise."""
        return shutil.which("ffmpeg") is not None

    @staticmethod
    def build_ydl_options(output_dir, quality):
        """Construct the yt-dlp options dictionary for MP3 extraction."""
        output_template = output_dir.rstrip("/\\") + "/%(title)s.%(ext)s"

        postprocessor_options = {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": quality,
        }

        options = {
            "format": "bestaudio/best",
            "outtmpl": output_template,
            "postprocessors": [postprocessor_options],
            # don't accidentally download someone's whole playlist
            "noplaylist": True,
            # let yt-dlp use whichever JS runtime is installed (deno or node)
            # to solve YouTube's JS challenges; harmless if neither is present.
            "js_runtimes": {"deno": {}, "node": {}},
        }

        return options

    @staticmethod
    def download_audio(url, output_dir, quality):
        """Download the given URL and convert it to an MP3 file."""
        options = YTConvertor.build_ydl_options(output_dir, quality)

        with YoutubeDL(options) as downloader:
            downloader.download([url])
