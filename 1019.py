N = int(input())

H = N // 3600;
N = N - (H*3600)
M = N // 60;
S = N - (M * 60);


print("{}{}{}{}{}".format(H,':',M,':',S))

