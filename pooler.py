unpooled = ["1","2","3","4","5","6","7","8"]
count = len(unpooled)

num = 3
k = 0
temp_list = []

div = count // num
mod = count % num
print(div, mod)

if mod == 0:
	step = div
else:
	step = div+1

#создание списков
for i in range(0, step):
	for j in range(k, k + step):
		temp_list.append(unpooled[j])
	print(temp_list)
	temp_list.clear()


# на потом
if mod >= div:
	for i in range(div+1):
		pool_dict = {i : "temp_list"}
		i += 1
		print(pool_dict)


