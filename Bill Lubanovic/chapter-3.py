#Bill Lubanovic - Introducing Python chapter 3 tasks.

# Вещание 3. Списки, словари, кортежи и множества, практическая часть.
divider = "\n";
print("Вывод результатов упражнений к 3 главе.")
print(divider)

# Задание 1.
# Создайте список years_list, содержащий год, в который вы родились,
#и каждый последующий год вплоть до вашего пятого дня рождения.
years_list=['1985']
i=1
while i<=5:
	add_year=str(int(years_list[0])+i)
	years_list.append(add_year)
	i+=1
print(years_list)
# Задание 2.
# В какой из годов, содержащихся в списке years_list, был ваш третий день рождения?
third_birthday=years_list[3]
print("Третий день рождения был в", third_birthday, "году.")
# Задание 3.
# В какой из годов, перечисленных в списке years_list, вам было больше всего лет?
max_age=years_list[-1]
print("Из списка годов больше всего лет мне было в", max_age, "году.")
print(divider)
# Задание 4.
# Создайте список things, содержащий три элемента: "mozzarela", "cinderella", "salmonella".
things=['mozzarela', 'cinderella', 'salmonella']
# Задание 5.
# Напишите с большой буквы тот элемент списка things, который относится к человеку, а затем выведете список.
things[1].capitalize()
print('Изменится ли значение, при таком варианте?\n', things, '\nКак видим - не изменилось.')
things[1]=things[1].capitalize()
print('Оно изменится в списке в том случае, если мы сделаем присваивание нового значения элементу списка:\n', things)
# Задание 6.
# Переведите сырный элемент списка things в верхний регистр целиком и выведете список.
things[0]=things[0].upper()
print("Сыр теперь капсом", things)
# Задание 7.
# Удалите болезнь из списка things, получите Нобелевскую премию и затем выведите список на экран.
things.pop()
win_Nobel_prize=True
print("Болезни больше нет: ", things)
if win_Nobel_prize:
	print("И за это мы получили Нобелевскую премию!")
print(divider)
# Задание 8.
# Создайте список, который называется surprise и содержит элементы 'Groucho', 'Chico', 'Harpo'.
surprise=['Groucho', 'Chico', 'Harpo']
# Задание 9.
# Напишите последний элемент списка surprise со строчной буквы, затем обратите его и напишите с прописной буквы.
name_from_surprise_list=surprise[-1].lower()
print("Последний элемент строчными буквами:", name_from_surprise_list)
inverted_name=name_from_surprise_list[::-1].capitalize()
print("Обратили имя и написали с заглавной буквы:", inverted_name)
print(divider)
# Задание 10.
# Создайте англо-французский словарь, который называется e2f, и выведите его на экран.
e2f={"dog" : "chien", "cat" : "chat", "walrus" : "morse"}
# Задание 11.
# Используя словарь e2f, выведите французский вариант слова walrus.
print("Французский вариант слова walrus:", e2f.get("walrus"))
# Задание 12.
# Создайте французско-анлийский словарь f2e на основе словаря e2f. Используйте метод items.
f2e = { v:k for k,v in e2f.items() }
# Альтернативное решение одной строкой без for-a.
f2e_alt = dict(zip(list(e2f.values()), list(e2f.keys())))
print("Французско-анлийский словарь:", f2e)
print("Альтернативный французско-анлийский словарь:", f2e_alt)
# Задание 13.
# Используя словарь f2e, выведите английский вариант слова chien.
print("Английский вариант слова chien:", f2e.get("chien"))
# Задание 14.
# Создайте и выведите на экран множество английских слов из ключей словаря e2f.
print("Множество из словаря e2f:", set(e2f))
print(divider)
# Задание 15.
# Создайте многоуровневый словарь life. Используйте следующие строки для
#ключей верхнего уровня: 'animals', 'plants' и 'other'.
# Сделайте так, чтобы ключ 'animals' ссылался на другой словарь, имеющий
#ключи 'cats', 'octopi' и 'emus'. Сделайте так, чтобы ключ 'cats'
#ссылался на список строк со значениями 'Henri', 'Grumpy' и 'Lucy'.
# Остальные ключи должны ссылаться на пустые словари.
cats_list=['Henri', 'Grumpy', 'Lucy']

animals_dict={
	"cats" : cats_list,
	"octopi" : "",
	"emus" : "",
}

life={
	"animals" : animals_dict,
	"plants" : "",
	"other" : "",
}

# Задание 16.
# Выведите на экран высокоуровневые ключи словаря life.
print("Высокоуровневые ключи словаря life:", life.keys())
# Задание 17.
# Выведите на экран ключи life['animals']
print("Ключи словаря life['animals']:", life['animals'].keys())
# Задание 18.
# Выведите значения life['animals']['cats']
print("Ключи словаря life['animals']['cats']:", life['animals']['cats'])
print(divider)
dict7 = { "colors" : {"red" : 0, "green" : 1}, "shapes" : ["square", "circle"] }
print("Complex data:", dict7, dict7.keys(), dict7['colors'].keys(), dict7['colors'].values(), dict7['shapes'])
