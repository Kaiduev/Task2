text = input()
# i = 0
# tab = '\t'
# size = len(text)
# while i < size:
#     print((tab*i)+text[i])
#     i = i + 1

for i,x in enumerate (text.split()):
    print(' '*i+x )