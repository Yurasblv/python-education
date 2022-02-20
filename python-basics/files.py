with open('test.txt', 'w') as f:
    f.write('Hello world\n')
    f.write('And you\n')

with open('test.txt', 'a') as f:
    f.write("What\'s up?")

with open('test.txt', 'r') as f:
    print(f.read())