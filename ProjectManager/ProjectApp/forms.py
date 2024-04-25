from django import forms
from .models import Client, Project


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'  # Or specify the fields you want to include in the form

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'  # You can specify the fields you want to include in the form explicitly if needed


class AssignUsersForm(forms.Form):
    # Define fields for assigning users to projects
    user1 = forms.CharField(max_length=100)
    user2 = forms.CharField(max_length=100)