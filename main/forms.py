from django import forms

class add_student_form(forms.Form):
	first_name = forms.CharField(max_length = 20)
	last_name = forms.CharField(max_length = 20)
	b_date = forms.DateTimeField('Birth Date')
	roll = forms.CharField(max_length = 20)
	dept = forms.CharField(max_length = 20)
	session  = forms.CharField(max_length = 20)