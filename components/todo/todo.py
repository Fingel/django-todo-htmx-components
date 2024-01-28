from django.http import HttpResponse
from django_components import component

from dj_super_todo.models import Todo


@component.register("todo")
class TodoComponent(component.Component):
    template_name = "todo/todo.html"

    def get_context_data(self, todo):
        return {"todo": todo}

    def post(self, request, *args, **kwargs):
        todo = Todo.objects.create(content=request.POST["content"])
        return self.render_to_response({"todo": todo})

    def delete(self, request, pk, *args, **kwargs):
        Todo.objects.get(pk=pk).delete()
        return HttpResponse()

    class Media:
        css = "todo/todo.css"
