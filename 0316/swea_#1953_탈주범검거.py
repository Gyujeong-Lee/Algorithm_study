'''
시뮬레이션 x
시간당 1의 거리 가능
움직이지 않는 경우도 고려해야 한다.
최대 시간 동안 갈 수 있는 모든 위치만 고려하면 된다.
BFS

파이프 모양에 따라 인접의 조건이 달라진다.
타입별로 방향을 표시
pipe = [[], [0, 1, 2, 3], [0, 3], ...]
r = pipe 타입
c = pipe가 가진 방향

타입 1 = 0(우), 1(하), 2(좌), 3(상)
ex) 현재 방향이 1이라면 옮길 파이프는 3을 가지고 있어야 함

고려할 방향이 x라면 옮겨갈 칸의 파이프가 (x+2)%4 방향을 갖고 있어야 한다.

L시간 동안 방문한 모든 칸을 찾는다.

'''