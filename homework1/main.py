
# Задание 3
# Пользователь с клавиатуры вводит названия файлов,
# до тех пор, пока он не введет слово quit. После завершения
# ввода программа должна объединить содержимое всех
# перечисленных пользователем файлов в один.

filenames: list[str] = input('Введите файлы: ').split(' ')

text = ''

for filename in filenames:
	with open(filename, encoding='utf-8') as f:
		text += f.read()

with open('output.txt', 'w', encoding='utf-8') as f:
	f.write(text)

