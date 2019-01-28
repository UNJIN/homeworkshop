### 15homework - Django Web Framework

#### 1. 우리가 사용하는 SQLite 는 RDBMS 에 속한다. RDBMS 의 특징을 2가지만 작성하세요.

1. 파일보다 더 빠르게 데이터를 접근할 수 있다.
2. 특정 패턴에 맞춰 데이터를 쉽게 추출할 수 있다.
3. 많은 사용자의 동시 접근에 자체 해결방법을 가지고 있다.



#### 2. True False

2.1. RDBMS를 조작하기 위해서는 SQL 문을 사용한다. [ T ]
2.2. SQL 에서 명령어는 대문자로 써야만 동작한다. [ F ] (키워드 대문자 권장)
2.3. 일반적인 SQL 문에서 명령어는 세미콜론(;) 으로 끝난다. [ T ]
2.4. SQLite 에서 dot(.) 으로 시작하는 명령어는 SQL 이 아니다.[ T ] (sqlite의 문법)
2.5. 한 개의 DB 에는 한개의 테이블만 존재한다. [ F ]



#### 3. 다음 코드의 실행결과로 나타나는 값을 작성하세요.

sqlite> .nullvalue “NULL”
sqlite> CREATE TABLE ssafy (
...> id INTEGER,
...> location TEXT,
...> class INTEGER
...> );
sqlite> INSERT INTO ssafy (id, location)
...> VALUES (1, ‘JEJU’);
sqlite> SELECT class FROM ssafy WHERE id=1;



-> NULL

