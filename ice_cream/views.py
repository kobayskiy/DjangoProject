# Внимание, пременную pk из функции ice_cream_detail
# передавть в шаблон в этом задании не надо.
# Достаточно просто получить ее, как второй обязательный
# аргумент и вызвать соответствующий шаблон
from django.shortcuts import render

ice_cream_catalog = [
    {
        'id': 0,
        'title': 'Классический пломбир',
        'description': 'Настоящее мороженое, '
                       'для истинных ценителей вкуса. '
                       'Если на столе появляется пломбир'
                       ' — это не надолго.',
    },
    {
        'id': 1,
        'title': 'Мороженое с кузнечиками',
        'description': 'В колумбийском стиле: мороженое '
                       'с добавлением настоящих карамелизованных кузнечиков.',
    },
    {
        'id': 2,
        'title': 'Мороженое со вкусом сыра чеддер',
        'description': 'Вкус настоящего сыра в вафельном стаканчике.',
    },
]


def ice_cream_detail(request, pk):
    template_name = 'ice_cream/detail.html'
    title = ice_cream_catalog[pk]['title']
    description = ice_cream_catalog[pk]['description']
    context = {
        'title': title,
        'description': description
    }
    return render(request, template_name, context) 


def ice_cream_list(request):
    template_name = 'ice_cream/list.html'
    catalog = ice_cream_catalog
    context = {
        'catalog': catalog
    }

    return render(request, template_name, context) 