#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_list = [str(n).replace(str(search), str(replace)) for n in my_list]
    return my_list
