from django.shortcuts import render
from mangoapp.forms import feedback_forms
# Create your views here.
def studentinput_view(request):
    submitted = False
    sname =''
    if request.method == 'POST':
        form =feedback_forms(request.POST)
        if form.is_valid():
            print('Form validation success and print data')
            print('RollNo:',form.cleaned_data['rollno'])
            print('Name:',form.cleaned_data['name'])
            print('Marks:',form.cleaned_data['marks'])
            sname = form.cleaned_data['name']
            submitted = True
    form = feedback_forms()
    return render(request,'mangoapp/form.html', {'form':form,'sname':sname,'submitted':submitted})
