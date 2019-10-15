import feedparser

#берем список по категории
rss_url = 'https://www.tokyotosho.info/rss.php?filter=1&reversepolarity=1'
#превращаем в удобный для путона вид
rss_data = feedparser.parse(rss_url)

#список подстрок, которые должны быть в названии, обязательно все
check = ['[HorribleSubs]', 'Black Clover']

#цикл обработки, 150 - количество записей, которое выдает сайт в своем rss
for i in range(150):
	#берем только названия
	title = rss_data['entries'][i]['title']
	#разбираем строку на отдельные куски
	splited_title = title.split( )
	#задаем разделитель для сборки
	s = " "
	#собираем строчку заново, отрезая лишнее
	new_title = s.join(splited_title[:-1])
	#выдираем номер серии
	episode_number = splited_title[-2:-1]

	if check in new_title:     #вот тут надо сделать проверку, что ВСЕ элементы списка есть в переменной new_title
		print(new_title)
