n = int(input("Введите количество элементов первого множества: "))
m = int(input("Введите количество элементов второго множества: "))


set1 = set()
set2 = set()
7
print("Введите элементы первого множества:")
for i in range(n):
    element = int(input())
    set1.add(element)
print("Введите элементы второго множества:")
for i in range(m):
    element = int(input())
    set2.add(element)
common_elements = set1.intersection(set2)
result_list = sorted(list(common_elements))
print("Общие элементы в обоих множествах (в порядке возрастания):")
print(result_list)