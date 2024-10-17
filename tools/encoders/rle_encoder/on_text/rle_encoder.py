import os
import sys
import threading
from time import time


class ThreadData:
    def __init__(self, input_str):
        self.input_str = input_str
        self.rle_str = ""
        self.rle_freq = []
        self.time_tuple = None
        self.mem_saved = 0


def rle_encode(thread_data):
    start_time = time()
    print(f"Thread for '{thread_data.input_str}' started.")

    input_str = thread_data.input_str
    rle_str = ""
    rle_freq = []

    i = 0
    while i < len(input_str):
        count = 1
        while i + 1 < len(input_str) and input_str[i] == input_str[i + 1]:
            count += 1
            i += 1

        if count > 1:
            rle_str += input_str[i] * 2
            rle_freq.append(count)
            rle_str += "["
            rle_str += str(count)
            rle_str += "]"
        else:
            rle_str += input_str[i]
        i += 1

    thread_data.rle_str = rle_str
    thread_data.rle_freq = rle_freq

    thread_data.mem_saved = len(thread_data.input_str) - len(thread_data.rle_str)
    end_time = time()
    thread_data.time_tuple = (start_time, end_time)
    print(f"Thread for '{thread_data.input_str}' finished.")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 your_script.py input/test.txt")
        sys.exit(1)

    # go to input folder
    input_file = sys.argv[1]
    if not os.path.isfile(input_file):
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)

    # read input strings from input dir/folder
    str_list = []
    with open(input_file, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                str_list.append(line)

    # create thread data objects and threads
    thread_data_list = [ThreadData(input_str) for input_str in str_list]
    threads = []

    # create and start threads
    for data in thread_data_list:
        thread = threading.Thread(target=rle_encode, args=(data,))
        threads.append(thread)
        thread.start()

    # wait for all threads to finish
    for thread in threads:
        thread.join()

    # print metrics
    for data in thread_data_list:
        print(f"Input string: {data.input_str}")
        print(f"RLE String: {data.rle_str}")
        print(f"RLE Frequencies: {' '.join(map(str, data.rle_freq))}")
        print(f"Time (start, finish): {data.time_tuple}")
        print(f"Execution Time: it took: {data.time_tuple[1] - data.time_tuple[0]}s")
        print(f"Memory Saved (in bytes): {data.mem_saved}\n")


if __name__ == "__main__":
    main()
