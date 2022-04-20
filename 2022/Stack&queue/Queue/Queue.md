# Queue

## queue란?

- 특성 

  - 삽입과 삭제의 위치가 제한적인 자료구조

    뒤에서는 삽입, 앞에서만 삭제

  - FIFO 선입선출 구조



- 구조 및 기본 연산

  - Front : 저장된 원소 중 첫 번째 원소 (가장 최근에 꺼내진 위치 / 마지막으로 꺼내진 위치)

  - Rear : 저장된 원소 중 마지막 원소

  - 주요연산 

    - 삽입 : enQueue(item) - rear 다음에 원소를 삽입

      rear += 1

    - 삭제 : deQueue() - front에서 원소를 삭제하고 반환

      fron += 1 필요 (top += 1 과 같은 로직)

    - createQueue() : 공백 상태의 큐를 생성하는 연산

      Q = [ ]

      Q = [0] * 100 

    - isEmpty() : 큐가 공백 상태인지를 확인하는 연산

      front 와 rear가 같은 값을 가지고 있는 지 확인.

      while not isEmpty:

      while front != rear:

    - isFull() : 큐가 포화 상태인지 확인하는 연산

      고정적인 크기의 큐에 대해 필요함

    - Qpeek() : front에서 원소를 삭제하지 않고 반환하는 연산



- 연산과정

  - 공백 큐 생성 : createQueue();

    front = rear = -1 초기화 (아무것도 접근할 수 없는 값) but list의 특성에 주의할 것.

  - 원소 A 삽입 : enQueue(A);

    rear += 1 

  - 원소 B 삽입 : enQueue(B);

    rear += 1

  - 원소 반환/삭제 : deQueue();

    front += 1 -> 원소 삭제 

  - 원소 C 삽입 : enQueue(C);

  - if rear == front : 공백상태 의미



- 큐의 구현

  - 선형큐
    - 1차원 배열을 이용한 큐
      - 큐의 크기 = 배열의 크기
      - front : 마지막에 꺼내진 원소의 인덱스
      - rear : 저장된 마지막 원소의 인덱스
    - 상태 표현
      - 초기 상태 : front = rear = -1
      - 공백 상태 : front == rear
      - 포화 상태 : rear == n-1 (n : 배열의 크기, n-1 : 배열의 마지막 인덱스)

  

  - 초기 공백 큐 생성(여기부터 교재보면 코드가 있다.)

    - 크기 n인 1차원 배열 생성 
    - front 와 rear -1로 초기화

  - 삽입(enQueue(item))

    - 마지막 원소 뒤에 새로운 원소를 삽입하기 위해

      - 포화 검사

      - rear + 1 : 새로운 원소를 삽입할 자리를 마련
      - 그 인덱스에 해당하는 배열원소 Q[rear] = item

  - 삭제(deQueue)

    - 가장 앞에 있는 원소를 삭제하기 위해

      - 공백 검사

      - front의 값을 하나 증가시켜 큐에 남아있는 첫 번째 원소로 이동한다.
      - 그때 새로운 첫번째 원소를 리턴 함으로써 삭제와 동일한 기능

  - 공백 상태와 포화 상태

    - 공백 : front == rear
    - 포화 : rear == n-1

  - 검색 : Qpeek()

    - 가장 앞에 있는 원소를 검색하여 반환하는 연산
    - 비어있는지 검사 후 Q[front + 1] 
    - front의 값을 변화시키지 않는다.



- 선형 큐 이용시의 문제점

  - 잘못된 포화상태 인식

    고정된 크기의 큐에서 원소의 삽입과 삭제가 수차례 수행된 경우 rear가 n-1임에도 불구하고 front가 0번째 자리가 아닐 수 있다.

  - 해결방법1

    매 연산이 이루어질 때마다 저장된 원소들을 배열의 앞부분으로 모두 이동시킴

    원소 이동에 많은 시간이 소요되어 큐의 효율성이 급격히 떨어짐

  - 해결방법2

    1차원 배열을 사용하되, 논리적으로 배열의 처음과 끝이 연결되어 원형 형태의 큐를 이룬다고 가정하고 사용
  
