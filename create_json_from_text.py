#чтение текстового файла base.txt и создание на его основе
#json-файла, содержащего массив уникальных слов
#либо из строки, если файл отсутствует

#блок импорта
import re

#создаем списки для работы
raw_list,uni_list=[],[]

def read_from_file(filename):
	#читаем файл, берем слова только из букв и переводим в lower_case
	with filename as raw_text:
		for line in raw_text:
			for word in re.findall(r'[a-zA-Z]+',line):
				raw_list.append(word.lower())
	return raw_list

def read_from_string(string):
	#читаем строку, берем слова только из букв и переводим в lower_case
	for word in re.findall(r'[a-zA-Z]+',string):
		raw_list.append(word.lower())
	return raw_list

def make_uniqe_list(raw_list):
	#создаем новый список, исключая повторяющиеся элементы и сортируем по алфавиту
	for i in raw_list:
		if i not in uni_list:
			uni_list.append(i)
		uni_list.sort()
	return uni_list

def write_to_json(uni_list):
	#блок записи (переписывает существующий list.json)
	new_file=open('list.json','w')
	new_file.write('[\n')
	for i in uni_list:
		new_file.write('\t'+i+','+'\n')
	new_file.write(']')
	new_file.close()

#основной блок
try:
    file = open('base.txt','r')			#проверка существования файла
except IOError as exc:					#работа со строкой, если файл base.txt не существует
    ask=('''This is an example string for case when base file does not exist.
    		This program should make a JSON file using the text you are reading now.
    		I hope i didn't make any mistakes because my English isn't perfect.
    	''')
    read_from_string(ask)
    make_uniqe_list(raw_list)
    write_to_json(uni_list)
else:
    with file:							#работа с файлом, если файл base.txt существует
        read_from_file(file)
        make_uniqe_list(raw_list)
        write_to_json(uni_list)