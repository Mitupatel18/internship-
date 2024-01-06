from django.urls import path
from .views import Home, Add_Student, Delete_Student, Edit_Student
from core import views

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('add-student/', Add_Student.as_view(), name='add-student'),
    path('delete-student/<int:id>/', Delete_Student.as_view(), name='delete-student'),
    path('edit-student/<int:id>/', Edit_Student.as_view(), name='edit-student'),
    path('cancel-action/', views.Cancel, name='cancel'),


]
