from django.shortcuts import render

class DemoClass: 
    def __init__(self):
        self.content = "Default Value of object"

# Create your views here.
def home(request):
    user = {'name': 'Rohan Shakya', 'age': 24}
    interests = ['reading', 'writing', 'coding', 'exploring']
    demo = DemoClass()

    context = {
        'user' : user,
        'interests' : interests,
        'demo' : demo
    }
    return render(request, 'app/home.html', context)

def posts(request):
    demo = "Posts Demo for Django templates "
    user_role = "users"
    posts = [
        {
            'title': 'Happy birthday', 
            'caption': "Many Many Happy returns of the day.", 
            'tags' : ['ram', 'shyam', 'hari']
        }, 
        {
            'title': 'Congratulations', 
            'caption': "Happy to be the part of your success.", 
            'tags' : ['ram', 'shyam', 'hari']
        }, 
        {
            'title': 'Fest and Festivals Happiness', 
            'caption': "Together we celebrate the fest and festivals.", 
            'tags' : ['ram', 'shyam', 'hari']
        }
    ]

    context = {
        'data' : posts,
        'user_role': user_role,
        'demo': demo
    }

    return render(request, 'app/posts.html', context)