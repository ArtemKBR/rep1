import json
with open('spisok.json', 'w') as f:
	bd = {}
	json.dump(bd, f)
def register(login):
	with open('spisok.json', 'r') as f:
		bd = {}
		bd = json.load(f)
	with open('spisok.json', 'w') as f:
		if login not in bd.keys():
			passwd = input('Придумайте и введите Ваш пароль ')
			bd[login] = passwd
			print('Регистрация прошла успешно')
		else:
			print('Пользователь с таким именем уже зарегистрирован')
		json.dump(bd, f)
while True:
	login = input('Для регистрации введите Ваш логин ')
	register(login)