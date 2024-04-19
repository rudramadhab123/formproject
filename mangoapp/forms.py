from django import forms
from django.core import validators
class feedback_forms(forms.Form):
    rollno = forms.IntegerField()
    name=forms.CharField(max_length=20)
    marks=forms.FloatField()
    #slno=forms.IntegerField()
    scourse=forms.CharField(max_length=30)
    feedback=forms.CharField(widget=forms.Textarea)
    #print("hiiiiiiiiiiiiii")
    def clean(self):
        print('Total form validation.....')
        total_cleaned_data = super().clean()
        print('Validating Name')
        inputname = total_cleaned_data['name']
        if inputname[0].lower() != 's':
            raise forms.ValidationError('name should be starts with s')
        inputrollno = total_cleaned_data['rollno']
        print('Validating rollno')