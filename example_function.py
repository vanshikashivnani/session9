def greet():
    print('Hello')


for i in range(10):
    print(f'{i+1} ', end='')
    greet()

x = greet()
print(x)

y = print('Hello World')
print(y)