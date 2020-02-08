def add_symbol_to_str(textToAdd, a):
    index = a.find('test')
    outputLine = a[:index] + 'TEST' + a[index:]
    print(outputLine)

a = int(input())
add_symbol_to_str(a)