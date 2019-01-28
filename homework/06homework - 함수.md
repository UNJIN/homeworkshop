## homework06 - 함수

#### 1. 우리가 이제까지 활용했던 print는 내장 함수(built-in function)입니다.

#### 배웠던 내장 함수 중 5개만 나열해보세요.

`abs`(*x*)

숫자의 절댓값을 돌려줍니다. 인자는 정수 또는 실수입니다. 인자가 복소수면 그 크기가 반환됩니다.

`all`(*iterable*)

*iterable* 의 모든 요소가 참이면 (또는 iterable 이 비어있으면) `True` 를 돌려줍니다. 다음과 동등합니다:

`any`(*iterable*)

*iterable* 의 요소 중 어느 하나라도 참이면 `True` 를 돌려줍니다. iterable이 비어 있으면 `False` 를 돌려줍니다. 다음과 동등합니다.

`bin`(*x*)

정수를 "0b" 가 앞에 붙은 이진 문자열로 변환합니다. 결과는 올바른 파이썬 표현식입니다. *x* 가 파이썬 [`int`](https://docs.python.org/ko/3/library/functions.html#int) 객체가 아니라면, 정수를 돌려주는 [`__index__()`](https://docs.python.org/ko/3/reference/datamodel.html#object.__index__) 메서드를 정의해야 합니다.

`bool`([*x*])

논리값, 즉 `True` 또는 `False` 중 하나를 돌려줍니다. *x* 표준 [논리값 검사 절차](https://docs.python.org/ko/3/library/stdtypes.html#truth) 를 사용하여 변환됩니다. *x* 가 거짓이거나 생략되면 `False` 를 돌려줍니다. 그렇지 않으면``True`` 를 돌려줍니다.

 `float`([*x*])

숫자 또는 문자열 *x* 로 부터 실수를 만들어 돌려줍니다.



#### 2. 다음 중 틀린 것은?

#### (1) 함수는 오직 하나의 객체만 반환할 수 있어서, return a, b 처럼 쓸 수 없다.

#### (2) 함수에서 return을 작성하지 않으면 None 값을 반환한다.

#### (3) 함수의 인자(parameter)는 함수 선언시 설정한 값이며, 인수(argument)는 함수 호출시 넘겨주는 값이다.

#### (4) 가변 인자를 설정할 때는 인자 앞에서 *을 붙이고, 이때는 함수 내에서 tuple로 처리된다.

#### (5) 파이썬 활용되는 ‘스코프(scope)’ 룰에 따르면 변수에서 값을 Local scope ->

#### Global scope -> Built-in scope 순으로 찾는다.

-> 1번

5번 설명)

- `L`ocal scope: 정의된 함수
- `E`nclosed scope: 상위 함수
- `G`lobal scope: 함수 밖의 변수 혹은 import된 모듈
- `B`uilt-in scope: 파이썬안에 내장되어 있는 함수 또는 속성

####  

#### 3. 함수의 인자 기본 값을 설정을 활용하여 곱셈의 결과를 반환하는 my_mul을 만들어주세요.

예시 호출1) my_mul(6)
예시 결과1) 6
예시 호출2) my_mul(3, 5)
예시 결과2) 15

```python
def my_mul(a,b=1): # 두수의 곱이니까 인자 두개
    return a*b # 뒤의 b값이 디폴트설정
print(my_mul(6))
print(my_mul(4,3))
```





