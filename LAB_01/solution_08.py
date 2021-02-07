msg = input("Write your name:")

row = len(msg)

h = ''.join(['+'] + ['-' *row] + ['+'])

result= h + '\n'"|"+msg+"|"'\n' + h

print(result)
