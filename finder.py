import math
import re
import sys


with open("roommembers.txt", "r") as f:
    # turn roommembers.txt into list of names
    member_list = f.read().split(", ")


def main():
    # prompt for username
    username = input("Enter your username: ")
    if username in member_list:
        pass
    else:
        print("Error: username was not in room")
        input("Press Enter to exit...")
        sys.exit()


def find_name_slice(fullname):
    # size of name chunk is: length of name / total people in room (5295)
    chunk_size = math.ceil(len(fullname) / 5295)
    if chunk_size < 2:
        chunk_size = 2

if __name__ == "__main__":
    main()
