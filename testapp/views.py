from django.shortcuts import render

# Create your views here.
from testapp.models import Movie
def index_view(request):
    return render(request,'testapp/index.html')
def list_movie(request):
    movie_list=Movie.objects.all()
    return render(request,'testapp/movieslist.html',{'movie_list':movie_list})
from testapp.forms import MovieForm
def add_movie(request):
    form = MovieForm()
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index_view(request)
    return render(request,'testapp/add.html',{'form':form})