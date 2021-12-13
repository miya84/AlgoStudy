'''
연구소
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	512 MB	49363	28575	15451	55.039%
문제
인체에 치명적인 바이러스를 연구하던 연구소에서 바이러스가 유출되었다. 다행히 바이러스는 아직 퍼지지 않았고, 바이러스의 확산을 막기 위해서 연구소에 벽을 세우려고 한다.

연구소는 크기가 N×M인 직사각형으로 나타낼 수 있으며, 직사각형은 1×1 크기의 정사각형으로 나누어져 있다. 연구소는 빈 칸, 벽으로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다. 

일부 칸은 바이러스가 존재하며, 이 바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 있다. 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.

예를 들어, 아래와 같이 연구소가 생긴 경우를 살펴보자.
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
27

8 8
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0

3
'''

N, M = map(int, input().split())
virus_map = []
office_map = []
# wall_map = []

for i in range(N):
    row = list(map(int, input().split()))
    office_map.append(row)
    for j in range(M):
        if row[j] == 2:
            virus_map.append([i,j])
        # if row[j] == 1:
        #     wall_map.append([i,j])


def move_wall(office_map, wall_map=[]):
    first, second, end = wall_map
    #if end cant move
    new_end = []
    for i in range(end[0]+1, N):
        for j in range(end[1]+1, M):
            if office_map[i][j] == 0:
                new_end = [i, j]
                break
    
    if new_end == end:
        #if second cant move
        new_second = []
        for i in range(second[0]+1, N):
            for j in range(second[1]+1, M):
                if office_map[i][j] == 0:
                    new_second = [i, j]
                    break
    #if first cant move

moves = [[0,1], [1,0], [0,-1], [-1,0]]
def spread_virus(office_map, N, M):
    def helper(office_map, i, j):
        for r, c in moves:
            if 0<=i+r<N and 0<=j+c<M:
                if office_map[i+r][j+c] == 0:
                    office_map[i+r][j+c] = 2
                    helper(office_map, i+r, j+c)
            else:
                return

    for i, j in virus_map:
        helper(office_map, i, j)
    return office_map


def check_empty_space(office_map):
    pass

# print(*spread_virus(office_map, N, M), sep='\n')
wall_map = []

# while move_wall(office_map, wall_map):
    