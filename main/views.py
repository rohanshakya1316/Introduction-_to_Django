from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task

# Create your views here.
# tasks = [{'title': 'Task One', "description": 'This is Task One description'},
#              {'title': 'Task Two', "description": 'This is Task Two description'}
#     ]

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