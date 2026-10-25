#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = list(map(lambda x, y, z : z[z.index(x)] = y, search, replace, my_list))
    return new_list
