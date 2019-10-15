import feedparser

rss_url = 'https://www.tokyotosho.info/rss.php?filter=1&reversepolarity=1'
rss_data = feedparser.parse(rss_url)

check = ['[HorribleSubs]', 'Black Clover']

for i in range(150):
	title = rss_data['entries'][i]['title']
	splited_title = title.split( )
	s = " "
	new_title = s.join(splited_title[:-1])
	episode_number = splited_title[-2:-1]

	if check in new_title:     #вот тут надо сделать проверку, что все элементы списка есть в переменной new_title
		print(new_title)