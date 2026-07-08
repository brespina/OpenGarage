# youtube_to_mp3.py
#
# Repo-embedded version of the yt2mp3 pipx CLI. Same core logic (ffmpeg
# check, yt-dlp options), adapted to run via `python -m` from the repo
# root and to save into this tool's own output/ folder by default.

import argparse
import os
import sys

from ..yt_convertor import YTConvertor


def parse_arguments():
    """Parse and return command-line arguments."""
    parser = argparse.ArgumentParser(
        prog="youtube_to_mp3",
        description="Download a YouTube video's audio as an MP3 file.",
    )

    parser.add_argument(
        "url",
        help="YouTube video URL to download",
    )

    parser.add_argument(
        "-o",
        "--output",
        default=None,
        help="Directory to save the MP3 file in (default: this tool's output/ folder)",
    )

    parser.add_argument(
        "-q",
        "--quality",
        default="192",
        help="MP3 bitrate in kbps, e.g. 128, 192, 320 (default: 192)",
    )

    return parser.parse_args()


def get_default_output_dir():
    """Build the path to this tool's own output/ folder."""
    current_directory = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_directory, "output")


def main():
    """Entry point for running this tool."""
    # Parse first so `-h/--help` works even when ffmpeg is missing.
    args = parse_arguments()

    if not args.quality.isdigit():
        print("Error: --quality must be a number in kbps, e.g. 128, 192, or 320.")
        sys.exit(2)

    if not YTConvertor.check_ffmpeg_installed():
        print("Error: ffmpeg was not found on your PATH.")
        print("This tool needs ffmpeg to convert audio to MP3.")
        print("Install it and make sure it's on PATH, then try again.")
        sys.exit(1)

    output_dir = args.output if args.output else get_default_output_dir()

    print("Downloading and converting: " + args.url)

    try:
        YTConvertor.download_audio(args.url, output_dir, args.quality)
    except Exception as error:
        print("Download failed: " + str(error))
        print(
            "\nIf this looks like a YouTube extraction error (e.g. 'SABR', "
            "'nsig', or 'the page needs to be reloaded'), yt-dlp is probably "
            "out of date. YouTube breaks older versions often; update with:\n"
            "    pip install -U yt-dlp"
        )
        sys.exit(1)

    print("Done. MP3 saved to: " + output_dir)


if __name__ == "__main__":
    main()
