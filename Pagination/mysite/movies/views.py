from django.shortcuts import render
from .models import MovieData
from django.core.paginator import Paginator
# Create your views here.

def movie_list(request):
    movie_list = MovieData.objects.all()

    search_field = request.GET.get('searchbar')
    if search_field != "" and search_field is not None:
        movie_list = movie_list.filter(name__icontains=search_field)

    paginator = Paginator(movie_list, 4)
    page = request.GET.get('page')
    movie_list = paginator.get_page(page)   # Returns the shortened list, ie it returns the list only for that page

    return render(request, 'movies/movie-list.html', {'movie_list': movie_list})