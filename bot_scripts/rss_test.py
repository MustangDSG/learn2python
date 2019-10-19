import feedparser
import json, os

# Путь к директории бота.
directory_path = os.path.dirname(os.path.abspath(__file__))
rss_list = os.path.join(directory_path, "rss_list.json")

rss_url = 'https://www.tokyotosho.info/rss.php?filter=1&reversepolarity=1'
rss_data = feedparser.parse(rss_url)


def check_series():
    with open(rss_list, "r") as f:
        json_data = json.load(f)

    los = []
    message = ""

    for i in range(len(rss_data['entries'])):
        title = rss_data['entries'][i]['title']
        splited_title = title.split()
        s = " "
        new_title = s.join(splited_title[:-3])
        episode_number = s.join(splited_title[-2:-1])
        temp_data = {"title" : new_title, "last_episode" : episode_number}
        los.append(temp_data)

    unique_los = []
    for i in los:
        if i not in unique_los:
            unique_los.append(i)

    for item in range(len(json_data)):
        for j in range(len(unique_los)):
            if all([
                json_data[item]['title'] == unique_los[j]['title'],
                json_data[item]['last_episode'] != unique_los[j]['last_episode']
                ]):
                new_data = {"title": unique_los[j]['title'], "last_episode": unique_los[j]['last_episode']}
                json_data.pop(item)
                json_data.append(new_data)
                message += unique_los[j]['title'] + " - " + unique_los[j]['last_episode'] + ", "

    with open(rss_list, "w") as f:
        json.dump(json_data, f)

    return message
