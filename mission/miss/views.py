from django.shortcuts import render, redirect
from .models import Habit

def intro(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'index.html')

def add(request):
    if request.method == 'POST':
        habit_name = request.POST.get("habit")
        habit_date = request.POST.get("date")

        if habit_name and habit_date:
            Habit.objects.create(
                name=habit_name,
                task_date=habit_date
            )
            return redirect('track')

    return render(request, 'add.html')


def track(request):
    track = Habit.objects.all()
    return render(request, 'track.html', {'track': track})

def stay(request):
    return render(request, 'stay.html')

def about(request):
    return render(request, 'about.html')
from django.shortcuts import render, redirect, get_object_or_404
from .models import Habit

def toggle(request, id):
    habit = get_object_or_404(Habit, id=id)
    habit.completed = not habit.completed  # switch True/False
    habit.save()
    return redirect('track')