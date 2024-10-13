# ffm_convertor.py

import ffmpeg


class FFMConvertor:
    # i just discovered what this staticmethod python decorator is.
    # afaik, you use this whenever you have a member function that is not manipulating and class variable data,
    # thus you declare it as a staatic method so that it cannot access the `self.` variables?
    @staticmethod
    def convert_webm_to_mp4_module(input_webm_path, output_mp4_path):
        """let's convert this .webm file to .mp4, boss!"""
        try:
            input_video = ffmpeg.input(input_webm_path)
            stream = ffmpeg.output(input_video, output_mp4_path)
            ffmpeg.run(stream)
            print(
                f"success! converted '{input_webm_path}' to '{output_mp4_path}', dude!"
            )
        except Exception as e:
            print("watch out bruh! an error occurred:", e)

    @staticmethod
    def convert_mp4_to_gif_module(
        input_mp4_path, output_gif_path, start_time, duration
    ):
        """let's transform this .mp4 file into a stunning .gif, my friend!"""
        try:
            input_video = ffmpeg.input(input_mp4_path, ss=start_time, t=duration)
            # building the filter chain for gif conversion
            palette = input_video.filter("split")[0].filter("palettegen")
            stream = ffmpeg.filter([input_video, palette], "paletteuse")

            ffmpeg.output(stream, output_gif_path, loop=0).run()
            print(
                f"success! converted '{input_mp4_path}' to '{output_gif_path}', dude!"
            )
        except Exception as e:
            print("whoa dude! like, an error occurred:", e)
