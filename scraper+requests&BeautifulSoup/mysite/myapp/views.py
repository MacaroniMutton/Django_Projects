from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import Link
# Create your views here.

def scrape(request):
    links = []
    search_bar = request.GET.get('search')
    if search_bar != '' and search_bar is not None:
        page = requests.get(search_bar)
        soup = BeautifulSoup(page.text, 'html.parser')

        for link in soup.find_all('a'):
            link_address = link.get('href')
            link_text = link.string
            Link.objects.create(address=link_address, name=link_text)
        
        links = Link.objects.all()

    if request.method == "POST":
        for link in links:
            link.delete()
        links = []
    return render(request, 'myapp/result.html', {'links': links})