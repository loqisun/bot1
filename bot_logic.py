import random


def generate_password(password_lenth):

    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(len(password_lenth)):
        password += random.choice(elements)

    return password



