# 스택1

> 자료 구조

## 1) stack

- 특성

  - 물건을 쌓아 올리듯 자료를 쌓아 올린 형태의 자료구조이다.

  - 선형구조 : 자료 간의 관계가 1대1의 관계를 갖는다.

  - 비선형구조 : 1대 n ex) tree

  - 자료 삽입과 추출이 가능함

  - LIFO(후입선출) : 마지막에 삽입한 자료를 가장 먼저 꺼낸다.

    ex) 뒤로 가기 기능

    | SWEA  |
    | :---: |
    | KAKAO |
    | NAVER |

     현재 swea에 있다면 kakao, naver 순으로 찾아감. 

    ex) ctl + z

- 자료구조 : 자료를 선형으로 저장할 저장소

  - 배열 / 리스트
  - 저장소 자체를 스택이라 부르기도 한다
  - 마지막 삽입된 원소의 위치를 top이라 부른다.

- 연산

  - 삽입 : 저장소에 자료를 저장한다. `push`
  - 삭제 : 저장소에서 자료를 꺼낸다. (LIFO) `pop` 자료를 꺼내 값을 반환(자료 구조 내 자료가 삭제됨)
  - 공백인지 아닌지 확인 `isEmpty` : 
  - 스택의 top에 있는 item을 반환하는 연산 `peek` : 자료를 꺼내는 것이 아닌 값만 반환함

  ```python
  top = -1 (스택의 밖, 공백스택)
  a push
  -> a 저장
  -> top += 1
  ```

- 스택의 구현

  - push : `append` 함수

    ```python
    def push(item):
        #가득찼는지 검사
        #top 변수를 사용
    	s.append(item)
    ```

    but, 스택(배열)은 크기가 정해져있기 때문에 스택의 자리가 남았는 지 먼저 검사해야 한다. // 리스트는 크기가 가변적이기 때문에 가능함.

  - pop

    무조건 공백 검사가 선행되어야 함

    ```python
    def pop():
    	if len(s) == 0:
            #underflow
            return
        else:
            return s.pop(-1);
    ```

  - 3개의 데이터를 스택에 저장하기

    - 리스트 사용

      파이썬식 처리

    - 리스트의 길이를 미리 결정해놓기

      top을 설정하면서, push할 때 검사 또한 진행

    

- 고려사항

  - 1차원 배열은 구현이 용이하지만, 스택의 크기를 변경하기 어렵다



- 스택의 응용

  - 괄호 종류 : 대괄호[], 중괄호{}, 소괄호()

  1) 왼쪽 괄호의 개수와 오른쪽 괄호의 개수가 같아야함

  2) 왼쪽 괄호가 먼저 나와야 함

  3) 괄호 사이에는 포함 관계만 존재한다.

  - 스택을 이용한 괄호 검사
    - 왼쪽 괄호를 만나면, 스택에 갑입, 오른쪽 괄호를 만나면 top 괄호를 삭제한 후, 오른쪽 괄호와 짝이 맞는지 검사한다.
    - 스택이 비어있으면 조건 1 또는 조건 2에 위배가 된다. 또한 괄호의 짝이 맞지 않으면 조건 3에 위배된다.
    - 마지막 괄호를 조사한 후 스택에 괄호가 남아있으면 조건 1에 위배
  - Function call
    - 프로그램에서의 함수 호출과 복귀에 따른 수행 순서를 관리
    - 함수 선언과 실행은 스택 구조를 따른다.

  

## 2) 재귀호출

> 자기 자신을 호출하여 순환 수행되는 것
>
> 프로그램의 크기를 줄이고 간단하게 작성 가능함

- base 

  : if (종료조건)

- 순환구조()

- 재귀호출의 예 : factorial

  ```python
  n! = n * (n-1)!
  ...
  2! = 2 * 1! 
  1! = 1
  ```

  - 마지막에 구한 하위 값을 반복하여 상위 값을 구함

  ``` =
  fact(4) 
  	return 4 * fact(3)
  fact(3) 
  	return 3 * fact(2)
  fact(2) 
  	return 2 * fact(1)
  fact(1)
  	return 1
  ```

- 재귀 호출의 예 : 피보나치 수열

  - 0과 1로 시작하고 두 수의 합을 다음 항으로 하는 수열을 피보나치라 한다.

    ```python
    F0 = 0, F1 = 1
    Fi = F(i-1) + F(i-2) for >= 2
    
    def fibo(n):
        if n < 2:#종료조건
            return n
        
        return fibo(n-1) + fibo(n-2)
    ```

    

## 3) Memoization

> 피보나치 수열의 경우 재귀함수로 구현하면 엄청난 중복 호출이 존재한다.
>
> 그 문제점을 해결하기 위한 기법 : Memoization

- 피보나치 수열의 Call Tree(교재 확인)

- 기록을 해놓자! Memorization

  동적 계획법의 핵심 

  이전에 계산한 값을 메모리에 저장해서 매번 다시 계산하지 않도록 하여 전체적인 실행 속도를 빠르게 하는 기술이다.

- 피보나치에서 fibo(n)의 값을 계싼하자 저장하면, 실행시간을 O(n)으로 줄일 수 있다.

