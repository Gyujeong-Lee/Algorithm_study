#  Hash

> 참고 : https://go-coding.tistory.com/30



## 개념

### Hash

- 어떤 값을 고정된 길이로 변환하는 것

### Hash Function

- Key에 대해 산술연산(고정된 길이로 변환-주소값을 배정하기 위해)을 수행하여 데이터 위치를 찾을 수 있는 값을 출력하는 함수

### Hash 값(해시주소)

- Key를 해시함수를로 연산하여 얻은 값. 이를 기반으로 해시 테이블에서 Key에 대한 데이터 위치를 찾을 수 있다.

### Hash Table 

- 해시 함수를 이용하여 키를 해시값으로 매핑하고 이 해시값을 인덱스 or 주소 삼아 데이터를 key와 함께 저장하는 자료구조 
- 단순하게 key : value 형태라고 보면 됨



## 특징

### 장점

- 해시테이블은 key와 value가 1:1 매핑되어 있기 때문에 삽입, 삭제, 검색의 과정에서 모두 평균적으로 O(1)의 시간 복잡도를 갖고 있다.
- 한마디로 삽입, 삭제, 검색이 빠르다.

### 단점

- 해시 충돌 발생 (참고 URL 확인)
  - 해결 방법 : 개방 주소법, 체이닝 등등
- 순서/관계가 있는 배열에 어울리지 않는다
- 공간 효율성이 떨어진다.
- Hash function의 의존도가 높다. (해당 함수를 구현하는 데 시간이 걸릴 수 있지만, 대부분 구현되어 있음)



## 활용

- 대표적으로 캐시(임시 기억)에서 활용
- DB 인덱싱 원리
- 저장 / 삭제 / 수정 / 검색이 빈번하게 이루어지는 상황에서 사용됨



## 코테 연습

[베스트앨범](../Hash/베스트앨범.py)



