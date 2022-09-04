input01 = open("input/input01.txt", "r")

input01_list = input01.read().split()

n = input01_list[0]
input01_list = input01_list[1:]

len_list = len(input01_list)
slice_list = list([input01_list[x], input01_list[x + 1]] for x in range(0, len_list, 2))

example_1 = [b for a, b in slice_list]  # Создаем массив оценок
example_2 = set(example_1)              # Трансформируем в множество, убирая повторы
example_3 = sorted(example_2)           # Сортируем, вернув тип list
example_4 = example_3[1]                # Берем по заданию 2 снизу значение

print("\n".join(sorted(list(name for name, grade in slice_list if grade == example_4))))

