import random


def setparameters(param):
    dict = {param:random.random()}
    return dict


print(setparameters(param=input("enter a parameter\n")))