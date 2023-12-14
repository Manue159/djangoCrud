from django import forms  
from myapp.models import Employee  
from myapp.models import Technicien  
from myapp.models import Informaticien  

class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = Employee  
        fields = ['name', 'contact', 'email'] 
        widgets = { 'name': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'email': forms.EmailInput(attrs={ 'class': 'form-control' }),
            'contact': forms.TextInput(attrs={ 'class': 'form-control' }),
        }
        

class TechnicienForm(forms.ModelForm):  
    class Meta:  
        model = Technicien  
        fields = ['name', 'contact', 'email'] 
        widgets = { 'name': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'email': forms.EmailInput(attrs={ 'class': 'form-control' }),
            'contact': forms.TextInput(attrs={ 'class': 'form-control' }),
        }


class InformaticienForm(forms.ModelForm):  
    class Meta:  
        model = Informaticien  
        fields = ['name', 'contact', 'email'] 
        widgets = { 'name': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'email': forms.EmailInput(attrs={ 'class': 'form-control' }),
            'contact': forms.TextInput(attrs={ 'class': 'form-control' }),
        }        