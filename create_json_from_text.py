#чтение текстового файла base.txt и создание на его основе
#json-файла, содержащего массив уникальных слов

#блок импорта
import re

#создаем списки для работы
raw_list=[]
uni_list=[]

#читаем файл, ,берем слова только из букв и переводим в lower_case
with open('base.txt', 'r') as raw_text:
	for line in raw_text:
		for word in re.findall(r'[a-zA-Z]+', line):
			raw_list.append(word.lower())

#создаем новый список, исключая повторяющиеся элементы и сортируем по алфавиту
for i in raw_list:
	if i not in uni_list:
		uni_list.append(i)
	uni_list.sort()

#блок записи (переписывает существующий list.json)
new_file=open('list.json', 'w')
new_file.write('[\n')
for i in uni_list:
	new_file.write('\t'+i+','+'\n')
new_file.write(']')
new_file.close()
