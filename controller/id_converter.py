def NCTU(number):
    if (number[0] == "0"):
        number = "1" + number[0:2]
    elif (number[0] == "3" or number[0] == "5"):
        number = "1" + number[1:3]
    else:
        number = number[0:2]
    return number


def NCU(number):
    if (number[0] == "1"):
        number = number[0:3]
    else:
        number = number[0:2]
    return number


def NTHU(number):
    if (number[0] == "1"):
        number = number[0:3]
    else:
        number = number[0:2]
    return number


def NYMU(number):
    number = number[1:3]
    if (number[0] == "0"):
        number = "1" + number
    return number
