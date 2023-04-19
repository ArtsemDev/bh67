# # numbers = [2, 3, 2, 4, 5, 3, 4, 2, 7, 5, 6]
# # print(numbers[1])
# # numbers[1] = 4
# # print(numbers[1])

# # objs = list('hello world')
# # print(objs)

# # objs = ['hello', 40, 5, 4, 4, 'world', True]
# # del objs[1:3]
# # print(objs)
# # obj = objs.pop(1)
# # print(objs)
# # print(obj)
# # objs.remove(44)
# # print(objs)
# # objs.append(1)
# # objs.extend([1, 2, 3, 4])
# # result = objs + [1, 2, 3, 4]
# # print(objs * -8)
# # print(result)
# # numbers = [1, 2, 3, 4, 5, 6]
# # numbers.append(7)
# # numbers.insert(0, 0)
# # numbers.insert(2, 'hello')
# # print(numbers)

# # numbers = [3, 5, 4, 6, 2, 3, 4, 7, 8]
# # result = sorted(numbers)
# # print(result)
# # print(numbers)
# # numbers.sort(reverse=True)
# # print(numbers)

# # words = ['Hello', 'age', 'bread', 'Apple', 'world']
# # words.sort(key=len)
# # print(words)

# # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # result = numbers[::-1]
# # print(numbers)
# # print(result)

# # numbers = [1, 2, 3]
# # result = list(numbers)
# # # numbers.append(4)
# # # print(result)
# # print(numbers[1] is result[1])

# # e = 3
# # a = [1, 2, 'hello']
# # b = [3, 4, 5]
# # b.append(a)
# # b[3][2] = 3
# # print(a)

# # numbers = [0 for i in range(100)]
# # print(numbers)
# # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # numbers = [numbers[i]*5 for i in range(len(numbers))]
# # print(numbers)
# # text = 'hello'
# # letters = list(text)
# # letters[1] = 'p'
# # print(letters)

# # numbers = [1, 2, 3, 4]
# # numbers[1:3] = [1, 2, 3, 4]
# # print(numbers)
# # a, b, *c = numbers
# # print(a)
# # print(b)
# # print(c)

# # a = [1, 2, 3]
# # b = [4, 5, 6, 7, 8, 9]
# # text = 'hello'
# # c = [*a, *b, *text]
# # d = a + b
# # print(c)


# # a = (4, )
# # print(a)

# # a = (1, 2, 3, 4, [5, 6, 7])
# # a[4].append(8)
# # print(a)


# # user = {
# # 	'name': 'Vasya',
# # 	'age': 23,
# # 	'languages': ['ru', 'en']
# # }
# # print(user['name'])
# # user['name'] = 'Petya'
# # user['city'] = 'Minsk'
# # print('Petya' in user)
# # user = dict([('name', 'Vasya'), ('age', 23)])
# # print(user)

# # data = dict(['ab', 'cd'])
# # print(data)

# # data = {i: i**2 for i in range(10)}
# # print(data)

# # data = dict.fromkeys(('name', 'age', 'city'), None)
# # print(data)
# # user = {
# # 	'name': 'Vasya',
# # 	'age': 23,
# # 	'languages': ['ru', 'en'],
# # }
# # print(user['city'])
# # print(user.get('city', 'Minsk'))
# # print(user)
# # print(user.setdefault('city', 'Minsk'))
# # print(user)
# # del user['name']
# # print(user)
# # print(user.pop('name', None))
# # print(user)
# # print(user.popitem())
# # print(user)
# # print({}.popitem())

# # print([*user.keys()])
# # print(list(user))


# user = {
# 	'name': 'Vasya',
# 	'age': 23,
# 	'languages': ['ru', 'en'],
# }
# new_data = {
# 	'age': 35,
# 	'city': 'Minsk'
# }
# # user.update(new_data)
# # print(user)
# # result = {**user, **new_data}
# # print(result)
# # print(user)
# # print(new_data)
# # result = user | new_data
# # print(result)
# # print(type({1, 2, 3}))

# # s1 = set('hello world')
# # print(s1)

# # numbers = {4, 3, 6, 5, 447, 8, 3, 6, 55, 1569}
# # print(numbers)

# # s1 = {1, 2, 3, 4, 5, 6}
# # s2 = {2, 3, 5}
# # print(s1.isdisjoint(s2))
# # print(s2.issubset(s1))
# # print(s2 <= s1)
# # print(s1.issuperset(s2))
# # print(s1 >= s2)
# # print(s1 == s2)
# # s1.add('hello')
# # print(s1)

# # s1 = {1, 2, 3, 4, 5, 6}
# # s2 = {2, 3, 5, 7, 8, 9}
# # print(s1 ^ s2)
# # print(s2 & s1)
# # s3 = s1.union(s2)
# # s4 = s1 | s2
# # print(s3)
# # print(s4)

# from collections import *

# # words = ['hello', 'python', 'world', 'hello', 'hello', 'python']
# # c = Counter(words)
# # print(c)

# # text1 = 'helloooolllo'
# # text2 = 'world'
# # c1 = Counter(text1)
# # c2 = Counter(text2)
# # print([*c1.elements()])
# # print(c1.most_common(3))
# # print(c1)
# # print(c2)
# # print(c1 - c2)
# # c1.subtract(c2)
# # print(c1)
# # q = deque([1, 2, 3, 4, 5])
# # q.rotate(-2)
# # print(q)

# # data = defaultdict(list)
# # data['languages'].append('ru')
# # print(data)


# # fields = ('name', 'age', 'city')
# # User = namedtuple('User', fields)
# # vasya = User('vasya', 23, 'minsk')
# # petya = User('petya', 15, 'mogilev')
# # print(vasya.city)
# # print(petya)
# # print(vasya._asdict())


# # data = {
# # 	1: 'A',
# # 	1.0: 'B',
# # 	True: 'C'
# # }
# # print(data)
# # data = {
# # 	1: {
# # 		'name': 'vasya'
# # 	}
# # }
# # print(data[1]['name'][1])


# # data = {
# # 	None: 3456,
# # 	(1, 2, (3, 4, (5, 6))): 'tuple'
# # }
# # print(data[(1, 2, (3, 4, (5, 6)))])


# # print('a'
# # 	  'b')
# # text = 'ab'
# # text = f'{45678}' \
# # 	   f'{45678}'
# # print(text)
# # text = f'{45678}{45678}'

# # a = b = 35

# # a = 35
# # b = 35

# # a, b = 35, 35
# # print(a)
# # print(b)


# # tup = 'hello',
# # print(tup)
# numbers = [1, 4, 6]
# data = {
# 	'name': 'vasya', 'age': 23
# }
# print(1, 2, 3, sep='----')

# print(5 > 0)

data = {
	'name': 'Vasya', 
	'age': 23, 
	'city': 'Minsk', 
	'languages': [
		'ru', 
		'en'
	]
}
