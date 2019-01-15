 #Bill Lubanovic - Introducing Python chapter 6 tasks.

# Вещание 6. Объекты и классы. Практическая часть.
divider="-------------------------------------------------------------"
print("Вывод результатов упражнений к 6 главе.")
print(divider)
# #Задание 1.
# Создайте класс, который называется Thing, не имеющий содержимого, и
#выведите его на экран. Затем Создайте объект example этого класса и
#также выведите его. Совпадают ли выведенные значения?
class Thing():
	pass
print(Thing)
example = Thing
print(example)
if Thing == example:
	print('Совпадают.')
else:
	print('Не совпадают.')
print(divider)
# Задание 2.
# Создайте новый класс с именем Thing2 и присвойте его методу letters
#значение 'abc'. Выведите на экран значение атрибута letters.
class Thing2():
	def letters():
		print('abc')
	pass
Thing2.letters()
print(divider)
# Задание 3.
# Создайте еще один класс, который, конечно же, называется Thing3. В этот раз
#присвойте значение 'xyz' атрибуту объекта, который называется letters.
# Выведите на экран значение атрибута letters. Понадобилось ли вам создавать
#объект класса, чтобы сделать это?
class Thing3():
	def __init__(self, letters):
		self.letters = letters
		pass
something = Thing3('xyz')
print('Значение атрибута letters:', something.letters)
print(divider)
# Задание 4.
# Создайте класс, который называется Element, имеющий атрибуты объекта name, symbol
#и number. Создайте объект этого класса со значениями 'Hydrogen', 'H' и 1.
class Element():
	def __init__(self, name, symbol, number):
		self.name = name
		self.symbol = symbol
		self.number = number
	pass
element1 = Element('Hydrogen', 'H', '1')
print(element1.name, element1.symbol, element1.number)
print(divider)
# Задание 5.
# Создайте словарь со следующими ключами и значениями: 'name': 'Hydrogen',
#'symbol' : 'H', 'number' : 1. Далее создайте объект с именем hydrogen
#класса Element с помощью этого словаря.
c6_dict = {'name' : 'hydrogen', 'symbol' : 'H', 'number' : '1'}
hydrogen = Element(c6_dict.get('name'), c6_dict.get('symbol'), c6_dict.get('number'))
print(hydrogen.name)
print(hydrogen.symbol)
print(hydrogen.number)
print(divider)
# Задание 6.
# Для класса Element определите метод с именем dump(), который выводит на экран
#значения атрибутов объекта (name, symbol, number). Создайте объект hydrogen из
#этого нового определения и используйте метод dump(), чтобы вывести на экран его атрибуты.
c6_dict = {'name' : 'hydrogen', 'symbol' : 'H', 'number' : '1'}
hydrogen = Element(c6_dict.get('name'), c6_dict.get('symbol'), c6_dict.get('number'))
print(hydrogen.name)
print(hydrogen.symbol)
print(hydrogen.number)
print(divider)
# #Задание 7.
# Вызовите функцию print(hydrogen). В определении класса Element измените имя метода
#dump на __str__, создайте новый объект hydrogen и затем снова вызовите метод print(hydrogen).
class Element():
	def __init__(self, name, symbol, number):
		self.name = name
		self.symbol = symbol
		self.number = number
		pass
	def dump(self):
		print("Dump method:")
		print(self.name, self.symbol, self.number)
		pass
	def __str__(self):
		return str(self.name) + ":" + str(self.symbol) + ":" + str(self.number)
print("Dump method and __str__.");
hydrogen = Element('Hydrogen', 'H', '1')
hydrogen.dump()
print(hydrogen)
helium = Element('Helium', 'He', '2')
print(helium)
print(divider)
# Задание 8.
# Модифицируйте класс Element, сделав атрибуты name, symbol, number закрытыми.
# Определите для каждого атрибута свойство получателя, возвращающее значение
#соответствующего атрибута.
class Element():
	def __init__(self, name, symbol, number):
		self.__name = name
		self.__symbol = symbol
		self.__number = number
		pass
	def name(self):
		return self.__name
	def symbol(self):
		return self.__symbol
	def number(self):
		return self.__number
	pass
objE = Element("Helium", "He", 2)
print("Hidden variables in Element:", objE.name(), objE.symbol(), objE.number())
# Задание 9.
# Определите три класса: Bear, Rabbit, Octothorpe. Для каждого из них определите
#всего один метод - eats(). Он должен возвращать значения 'berries' (для Bear),
#'clover' (для Rabbit) или 'campers' (для Octothorpe). Создайте по одному
#объекту каждого класса и выведите на экран то, что ест указанное животное.
class Bear():
	def eats(self):
		eats = 'berries'
		return eats
class Rabbit():
	def eats(self):
		eats = 'clover'
		return eats
class Octothorpe():
	def eats(self):
		eats = 'campers'
		return eats
bear = Bear()
rabbit = Rabbit()
octothorpe = Octothorpe()
print ('Bear eats', bear.eats())
print ('Rabbit eats', rabbit.eats())
print ('Octothorpe eats', octothorpe.eats())
print(divider)
# Задание 10.
# Определите три класса: Laser, Claw, SmartPhone. Каждый из них имеет только один метод - does().
# Он возвращает значения 'disintegrate' (Laser), 'crush' (Claw), 'ring' (SmartPhone).
# Далее определите класс Robot, который содержит по одному объекту каждого из этих классов.
# Определите метод does() для класса Robot, который выводит на экран все, что делают его компоненты.
class Laser():
	def does(self):
		val = 'disintegrate'
		return val
	pass
class Claw():
	def does(self):
		val = 'crush'
		return val
	pass
class SmartPhone():
	def does(self):
		val = 'ring'
		return val
	pass
class Robot():
	def __init__(self, objL, objC, objS):
		self.laser = objL
		self.claw = objC
		self.smartphone = objS
		pass
	def does(self):
		return self.laser.does(), self.claw.does(), self.smartphone.does()
	pass
cl_l = Laser(); cl_c = Claw(); cl_s = SmartPhone()
robot1 = Robot(cl_l, cl_c, cl_s)
print('Robot does', robot1.does())
