from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.db.models import Q

from .models import Clients

# Create your views here.
def index(request):
    return render(request,'main/index.html')
    
def show_search(request):
    return render(request,'main/show_search.html')
    
def main_add(request):
    pass
    
class SearchResultsView(ListView):
    model = Clients
    template_name = 'main/search_results.html'
 
    def get_queryset(self): # новый
        query = self.request.GET.get('q')
        object_list = Clients.objects.filter(
            Q(full_name__icontains=query) | Q(inn__icontains=query)
        )
        return object_list