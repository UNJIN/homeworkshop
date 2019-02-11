### Python 활용 SQL

### 1. Django에서 선언한 Model을 실제 DB에 반영하는 과정을 무엇이라고 하는가?

- migrate

우리가 작성한 모델을 DB에 반영하기 위해서는 마지막으로 마이그레이션 이라는 것을 해 주어야 한다.

이 것은 프로젝트 폴더 경로에서 

python manage.py makemigrations
python manage.py migrate 

이 두가지 명령을 실행해 주면 된다.

### 2. 모델의 필드를 정의할 때 CharField는 필수로 들어가야하는 인자가 존재한다. 무엇인가?

max_length,	문자열 데이터를 저장하는 필드. 최대 글자 수를 반드시 지정해주어야 한다.

### 3. Django 에서 동작하는 모든 명령을 대화식 Python 쉘에서 시험할 수 있는 명령어를 작성하세요.

python manage.py shell

### 4. Post라는 이름의 모델은 CharField로 정해진 title과 CharField로 정해진 content가 필드로 정의 되어있다. 제목은 자신의 이름, 내용은 자신의 이메일 정보가 들어간 Post를 만드는 코드를 작성하세요

from board.models import Post
p = Post(title="나원", content="yud02150@gmail.com")
p.save()