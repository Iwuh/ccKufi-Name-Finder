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
        name_chunk = find_name_chunk(username, member_list.index(username))
    else:
        print("Error: username was not in room")
        input("Press Enter to exit...")
        sys.exit()


def find_name_chunk(fullname, username_index):
    # size of name chunk is: length of name / total people in room (5295), rounded up
    chunk_size = math.ceil(len(fullname) / 5295)
    # minimum chunk size is 2
    if chunk_size < 2:
        chunk_size = 2

    # position where slice begins is: (position of name in user list / total people in room ) * length of username
    # note: reddit's servers were f**d around the time ccKufi was created, so your username piece may be different
    # from what this method says. In the future there will be a long search option that uses every possible slice of
    # your username.
    chunk_begin = math.ceil((username_index / 5295 * len(fullname)))
    chunk = fullname[chunk_begin:chunk_size]

    return chunk

if __name__ == "__main__":
    main()
