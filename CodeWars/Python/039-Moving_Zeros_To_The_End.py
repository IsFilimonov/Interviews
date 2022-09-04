def move_zeros(array):
    return list(filter(lambda el: el != 0, array)) + [0] * array.count(0)
