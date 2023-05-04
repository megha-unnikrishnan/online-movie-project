from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm
def movie(request):
    obj=Movie.objects.all()
    return render(request,'index.html',{'display':obj})

# def detail(request,movie_id):
#     return HttpResponse("This is movie no %s" %movie_id)


def detail(request, movie_id):
    movies = Movie.objects.get(id=movie_id)
    return render(request, 'detail.html', {'movie': movies})





def add_movie(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        decsc = request.POST.get('decscription',)
        year = request.POST.get('year',)
        img = request.FILES['file']
        movie=Movie(name=name,decscription=decsc,year=year,image=img)
        movie.save()
        print("saved succesfully")
    return render(request,'add.html')

def update(request,id):
    movie=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():

        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})

def delete(request,id):
    if request.method == 'POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')
# Create your views here.
