#!/usr/bin/python3
# 4-list_division.py

def list_division(my_list_1, my_list_2, list_length):
    """
    list_division - divides elements in list 1 by element 2 lists

    Args:
    @my_list_1: the first list
    @my_list_2: the seond list
    @list_length: length of elements to be divided
    can be bigger than the length of both lists

    Return:
    new list (length = list_length) with all divisions)
    """
    res_list = []
    for i in range(0, list_length):
        try:
            res = my_list_1[i] / my_list_2[i]
        except TypeError:
            res = 0
            print("wrong type")
        except ZeroDivisionError:
            res = 0
            print("division by 0")
        except IndexError:
            res = 0
            print("out of range")
        finally:
            res_list.append(res)
    return (res_list)
