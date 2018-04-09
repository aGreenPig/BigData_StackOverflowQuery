from django.http import HttpResponse
from django.shortcuts import render

from .word_vector_model import *


def index(request):
    if request.method == 'POST':
        q = request.POST['query']
        print(q)

        if not q:
            result_list = ["Nothing searched"]
        else:
            result = run_program(q)
            result_list = result.split('<br>')

        c = {'result_list': result_list}
    else:
        c = {'result_list': {}}

    return HttpResponse(render(request, 'result.html', c))