- 원형 큐의 구조

  - 초기 공백 상태

    - front = rear = 0

  - index의 순환

    - front와 rear의 위치가 n-1을 가리킨 후 논리적 순환을 이루어 배열의 처음 인덱스 0으로 이동해야 함.
    - % 연산 이용

  - front 변수

    - 공백 상태와 포화상태 구분을 쉽게 하기 위해 front가 있는 자리는 사용하지 않고 항상 빈자리로 둠

      

- 원형 큐의 구현 (교재에 코드 전체 있음)

  - 초기 공백 큐 생성

    - 크기 n인 1차원 배열 생성
    - front = rear = 0

  - 공백 및 포화상태 검사 : isEmpty(), isFull()

    - 공백 : front == rear
    - 포화상태 : 삽입할 rear의 다음 위치(rear+1 % n) == 현재 front

    ```python
    def is_empty():
        return front == rear
    def is_full():
        return (rear+1) % len(q) == front
    ```

  - 삽입 : enQueue(item)

    마지막 원소 뒤에 새로운 원소를 삽입하기 위해

    - rear 값을 조정 : rear = (rear+1) % n
    - 배열에 원소 저장 Q[rear] = item

    ```python
    def enQueue(item):
        global rear
        if isFull():
            print('q is full')
        else:
            rear = (rear+1) % len(q)
            q[rear] = item
    ```

  - 삽입 : enQueue(item)

    마지막 원소 뒤에 새로운 원소를 삽입하기 위해

    - rear 값을 조정 : rear = (rear+1) % n
    - 배열에 원소 저장 Q[rear] = item

    ```python
    def enQueue(item):
        global rear
        if isFull():
            print('q is full')
        else:
            rear = (rear+1) % len(q)
            q[rear] = item
    ```

  - 삽입 : enQueue(item)

    마지막 원소 뒤에 새로운 원소를 삽입하기 위해

    - rear 값을 조정 : rear = (rear+1) % n
    - 배열에 원소 저장 Q[rear] = item

    ```python
    def enQueue(item):
        global rear
        if isFull():
            print('q is full')
        else:
            rear = (rear+1) % len(q)
            q[rear] = item
    ```

    

  - 삭제 : deQueue()

    가장 앞에 있는 원소를 삭제하기 위해

    - front의 값을 조정하여 삭제할 자리를 준비함
    - 새로운 front 원소를 리턴함으로써 삭제와 동일한 기능함

    ```python
    def deQueue():
        global front
        if isEmpty():
            print('q is empty')
        else:
            front = (front+1) % len(q)
            return q[front]
    ```

  

- 연결 큐의 구조

  > 공간 활용도가 좋음 but 복잡하고 구현이 어려움
  >
  > 단순연결리스트 : 한방향으로 이동 가능

  - 단순 연결 리스트를 이용한 큐
    - 큐의 원소 : 단순 연결 리스트의 노드 (데이터 / 참조주소)
    - 큐의 원소 순서 : 노드의 연결 순서, 링크로 연결되어 있음
    - front : 첫번째 노드를 가리키는 링크
    - rear : 마지막 노드를 가리키는 링크
  - 상태표현
    - 초기 : front = rear = None
    - 공백 : front = rear = None

- 연결 큐의 연산과정(연결 리스트에 대해 학습 후 다시 다룰 예정)



## 우선순위 큐

- 우선순위 큐의 특성
  - 우선순위를 가진 항목들을 저장하는 큐
  - FIFO 순서가 아닌, 우선순위가 높은 순서대로 먼저 나가게 된다.
- 적용분야
  - 시뮬레이션 시스템
  - 네트워크 트래픽 제어
  - 운영체제의 테스크 스케줄링
- 구현
  - 배열 이용 (크기 고정)
  - 리스트 이용
- 기본 연산 (tree 와 heap)



- 배열을 이용한 우선순위 큐 구현

  - 배열을 이용하여 자료 저장
  - 원소를 삽입하는 과정에서 우선순위를 비교하여 적절한 위치에 삽입하는 구조
  - 가장 앞에 최고 우선순위의 원소가 위치

- 문제

  - 삽입과 삭제 연산 시 원소의 재배치가 발생함
  - 시간과 메모리 낭비가 크다.

  

## BFS\**

> 너비 우선 탐색 알고리즘

#### 그래프 탐색법

- 깊이 우선 탐색 DFS

