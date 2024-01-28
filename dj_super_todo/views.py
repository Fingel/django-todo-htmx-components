from django.shortcuts import render

from dj_super_todo.models import Todo


def index(request):
    todos = Todo.objects.all()
    return render(request, "index.html", {"todos": todos})
