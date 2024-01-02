name = 'John'
age = 30
# print('My name is ' + name + '. I\'m ' + str(age)) - хуйня так как сложно
# print('My name is %(name)s. I\'m %(age)d' %{'name': name, 'age': age}) - можно несколько раз использовать маркеры
# тоже хуйня так как старовато но используемо
# print('My name is %s. I\'m %d' %(name, age)) - прикольнее и коротче
# print('Title: %s, Price: %.2f' %('Sony', 40)) "%.2f" - 2 знака после запятой, без 2 буде куча 0 але старий варіант
# format
# print('My name is {}. I\'m {}'.format(name, age)) (name, age) - аргументы
# print('My name is {0}. I\'m {1}'.format(name, age)) - номер аргумента от 0 до .... {} можно подставлять несколько раз где угодно
# print('My name is {name}. I\'m {age}'.format(name=name, age=age)) {name} и {age} -  переменные которые можно назвать как угодно указывать без пробелов перед и после =

# f-strings
# print(f'My name is {name}. I\'m {age}') f - форматирование строки для использования переменных
# print(f'My name is {name}. I\'m {age + 5}') - добавили к переменной возраст еще + 5 лет
# print('5 + 2 = {}'.format(5 + 2)) - длинно
# print(f'5 + 2 = {5 + 2}') - форматировано сильно проще