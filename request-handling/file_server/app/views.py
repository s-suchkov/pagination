import datetime
import os
from django.http import HttpResponse
from app.settings import FILES_PATH
from django.shortcuts import render
print(os.listdir(FILES_PATH))
print(os.stat(FILES_PATH))

# print(os.stat('settings.py'))
def file_list(request, date=None):
    template_name = 'index.html'
    # print(os.listdir('settings.FILES_PATH'))
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    context = {
        'files': [
            # {'name': i,
            #  'ctime': datetime.datetime.fromtimestamp(stat.st_ctime),
            #  'mtime': datetime.datetime.fromtimestamp(stat.st_mtime)}
        ]
        # 'date': datetime.date(2018, 1, 1)  # Этот параметр необязательный
    }
    context_1 = {
        'files': []
        # 'date': datetime.datetime.strptime(date, '%Y-%M-%d').date()
    }
    for i in os.listdir(FILES_PATH):
        list = os.path.join(FILES_PATH, i)
        stat = os.stat(list)
        file = {'name': i,
         'ctime': datetime.datetime.fromtimestamp(stat.st_ctime),
         'mtime': datetime.datetime.fromtimestamp(stat.st_mtime)}
        context['files'].append(file)
        if date!= None:
            date_res = file['mtime'].date()
            # return HttpResponse(f'{date_res}, {date} {date_res==date}')
            if str(date) == str(date_res):
                context_1['files'].append(file)
    if date != None:
        context_1['date'] = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        return render(request, template_name, context_1)

    return render(request, template_name, context)
# print(datetime.date('2018-01-01'))

def file_content(request, name):
    server = os.path.join(FILES_PATH, name)
    with open(server, 'r') as file:
        content = file.read()
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    return render(
        request,
        'file_content.html',
        context={'file_name': name, 'file_content': content}
    )

