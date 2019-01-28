## Python 1. 파이썬 기초 workshop

#### 1. 두 개의 정수 n과 m이 주어집니다. 반복문을 사용하지 않고 별(*) 문자를 이용해 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 출력해보세요. 

n = 5, m = 9

```python
n = 5
m = 9

print(("*" * n + '\n') * m)
```

#### 2. 다음 딕셔너리에서 평균 점수를 출력하시오.

```python
student = {'python':80, 'algorithm':78, 'django':95, 'flask':80}

student.values()
print(sum(student.values())/len(student))
```

#### 3. 다음은 학생들의 혈액형(A, B, AB, O)에 대한 데이터이다. for문을 이용하여 각 혈액형별 학생수의 합계를 구하시오.

```python
blood = ['A','B','O','A','B','A','AB','AB','O','A','O','AB','O']

a = [] # a = 0
b = []
o = []
ab = []
for i in blood:
    if i == "A": 
        a.append(i) # a += 1
    elif i == "B":
        b.append(i)
    elif i == "O":
        o.append(i)
    else:
        ab.append(i)
        
# a_count = a.count

print(f"A형은 {a.count('A')} 명 입니다.")
print(f"B형은 {b.count('B')} 명 입니다.")
print(f"O형은 {o.count('O')} 명 입니다.")
print(f"AB형은 {ab.count('AB')} 명 입니다.")
```