- 적용

  ```python
  memo를 위한 배열 할당, 0으로 초기화
  memo[0]은 0 memo[1] = 1로 초기화 n<2 조건
  memo = [0, 1]
  def fibo(n):
      global memo#선택
      if n >= 2 and len(memo) <= n:
          memo.append(fino(n-1) + fibo(n-2))
      return memo[n]
  ```

  

## 4) DP(동적 계획법 : Dynamic Programming) - Bottom_up

> 그리디 알고리즘과 같이 최적화 문제를 해결하는 알고리즘이다.
>
> 입력 크기가 작은 부분 문제들을 모두 해결한 후 보다 큰 크기 부분 문제를 해결하고 최종적으로 원래 주어진 입력의 문제를 해결하는 알고리즘이다.

- 피보나치 수 DP 적용

  - 부분문제로 분할하자

    Fibo(n) = fibo(n-1) + fibo(n-2)n

    ```python
    def fibo():
        f = [0, 1]
        for i in range(2, n+1):
            f.append(f[i-1] + f[i-2])
    	return f(n)
    ```

- DP의 구현방식

  - recursive
  - iterative(반복문 방식)

- memoization은 재귀적 구조보다 반복적 구조로 DP를 구현한 것이 성능면에서 보다 효율적이다.

- 재귀적 구조는 내부에 시스템 호출 스택을 사용하는 오버헤드가 발생하기 때문이다.





## 5) \******DFS(깊이 우선 탐색)

> 비선형구조인 그래프 구조는 그래프로 표현된 모든 자료를 빠짐없이 검색하는 것이 중요함.

- 그래프란 무엇인가?

  - G는 v와 e의 쌍이다.

  - 정점과 간선(edge : v1-v2를 이어주는 선)의 모음
  - V는 정점의 집합 : 독립된 개체, 동그라미로 표현 
  -  E는 간선의 집합 : 두 정점을 잇는 개체(관계를 표현), 선 혹은 화살표로 표현
  - 화살표 : 방향 그래프에서 씀

- 인접이란,

  간선이 없다면, 관계가 없다.

  - 간선(u, v) : 시작정점 - u / 종료정점 v, 
  - 간선이 있다면 u와 v가 인접하다.

- 무방향 그래프 : 선으로 표시, 인접관계가 동일 (친구관계)

- 방향 그래프 : 화살표로 표시, 인접관계가 다름 (짝사랑 관계)

- 그래프의 표현

  - 인접행렬(가장 쉬움) : 인접 관계를 표현하는 행렬(2차원 리스트)

    - 정점 크기의 행렬을 만듬 : V*V 0으로 초기화

    - 두 정점 i, j를 잇는 간선이 있다면, 행렬 (i, j)는 1, 아니면 0

    - 무방향 그래프

      양 방향으로 간선이 존재한다는 의미

      대각선 기준으로 대칭되는 형태로 나타남

    - 방향 그래프

      시작 = 행

      종료 = 열

  - 인접리스트

- 목적 

  순서가 없는 데이터(비선형)에 대한 접근을 위해 그래프를 만들어 사용



- 문제 유형

  시작점을 주고 그곳에서 출발하여 갈 수 있는 곳이 최대 어디인지 찾아라

  

- 두 가지 방법

  - DPS(깊이우선탐색) : stack
  - BPS(너비우선탐색) : Q 

- 정의

  시작 정점의 한 방향으로 갈 수 있는 경로가 있는 곳까지 깊이 탐색하다 더이상 갈 곳이 없게 되면, 가장 마지막에 만났던 갈림길 간선이 있는 정점으로 되돌아와서 다른 방향의 정점으로 탐색을 계속 반복하여 결국 모든 정점을 방문하는 순회 방법

- 알고리즘 (교재볼 것)

  - 시작정점 v를 결정하여 방문
  - 정점 v에 인접한 정접 중 
    - 방문하지 않은 정점 w가 있으면, v를 스택에 push하고 정점 w를 방문한다.
    - w를 v로 재설정하고 위 과정을 반복한다.
    - 방문하지 않은 정점이 없으면, 탐색의 방향을 바꾸기 위해 pop하여 받은 가장 마지막 v를 반환함
    - 현재 위치를 바꿈 pop에서 나온 값의 위치로
  - 스택이 공백이 될 때까지 반복한다.

  ```python
  stack = []
  visited = [F]#이미 방문한 지점에 같은 처리 반복 x
  ```

- 모든 정점만 탐색할 수 있으면 됨. 경로는 다양하게 존재

- DFS 알고리즘 - 재귀

  ```python
  DFS_recursive(g, b):
      if visited[v] True
      	for each all w in adjacency(g, v):
          	if visited[w] != True:
                  DFS_recursive(g, w)
  ```

- DFS 알고리즘 - 스택

  ```python
  stack s
  visited[]
  dfs v
  	push(s, v)
      while not isEmpty(s):
          v <- pop(s)
          if not visited[v]:
              visit(v)
              for each w in adjacency(v)
              	if not visited[w]
                  	push(s, w)
  ```

- 인접요소를 확인하는 두 가지 방법 (입력 받는 방법)

  - 인접 행렬

    정점의 개수와 간선의 수

  - 인접 리스트

    연결되어 있는 데이터들만 가지고 있는다 

    다른 정보가 필요 없다?

    

## practice

- 종이붙이기 (재귀)
- 괄호검사 
- 그래프 경로 : 갈 수 있는가 없는가
- 반복문자 지우기