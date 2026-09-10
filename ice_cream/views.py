# Внимание, пременную pk из функции ice_cream_detail
# передавть в шаблон в этом задании не надо.
# Достаточно просто получить ее, как второй обязательный
# аргумент и вызвать соответствующий шаблон
from django.http import HttpResponse


def ice_cream_detail(request, pk):
    return HttpResponse(f'Мороженое номер {pk}')


def ice_cream_list(request):
    return HttpResponse('Список мороженого')