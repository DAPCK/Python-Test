print('Таблица умножения')

for i in range(2, 10):
    for k in range(2, 10):
        print(f'{k} * {i} = {i * k}\t', end='')
    print('')
else:
    print('Well done')