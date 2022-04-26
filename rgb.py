#!/usr/bin/env python3

# Created by Ethan Prieur
# Created on APRIL 2022
# This is a program that goes through every rgb combination


def main():
    # This is the main program
    counter = 0
    coutner2 = 0
    counter3 = 0

    # Output
    print("")
    for counter in range(256):
        for counter2 in range(256):
            for counter3 in range(256):
                print("{0}, {1}, {2}".format(counter, counter2, counter3))
    print("\nDone.")


if __name__ == "__main__":
    main()
