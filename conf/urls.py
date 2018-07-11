"""conf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from home import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^mypage/', views.display_my_page),
    url(r'^mypage2/(?P<my_parameter>.+)', views.display_my_page_with_param)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

''' URL은 정규표현식과 함께 사용된다.
    '^mypage2/(?P<my_parameter>.+)'부분에서 mypage2/~~~ 뒤에 내용은 my_parameter로 전달하라는 의미다.
    일반적인 정규식이라면 '(.+)' 으로 나타내고 이 그룹의 이름은 Group#1 이겠지만,
    파이썬에서는 '(?p<그룹 이름>.+)' 로 그룹이름을 임의로 적용할 수 있다.
    여기서 설정한 my_parameter라는 그룹 이름은 views.display_my_page_with_param 에서 사용된다.
'''

urlpatterns += staticfiles_urlpatterns()
