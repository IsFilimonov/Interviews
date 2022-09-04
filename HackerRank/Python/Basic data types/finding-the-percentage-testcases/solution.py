input00 = open("input/input00.txt", "r")
input01 = open("input/input01.txt", "r")

input00_list = input00.read().splitlines()
input01_list = input01.read().splitlines()

count_elements = int(input00_list[0])

dictionary = {}
for i in range(count_elements):
    str_elements = input00_list[i+1].split()
    dictionary[str_elements[0]] = [str_elements[1], str_elements[2], str_elements[3]]

average = sum(map(int, dictionary[input00_list[count_elements + 1]])) / len(input00_list)

print(average)

#    query_scores = student_marks[query_name]
#    print("{0:.2f}".format(sum(query_scores) / len(query_scores)))
