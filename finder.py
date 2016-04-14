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
    # note: reddit's servers were f'd around the time ccKufi was created, so your username piece may be different
    # from what this method says. In the future there will be a long search option that uses every possible slice of
    # your username.
    chunk_begin = int(username_index / 5295 * len(fullname))
    chunk = fullname[chunk_begin:chunk_begin+chunk_size]

    return chunk


def search_name_chunk(search_term, username_index):
    s = re.compile('(%s)' % search_term)
    with open("roomname.txt", "r") as r:
        # approximate beginning of name chunk in room name
        # multiplied by 2 because every username got 2 letters in ccKufi's name
        center_search = r.read()[username_index * 2]
        # give an extra 2000 characters on each side to be safe (full name is >10000 characters long)
        search_section = r.read()[center_search-2000:center_search+2000]
        # use list comprehension to get a list of tuples where matches were found
        result_list = [m.span() for m in s.finditer(search_section)]
        adjusted_list = []
        # reduce second value of every tuple in result_list by 1
        # however, tuples are immutable so we need to create new ones...
        for i in result_list:
            adjusted_list.append((i[0], i[1]-1))

if __name__ == "__main__":
    main()
