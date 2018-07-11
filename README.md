# MangKyu's Blog



현재 개발 진행중입니다.

Start Server: python manage.py runserver

superuser id: mang

superuser pw: over 8 words

내일: 

- 장고 전반: https://tuwlab.com/26314
- URL 매핑: https://tuwlab.com/26351
- 장고 전반: https://wayhome25.github.io/django/2018/03/03/django-deploy-01-settings/
- 환경 세팅: http://blog.embian.com/search/django
- 장고 개념: https://docs.djangoproject.com/ko/2.0/intro/tutorial01/
- Rest Framework: https://javafa.gitbooks.io/python-django/content/chapter4.html
- Templates 읽어보기: https://docs.djangoproject.com/en/1.8/topics/templates/



### File Architecture

`[myproject]         : 프로젝트 루트 디렉토리`

` +-  [conf]      : 사이트 공통 플랫폼 디렉토리`

` |   +- settings.py : 사이트 전역 설정(DB, 언어 및 시간, DEBUG 등)`

` |   +- urls.py     : URL 라우팅 규칙을 정의`

` |   +- wsgi.py     : 실제 운용시 웹 서버와 연동하기 위한 WSGI 포트`

` +-  [home]         : 모듈(App) 디렉토리`

` |   +- admin.py    : 모듈을 Admin모듈과 연동하기 위한 설정`

` |   +- models.py   : 모듈에서 사용할 DB Model을 정의`

` |   +- views.py    : 모듈의 실질적인 동작을 정의`

` +- manage.py       : 사이트 관리를 위한 백엔드 콘솔`



=>  추후에 Settings는 분리될 예정(https://aweekj.github.io/django-setting-file/)



### Django MAKEMIGRATIONS/ MIGRATE

Django에서 DB를 업데이트할 때 쓰는 커맨드 2가지가 있다.

* python manage.py makemigrations
* python manage.py migrate

makekigrations는 Model의 변경내역을 파일로 생성하기 위해 사용한다. 그 파일은 migrations 디렉토리에 0001_inital.py로 저장된다.  0001_inital.py의 코드를 들여다보면 변경 내역을 파일로 생성하였음을 알 수 있고, 이 변경내역을 가지고 SQL을 생성해서 DB를 건드린다. 예를 들어 models.py에서 'content' 칼럼을 'new_conent'로 바꿨는데, 이를 SQL로 변환하는 변경내역(migrations)이 단순히 기존의 content를 삭제해버리고, new_content를 생성하는 작업이라면 기존에 사용자들이 작성한 데이터들을 다 날려버리는 실수를 저지르는 것이다. 

그렇기 때문에 migrations 생성 + migrate를 한번에 묶어서 실행하는 것이 아니라, 분리해야 한다. 



from 
https://undutifulchild.wordpress.com/2015/07/21/django%EC%9E%A5%EA%B3%A0-makemigrations-migrate/

https://wayhome25.github.io/django/2017/03/20/django-ep6-migrations/

### References from

* https://wikidocs.net/6609
* http://heiswed.tistory.com/entry/%EC%9E%A5%EA%B3%A0-%EA%B0%9C%EB%B0%9C-%ED%99%98%EA%B2%BD-%EC%9C%88%EB%8F%84%EC%9A%B0-%EA%B0%9C%EB%B0%9CPC%EC%97%90-%EC%84%A4%EC%B9%98%ED%95%98%EA%B8%B0
* https://inwon5554.github.io/django-blog-nginx/
* http://www.w3big.com/ko/django/django-nginx-uwsgi.html

