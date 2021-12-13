
'''
P(1)부터 P(10)까지 첫 10개 숫자는 1, 1, 1, 2, 2, 3, 4, 5, 7, 9
'''

triangle = [0] * 100

for i in range(0,100):
    if i <3:
        triangle[i] = 1
    else:
        triangle[i] = triangle[i-2]+triangle[i-3]
        
tc = int(input())
for j in range(tc):
    t = int(input())
    print(triangle[t-1])