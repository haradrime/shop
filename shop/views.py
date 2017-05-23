from django.shortcuts import render
from shop.models import *


def shop(request):
    # session_key = request.session.session_key
    # if not session_key:
    #     request.session.cycle_key()
    #
    # print(request.session.session_key)

    return render(request, 'shop/shop.html', locals())
