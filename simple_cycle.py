def func():
	newlist = []
	message = ""

	id_list = ["1", "2", "3", "4"]
	print(id_list)
	counter = len(id_list)

	for i in range(counter):
		old_id = id_list[i]
		new_id = "new"

		if old_id != new_id:
			newlist.append(new_id)
			message = "Новое видео " + new_id
		return message
		print(newlist)

print(func())