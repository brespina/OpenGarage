import argparse
import os
import sys

from ..ffm_convertor import FFMConvertor


def parse_arguments():
    """time to grab some arguments, let's do this!"""
    parser = argparse.ArgumentParser(
        description="convert a .webm file to .mp4 format, gang!"
    )

    # if the user wants to copy their input video into the project folder
    parser.add_argument(
        "-ip",
        "--input-path",
        dest="input_webm_path",
        required=True,
        help="yo, give me the path to your .webm file, broski!",
        metavar="INPUT_webm_PATH",
    )

    parser.add_argument(
        "-of",
        "--output-file",
        dest="output_mp4_file",
        help="what's the name you wanna give to the delicious .mp4 file, my dude?",
        metavar="OUTPUT_MP4",
        default="output.mp4",
    )

    return parser.parse_args()


def get_file_paths(args):
    """let's build those file paths like a champ!"""
    current_directory = os.path.dirname(os.path.abspath(__file__))

    if args.input_webm_path is None:
        print(
            "bro, you can't show up to a party empty handed. give me that full path to your .webm file!"
        )
        print("use the -h option to see usage information")
        sys.exit(2)
    else:
        input_webm_path = args.input_webm_path

    output_dir = "output/"
    output_mp4_path = os.path.join(current_directory, output_dir, args.output_mp4_file)

    return input_webm_path, output_mp4_path


def main():
    """main event, baby!"""
    ffm = FFMConvertor()
    args = parse_arguments()

    # compute file path from args, feed as params into function
    input_webm_path, output_mp4_path = get_file_paths(args)
    ffm.convert_webm_to_mp4_module(input_webm_path, output_mp4_path)


if __name__ == "__main__":
    main()
