x,y = map(int, input().split())
costa = 0
tabuleiro = []

for i in range(x):
    tabuleiro.append(input())
    
    #print(tabuleiro[-1])
    
for i in range(x):
    for j in range(y):
    
        if tabuleiro[i][j] == "#":
            
            if i+1 == x or j+1 == y or i == 0 or j == 0:
                costa = costa + 1             
                        
            elif tabuleiro[i-1][j] == "." or tabuleiro[i+1][j] == "." or tabuleiro[i][j+1] == "." or tabuleiro[i][j-1] == ".":
            
                costa = costa + 1
                
        
            
print(costa)
