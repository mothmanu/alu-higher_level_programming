#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    num = 0
    for i in range(list_length):
        try:
            num = my_list_1[i] / my_list_2[i]
            new_list.append(num)
        except ValueError:
            print("wrong type")
            pass
        except ZeroValueError:
            print("division by 0")
            pass
        except IndexError:
            print("out of range")
            pass
        finally:
            break
     return new_list
