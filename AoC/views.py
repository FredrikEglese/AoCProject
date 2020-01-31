from django.views import generic

class IndexView(generic.ListView):
    template_name = 'AoC/index.html'

    def get_queryset(self):
        return True
    
class SolveView(generic.DetailView):
    template_name = 'AoC/solve.html'

    def get_queryset(self):
        return True