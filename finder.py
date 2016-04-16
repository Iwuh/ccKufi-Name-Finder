import math
import re
import colorama


with open("roommembers.txt", "r") as f:
    # turn roommembers.txt into list of names
    member_list = f.read().split(", ")


def main():
    # prompt for username
    username = input("Enter your username: ")
    # TODO Find out why it says my name isn't in the list
    try:
        name_chunk = find_name_chunk(username, member_list.index(username))
        character_list = search_name_chunk(name_chunk, member_list.index(username))
        print_results(character_list)
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
    chunk = fullname[chunk_begin:chunk_begin+chunk_size]

    return chunk


def search_name_chunk(search_term, username_index):
    s = re.compile('(%s)' % search_term)
    with open("roomname.txt", "r") as r:
        # approximate beginning of name chunk in room name
        # multiplied by 2 because most if not everyone got 2 letters in ccKufi's name and I don't know a better solution
        center_search = int(r.read()[username_index * 2])
        # give an extra 2000 characters on each side to be safe (full name is >10000 characters long)
        if center_search-2000 < 0:
            # however, we don't want the start to be lower than 0
            search_section = r.read()[0:center_search + 2000]
        else:
            search_section = r.read()[center_search - 2000:center_search + 2000]
        # use list comprehension to get a list of tuples where matches were found
        result_list = [m.span() for m in s.finditer(search_section)]
        adjusted_list = []
        # convert list of tuples to list of character indices where matches were found
        for i in result_list:
            adjusted_list.append(i[0])
            adjusted_list.append(i[1]-1)

        return adjusted_list


def print_results(results):
    with open("roomname.txt", "r") as n:
        for i in n.read():
            if i in results:
                print(colorama.Fore.RED + i)
            else:
                print(colorama.Fore.WHITE + i)

if __name__ == "__main__":
    # must initialise colorama before use and deinitialise after use (only on Windows)
    colorama.init()
    main()
    colorama.deinit()
