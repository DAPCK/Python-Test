# i = 1
# while i <= 10:
#      print(i)
#      i += 1

# s = 'Hello world'
# for l in s:
#     if l == ' ':
#         continue
#     print(f'"{l}"', end=' ')

x = input("Enter a world: ")
for i in x:
    if i == ' ':
        break
    print(i, end=' ')
else:
    print('\nAll Clear')
