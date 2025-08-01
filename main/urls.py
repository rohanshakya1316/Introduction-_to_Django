from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('contact/', views.contact, name="contact"),
    path('task/create', views.create_task, name="create_task"),
    # path('schools/', views.schools, name="schools"),
    path('schools/', views.SchoolView.as_view(), name="schools_list"),
    # path('schools/<int:school_id>/view/', views.school_detail, name="school_detail")
    path('schools/<pk>/view/', views.SchoolDetailView.as_view(), name="school_detail"),
    path('schools/create/', views.SchoolCreate.as_view(), name="create_school"),
    path('schools/update/<pk>/', views.SchoolUpdate.as_view(), name="update_school"),
    path('schools/delete/<pk>/', views.SchoolDelete.as_view(), name="delete_school")
]
