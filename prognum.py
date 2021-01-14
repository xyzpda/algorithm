def fibonum(num):
    if num == 1:
        return 1
    elif num == 2:
        return 1
    else:
        return fibonum(num - 1) + fibonum(num - 2)
    

