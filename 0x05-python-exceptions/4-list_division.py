#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """divides element by element 2 lists"""
    new_list = []
    try:
        for elem in range(list_length):
            try:
                val1 = my_list_1[elem]
                val2 = my_list_2[elem]

                if not (isinstance(val1, (int, float))
                        and isinstance(val2, (int, float))):
                    print("wrong type")
                    new_list.append(0)
                elif val2 == 0:
                    print("division by 0")
                    new_list.append(0)
                else:
                    new_list.append(val1 / val2)
            except IndexError:
                print("out of range")
                new_list.append(0)
    finally:
        return new_list
