import requests, os, json, sys
from configparser import ConfigParser

#Путь к директории бота.
directory_path = os.path.dirname(os.path.abspath(__file__))
api_key = os.path.join(directory_path, "api_key.txt")
channels_list = os.path.join(directory_path, "channels_list.json")

#Проверяем наличие вспомогательных файлов.
if not os.path.exists(api_key):
	print("Api_key.txt file does not exist.")
	sys.exit()

#Загрузка ключа
def read_api_key():
	with open(api_key, "r") as f:
		lines = f.readlines()
		return lines[0].strip()

api_key = read_api_key()

#Строчка запроса ютубчика
link = 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId={}&maxResults=1&key={}'

#Проход по списку каналов и проверка на публикацию
def check_channels_list():
	newlist = []
	message = ""

	with open(channels_list, "r") as f:
		data = json.load(f)
		counter = len(data)


	for i in range(counter):

		playlist = data[i]['all_video_playlist']
		get_link = link.format(playlist, api_key)
		req = requests.get(get_link)
		req_data = req.json()
		video_id = req_data['items'][0]['snippet']['resourceId']['videoId']

		if video_id != data[i]['last_video_id']:
			newdata = {
						"channel_name" : data[i]['channel_name'],
						"all_video_playlist" : data[i]['all_video_playlist'],
						"last_video_id" : video_id}
			newlist.append(newdata)

			message = "Новое видео на канале " + data[i]['channel_name'] + ": " + "https://www.youtube.com/watch?v=" + video_id

			return message

		elif video_id == data[i]['last_video_id']:
			newlist.append(data[i])

		else:
			continue

	with open(channels_list, "w") as f:
		json.dump(newlist, f)

print(check_channels_list())