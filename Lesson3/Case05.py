def mask(money) :
    x = money // 5  # //整除
    size = "成人"
    return  x, size

my_x, my_size = mask(1366)
print(my_x, my_size)