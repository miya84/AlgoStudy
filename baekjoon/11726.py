
tiles = [0] * 1001
tiles[1] = 1
tiles[2] = 2


n = int(input())


for i in range(3, n+1):
        tiles[i]= tiles[i-1] + tiles[i-2]
        
print(tiles[n]%10007)