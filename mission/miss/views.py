from django.shortcuts import render, redirect, get_object_or_404
from datetime import date, timedelta
from .models import Habit, HabitDay
from django.contrib import messages


def tracker(request):
    today = date.today()

    start = today - timedelta(days=today.weekday())
    week = [start + timedelta(days=i) for i in range(7)]

    habits = Habit.objects.all()

    # ADD HABIT
    if request.method == "POST" and "new_habit" in request.POST:
        name = request.POST.get("new_habit")
        if name:
            Habit.objects.create(name=name)
            messages.success(request, "Habit added!")
        return redirect("tracker")

    # SAVE CHECKBOXES
    if request.method == "POST" and "save" in request.POST:
        for habit in habits:
            for i, day in enumerate(week):

                if day != today:
                    continue

                key = f"{habit.id}_{i}"
                checked = key in request.POST

                obj, _ = HabitDay.objects.get_or_create(
                    habit=habit,
                    date=day
                )

                obj.completed = checked
                obj.save()

        messages.success(request, "Progress saved!")
        return redirect("tracker")

    habit_data = []

    for habit in habits:
        days = []
        for i, day in enumerate(week):
            completed = HabitDay.objects.filter(
                habit=habit,
                date=day,
                completed=True
            ).exists()

            days.append({
                "done": completed,
                "is_today": (day == today),
                "is_past": (day < today),
                "is_future": (day > today),
                "index": i
            })

        habit_data.append((habit, days))

    return render(request, "index.html", {
        "habit_data": habit_data,
        "week": week,
        "today": today
    })


# DELETE PAGE
def delete_habit(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id)

    if request.method == "POST":
        habit.delete()
        messages.success(request, "Habit deleted!")
        return redirect("tracker")

    return render(request, "delete.html", {"habit": habit})


def landing(request):
    return render(request, "home.html")