from django.shortcuts import redirect,render
from django.views import View
from .models import Student
from .forms import AddStudentForm

# Create your views here.

def Cancel(request):
    return redirect('home')


class Home(View):
    def get(self, request):
        stu_data = Student.objects.all()
        return render(request,'core/home.html', {'studata':stu_data})
    
class Add_Student(View):
    def get(self, request):
        fm = AddStudentForm
        return render(request, 'core/add-student.html', {'form':fm})
    
    def post(self, request):
        fm = AddStudentForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/core/')
        else:
            return render(request, 'core/add-student.html', {'form':fm})
        

class Delete_Student(View):
    def get(self, request, id):
        stu = Student.objects.get(id=id)
        fm = AddStudentForm(instance=stu)
        return render(request, 'core/delete-student.html', {'form': fm, 'stud': stu})
        
    def post(self, request, id):
        # Use the 'id' from the URL parameter instead of getting it from the form
        studata = Student.objects.get(id=id)
        studata.delete()
        return redirect('/core/')
    
class Edit_Student(View):
    def get(self, request, id):
        stu = Student.objects.get(id=id)
        fm = AddStudentForm(instance=stu)
        return render(request,'core/edit-student.html', {'form':fm})
    
    def post(self, request, id):
        stu = Student.objects.get(id=id)
        fm = AddStudentForm(request.POST, instance=stu)
        if fm.is_valid():
            fm.save()
            return redirect('/core/')
        else:
            return render(request, 'core/add-student.html', {'form':fm})