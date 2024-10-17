"""
function that takes binary image. (black and white) and rle compresses it.
for binary image only two possible values.
we separate image into rows.
designate the starting color, every value represents color change.

most of this code comes from my digital image proc class.
"""

import ast
import os
import sys

import cv2
import numpy as np
from binarize import BinImage


def force_binary(image):
    binary = BinImage()
    result = binary.binarize(image)

    return result


def encode_image(binary_image):
    """
    takes a binary image as input
    returns run length encoding of image
    """

    copy_bin_image = binary_image.copy()
    rle = []
    count = 1
    for i in range(copy_bin_image.shape[0]):
        for j in range(copy_bin_image.shape[1]):

            # need to append last chunk of numbers. so append before continuing to next row
            if j == copy_bin_image.shape[1] - 1:
                rle.append(count)
                continue

            # first number indicates the starting color. no need to denote the value of pixel as the only reason
            # to switch count is if the other color has been encountered
            if j == 0:
                # cast as a string to avoid erroneous addition
                if copy_bin_image[i][j] == 255:
                    rle.append("W")
                else:
                    rle.append("B")
                count = 1

            # match, a run has occurred. increment count
            if copy_bin_image[i][j] == copy_bin_image[i][j + 1]:
                count += 1

            # don't match. append current count. and reset count. color has changed
            if copy_bin_image[i][j] != copy_bin_image[i][j + 1]:
                rle.append(count)
                count = 1

    return rle


def save_rle_to_file(rle_code, filename):
    with open(filename, "w") as f:
        f.write(str(rle_code))


def load_rle_from_file(filename):
    with open(filename, "r") as f:
        rle_string = f.read()
    return ast.literal_eval(rle_string)


def decode_image(filename, height, width):
    rle_code = load_rle_from_file(filename)
    decoded_image = np.zeros((height, width))

    rle_index = 0
    prev = 0  # holds the previous rle array integer to combine with k
    row_sum_pixel = 0
    i = 0
    while i < height:
        # if current elem of rle array is string. indicate starting color.
        if rle_code[rle_index] == "W":
            is_white = True
        elif rle_code[rle_index] == "B":
            is_white = False

        # string elements are just indicators of color. once indicated. move up.
        if isinstance(rle_code[rle_index], str):
            rle_index += 1

        # k controls how many pixels to give the proper color to.
        for k in range(rle_code[rle_index]):
            if is_white:
                decoded_image[i][
                    k + prev
                ] = 255  # we add prev. to ensure we continue where we left
            else:
                decoded_image[i][k + prev] = 0

        is_white = not is_white  # once k finishes. this indicates a color change
        prev += rle_code[rle_index]  # increment prev appropriately
        row_sum_pixel += rle_code[rle_index]  # controls when to go to new row.
        rle_index += 1  # move to next element in rle array

        # exit logic
        if row_sum_pixel == width:
            i += 1
            row_sum_pixel = 0
            prev = 0

    return decoded_image  # replace zeros with image reconstructed from rle_Code


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 your_script.py input/binary_image.jpg")
        sys.exit(1)

    # go to input folder
    input_file = sys.argv[1]
    if not os.path.isfile(input_file):
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)

    image = cv2.imread(input_file)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # print(image.shape)

    binary_image = force_binary(image)
    rle_code = encode_image(binary_image)
    print(rle_code)
    save_rle_to_file(rle_code, "output/rle.txt")

    output_dir = "output/"
    [h, w] = binary_image.shape
    decode = decode_image("output/rle.txt", h, w)
    output = output_dir + "decode" + ".jpg"
    cv2.imwrite(output, decode)


if __name__ == "__main__":
    main()
