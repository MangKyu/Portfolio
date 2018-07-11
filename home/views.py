from django.shortcuts import render


# Create your views here.
def display_my_page(request):
    return render(request, 'common/mypage.html', {'welcome_text': 'Hello World!'})


def display_my_page_with_param(request, my_parameter):
    welcome_text = my_parameter
    return render(request, 'common/mypage.html', {'welcome_text': welcome_text})
