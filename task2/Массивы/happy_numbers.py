N = input()
print('unlucky' if not len(N) % 2 and (sum(map(int, N[:int(len(N)/2)]))) == (sum(map(int, N[int(len(N)/2):]))) else 'lucky')