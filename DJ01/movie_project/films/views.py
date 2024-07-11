from django.shortcuts import render
from .models import Movie

def add_movie(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        review = request.POST.get('review')
        Movie.objects.create(title=title, description=description, review=review)
    return render(request, 'add_movie.html')

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movie_list.html', {'movies': movies})