- 너비 우선 탐색 BFS

  인접한 정점 모두 차례로 방분 후 방문했던 정점을 시작점으로 다시 인접한 장저들을 차례로 방문하는 방식

  인접한 정점들에 대해 탐색 후, 차례로 다시 너비우선탐색을 진행해야 함, FIFO, que 활용

#### 알고리즘

- 입력 파라미터 : 그래프 G(인접행렬, 리스트) 와 탐색 시작점 v

- 슈더코드

  ```python
  def BFS(G, v): #그래프 G, 시작점 v
      visited = [0] * n+1 #n : 정점의 개수
      queue = [] #큐 생성
      queue.append(v) #시작점 v를 큐에 삽입
      while queue : #큐가 비어있지 않을 때 / 시작점을 넣은 후 시작점에서 방문할 수 있는 모든 정점 탐색
          t = queue.pop(0) #큐의 첫번째 원소 반환 (deQueue )
          if not visited[t]:
              visited[t] = True#방문 표시
              visit(t)#방문 체크할 때 필요한 작업을 해라~
          for i in G[t]:#t와 인접한 정점들 
              if not visited[i]:
                  queue.append(i)
  ```

- 초기상태

  - visited 배열 초기화
  - Q 생성
  - 시작점 enqueue

- v점부터 시작

  - deQueue v
  - v 방문 표시
  - v의 인접점 enQueue

- 탐색 진행

  - deQueue B
  - B 방문 표시
  - B의 인접점 enqueue

- 완전그래프 혹은 정점이 겹치는 경우 불필요한 메모리 낭비 존재

  - 시작점에서 방문 처리를 해줌

  ```python
  def BFS(G, v): #그래프 G, 시작점 v
      visited = [0] * n+1 #n : 정점의 개수
      queue = [] #큐 생성
      queue.append(v) #시작점 v를 큐에 삽입
      visited[v] = True
      while queue : #큐가 비어있지 않을 때 / 시작점을 넣은 후 시작점에서 방문할 수 있는 모든 정점 탐색
          t = queue.pop(0) #큐의 첫번째 원소 반환 (deQueue )
          for i in G[t]:#t와 인접한 정점들 
              if not visited[i]:
                  queue.append(i)
                  visited[i] = True
  ```

  - 초기 상태 
    - visited 배열 초기화
    - Q의 생성
    - 시작점 enQueue
    - visted[v] = True
  - point : Queue에 삽입하기 전에 방문처리를 선처리하자.



#### BFS의 활용

> 그래프 형태에서 무엇인가 뽑아냈다.

- BFS 2차원 리스트 탐색

  Q에 좌표를 튜플 형태로 저장

  같은 크기에 2차원 리스트 생성 - visited 체크 and 거리를 표시

  최단 거리를 파악할 수 있다.

- 방향 그래프

  비상 연락망

  - DFS 탐색 시 3시간 소요

  - BFS 탐색 시 2시간 소요



## 큐의 활용 : 버퍼

> 데이터를 한 곳에서 다른 한 곳으로 전송하는 동안 일시적으로 그 데이터를 보관하는 메모리의 영역

- 버퍼링 : 버퍼를 활용하는 방식 또는 버퍼를 채우는 동작을 의미한다.
- 자료구조 
  - 입출력 및 네트워크와 관련된 기능에서 이용된다.
  - 순서대로 입/출력/ 전달을 해야 함으로 FIFO 방식인 자료구조 큐를 사용



## 총정리

#### Stack

- LIFO : 후입선출
- 선형 스택 : 일정한 크기에 배열을 만들어 놓고 활용 top
- 리스트 활용 가능 []
- 내장함수
- 연결스택



#### Queue

- FIFO : 선입선출
- 선형 Queue : 배열 활용
- 리스트 활용 가능 [] // pop(0) 써야함
- 내장함수
- 원형 큐
- 연결 큐 / 우선순위 큐

#### DFS

> 깊이우선탐색 시 stack 자료 구조 활용
>
> 끝까지 내려 갔다가 처음으로 돌아옴

- 백트래킹 (유망성 검사) : 가능성이 없다면 탐색 x 

#### BFS 

>  너비우선탐색 시 Queue 자료 구조 활용
>
> 인접 정점 검사 후

- 최단거리 : 거리 탐색 가능 



