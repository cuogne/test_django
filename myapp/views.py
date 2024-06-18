from django.shortcuts import render, redirect, get_object_or_404
from .forms import PersonForm
from .models import Person

def index(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PersonForm()
    persons = Person.objects.all()
    return render(request, 'index.html', {'form': form, 'persons': persons})

def delete_person(request, person_id):
    person = get_object_or_404(Person, id=person_id)
    if request.method == "POST":
        person.delete()
        return redirect('index')
    return render(request, 'index.html')
