from datetime import date
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from .models import Todo
from django.urls import reverse_lazy


# Create your views here.
class TodoListView(ListView):
    model = Todo
    template_name = 'todo_list.html'

class TodoCreateView(CreateView):
    model = Todo
    fields = ["title", "deadline"]
    template_name = 'todo_form.html'
    context_object_name = 'todos'
    success_url = reverse_lazy('todo_list')
    
class TodoUpdateView(UpdateView):
    model = Todo
    fields = ["title", "deadline"]
    template_name = 'todo_form.html'
    context_object_name = 'todos'
    success_url = reverse_lazy('todo_list')
    
class TodoDeleteView(DeleteView):
    model = Todo
    template_name = 'todo_confirm_delete.html'
    success_url = reverse_lazy('todo_list')
    
class TodoCompleteView(View):
    def get(self, request, pk):
        Todo.objects.get(pk=pk)
        todo = get_object_or_404(Todo, pk=pk)
        todo.finished_at = date.today()
        todo.save()
        return redirect("todo_list")