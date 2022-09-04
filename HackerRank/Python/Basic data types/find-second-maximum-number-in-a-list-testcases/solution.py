input00 = open("input/input00.txt", "r")

input00_list = input00.read().split()

n = int(input00_list[0])
arr = map(int, input00_list[1:])

arr_list = list(arr)  # объект map преобразовываем в list
max_arr_el = max(arr_list)
print(max(list(filter(lambda el: el != max_arr_el, arr_list))))  # используем фильтрацию по максимальному элементы

