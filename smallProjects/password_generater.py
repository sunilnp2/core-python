from ast import While
import random
from re import A
from symtable import Symbol
from venv import create

def create_pass():
    lower_case = "anfdajktetoeafldaiuqpwqlajelapipwlelfnviwuiehoiqlasfnbfkjqdv"
    upper_case = "FQJETUOEDMANGKJEHIUTWEOIPQOWETUOIWEMVSNABCZNFWAFIUWEHREHT"
    number = '0987654321'
    symbol = '@#$%&*/?'

    gen_pass = lower_case + upper_case + number + symbol

    # password = "".join(random.sample(gen_pass, 8))
    # print(password)

    mypassword = random.sample(gen_pass, 8)
    a = ""
    b = a.join(mypassword)
    return print(b)
import time
# for i in range(1, 10):
#     create_pass()
#     time.sleep(2)
# i = 0
# while i < 1:
#     create_pass()
#     time.sleep(2)

def show_pass():
    create_pass()
    a = input("Enter a for another password:\n")
    # white i < 1
    if a == a:
        create_pass()
    else:
        print("Thanku for get change to serve you")

show_pass()

