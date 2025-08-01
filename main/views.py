from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task, School
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
# tasks = [{'title': 'Task One', "description": 'This is Task One description'},
#              {'title': 'Task Two', "description": 'This is Task Two description'}
#     ]

class SchoolCreate(CreateView):
    model = School
    fields = "__all__"
    success_url = reverse_lazy("schools_list")

class SchoolUpdate(UpdateView):
    model = School
    fields = "__all__"
    success_url = reverse_lazy("schools_list")

class SchoolDelete(DeleteView):
    model = School
    success_url = reverse_lazy("schools_list")

class SchoolDetailView(DetailView):
    model = School

class SchoolView(ListView):
    model = School

def school_detail(request, school_id):
    print('This is dynamic url', school_id)
    return HttpResponse(f"<h1>This is dynamic url demo. The dyanmic value is {school_id}</h1>")

# def schools(request):
#     print("This is school page.")
#     return HttpResponse("<h1>This is school Page.</h1>")

def home(request):
    print("This is home page.")
    user_name = "Rohan"
    tasks = Task.objects.all()
    context = {"user": user_name,
                "tasks": tasks
            }
    # return HttpResponse("<h1>This is home page content.</h1>")
    return render(request, "main/home.html", context)

def create_task(request):
    if request.method == "POST":
        print("----------This is post request----------")
        data = request.POST
        task_title = data.get('title')
        task_desc = data.get('description')
        # new_task = {'title': task_title, 'description': task_desc}
        # global tasks
        # tasks.append(new_task)
        Task.objects.create(
            title = task_title, 
            description = task_desc
        )
        return redirect(home)
        # print(data)


    return render(request, "main/create-task.html")

def contact(request):
    print("This is contact page.")
    return HttpResponse("<h1>This is contact page content.</h1>")