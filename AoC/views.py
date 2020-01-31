from django.views import generic
import os

class IndexView(generic.ListView):
    template_name = 'AoC/index.html'
    context_object_name = 'avaliable_solution_list'

    def get_queryset(self):
        return (["a", "b"])
        

class SolveView(generic.DetailView):
    template_name = 'AoC/solve.html'

    def get_queryset(self):
        return True