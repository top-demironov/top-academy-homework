
# Задание 2.
# Напишите функцию, которая принимает два числа
# в качестве параметра и отображает все нечетные числа
# между ними.
def get_even_numbers_in_range(a : int, b: int):
	even_arr: list[int] = []
	for i in range(a, b+1):
		if i % 2!=0:
			even_arr.append(i)

	return even_arr
a : int = 3
b: int = 10
print(get_even_numbers_in_range(a, b))
