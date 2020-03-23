from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'main/index.html')
    
def main_search(request):
    pass
    
def main_add(request):
    pass