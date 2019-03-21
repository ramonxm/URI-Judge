N = int(input())
conta = int

if N <= 10:
	conta = 7
elif N >= 11 and N <= 30:
	conta = N - 10 * 1 + 7
elif N >= 31 and N <= 100: 
	conta = (N - 30) * 2 + 27
else:
	conta = (N - 100) * 5 + 167
	
print(conta)
