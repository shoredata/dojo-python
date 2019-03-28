# Inside your app's forms.py file
from django import forms
from .models import *

class RegisterForm(forms.Form):
    name = forms.CharField(max_length=45)
    company = forms.CharField(max_length=45)
    email = forms.EmailField()
    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput)
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs) # Call to Form constructor
        # self.fields['accountnumber'].widget.attrs['style'] = "width:10%"
        # self.fields['name'].widget.attrs['style'] = "width:50%"
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
                })

class RegisterUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ['created_at', 'updated_at', 'passwordhash_decoded']
    def __init__(self, *args, **kwargs):
        super(RegisterUpdateForm, self).__init__(*args, **kwargs) # Call to ModelForm constructor
        # self.fields['accountnumber'].widget.attrs['style'] = "width:10%"
        # self.fields['name'].widget.attrs['style'] = "width:50%"
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
                })



class LoginForm(forms.Form):
    loginemail = forms.CharField(max_length=45)
    loginpassword = forms.CharField(max_length=100, widget=forms.PasswordInput)
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs) # Call to Form constructor
        self.fields['loginemail'].label = "Email"        
        self.fields['loginpassword'].label = "Password"        
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
                })

# File "/Users/bart/anaconda3/envs/pipenv-py36-aws/lib/python3.6/site-packages/django/forms/models.py", line 243, in __new__
#     "needs updating." % name
# django.core.exceptions.ImproperlyConfigured: Creating a ModelForm without either the 'fields' attribute or the 'exclude' attribute is prohibited; form AccountForm needs updating.

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        exclude = ['created_at', 'updated_at']
    def __init__(self, *args, **kwargs):
        super(AccountForm, self).__init__(*args, **kwargs) # Call to ModelForm constructor
        # self.fields['accountnumber'].widget.attrs['style'] = "width:10%"
        # self.fields['name'].widget.attrs['style'] = "width:50%"
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
                })




class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        exclude = ['created_at', 'updated_at']
    def __init__(self, *args, **kwargs):
        super(DeliveryForm, self).__init__(*args, **kwargs) # Call to ModelForm constructor
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
                })

class TruckForm(forms.ModelForm):
    class Meta:
        model = Truck
        exclude = ['created_at', 'updated_at']
    def __init__(self, *args, **kwargs):
        super(TruckForm, self).__init__(*args, **kwargs) # Call to ModelForm constructor
        self.fields['number'].label = "Truck Number"        
        self.fields['description'].label = "Description"        
        self.fields['truckinspectiondate'].label = "Vehicle Inspection Date"        
        self.fields['tankinspectiondate'].label = "Tank Inspection Date"        
        self.fields['watercapacity'].label = "Water Capacity"        
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
                })




