from collections import Counter

from django.shortcuts import render_to_response

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()


def index(request):
    transition = request.GET['from-landing']
    # counter_click(transition)
    if transition == 'original':
        counter_click['original'] += 1
    elif transition == 'test':
        counter_click['test'] += 1
    #     return render_to_response('landing_alternate.html')
    return render_to_response('index.html')


def landing(request):
    site = request.GET['ab-test-arg']
    # counter_show(site)
    if site == 'original':
        counter_show['original'] += 1
        return render_to_response('landing.html')
    elif site == 'test':
        counter_show['test'] += 1
        return render_to_response('landing_alternate.html')
    # # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # # в зависимости от GET параметра ab-test-arg
    # # который может принимать значения original и test
    # # Так же реализуйте логику подсчета количества показов
    # return render_to_response('landing.html')


def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Чтобы отличить с какой версии лендинга был переход
    # проверяйте GET параметр marker который может принимать значения test и original
    # Для вывода результат передайте в следующем формате:
    return render_to_response('stats.html', context={
        'test_conversion': counter_click['test']/counter_show['test'],
        'original_conversion': counter_click['original']/counter_show['original'],
    })
