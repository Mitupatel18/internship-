from django.shortcuts import render
from .forms import StudentForm

def admission_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or perform other actions upon successful form submission
            # Example: return HttpResponseRedirect('/success/')
    else:
        form = StudentForm()
    
    return render(request, 'admission_form.html', {'form': form})