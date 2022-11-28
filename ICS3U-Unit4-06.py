#!/usr/bin/env python3
# Created by: Emmanuel Fofeyin
# Created on: Nov 2022
# This program uses nested loops


def main():
    # This is the nested loop function

    rgb1 = 0
    rgb2 = 0
    rgb3 = 0

    # process,output
    for rgb1 in range(256):
        for rgb2 in range(256):
            for rgb3 in range(256):
                print("RGB({0},{1},{2})".format(rgb1, rgb2, rgb3))

    print("\nDone.")


if __name__ == "__main__":
    main()
