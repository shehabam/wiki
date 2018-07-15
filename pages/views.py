from django.shortcuts import render
from .models import Page
# Create your views here.
def wiki_list(request):
    wikis = Page.objects.all()
    context = {
        'wikis': wikis
    }
    return render(request, 'list.html', context)

def wiki_detail(request, page_id):
    wikis = Page.objects.get(id=page_id)
    context = {
        'wikis': wikis
    }
    return render(request, 'detail.html', context)
