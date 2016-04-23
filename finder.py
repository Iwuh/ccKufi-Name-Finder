#!/usr/bin/env python3

import math
import re
import colorama


with open("roommembers.txt", "r") as f:
    # turn roommembers.txt into list of names
    member_list = f.read().split(", ")


def main():
    # prompt for username
    username = input("Enter your username: ")
    try:
        name_chunk = find_name_chunk(username, member_list.index(username))
        search_name_chunk(name_chunk, member_list.index(username))
        print("")
        input("Press Enter to exit...")
    except ValueError:
        print("Error: username was not in room")
        input("Press Enter to exit...")


def find_name_chunk(fullname, username_index):
    # size of name chunk is: length of name / total people in room (5295), rounded up
    chunk_size = math.ceil(len(fullname) / 5295)
    # minimum chunk size is 2
    if chunk_size < 2:
        chunk_size = 2

    # position where slice begins is: (position of name in user list / total people in room ) * length of username
    # note: reddit's servers were f'd around the time ccKufi was created, so your username piece may be different
    # from what this method says. In the future there will be a long search option that uses every possible slice of
    # your username.
    chunk_begin = int(username_index / 5295 * len(fullname))
    # make sure the chunk doesn't get shortened because it goes over the end of the string
    if chunk_begin+chunk_size > len(fullname):
        # spooky string slicing magic
        chunk = fullname[len(fullname)-chunk_size:]
    else:
        chunk = fullname[chunk_begin:chunk_begin+chunk_size]

    return chunk


def search_name_chunk(search_term, username_index):
    s = re.compile('(%s)' % search_term)
    with open("roomname.txt", "r") as r:
        # approximate beginning of name chunk in room name
        # multiplied by 2 because most if not everyone got 2 letters in ccKufi's name and I don't know a better solution
        center_search = username_index * 2
        # give an extra 100 characters on each side to be safe (full name is >10000 characters long)
        if center_search-100 < 0:
            # however, we don't want the start to be lower than 0
            search_start = 0
        else:
            search_start = center_search-100
        search_section = r.read()[search_start:center_search+100]
        # use list comprehension to get a list of tuples where matches were found
        result_list = [m.span() for m in s.finditer(search_section)]
        adjusted_list = []
        # convert list of tuples to list of character indices where matches were found
        for i in result_list:
            adjusted_list.append((i[0])+search_start)
            adjusted_list.append((i[1]-1)+search_start)

        print_results(adjusted_list)


def print_results(results):
    with open("roomname.txt", "r") as n:
        room_name = n.read()
        # iterate over every character in the room name and print in red if it matches an item in results
        for i in range(0, len(room_name)):
            if i in results:
                print(colorama.Fore.RED + room_name[i], end="")
            else:
                print(colorama.Fore.WHITE + room_name[i], end="")

if __name__ == "__main__":
    # must initialise colorama before use and deinitialise after use (only on Windows)
    colorama.init()
    main()
    colorama.deinit()
