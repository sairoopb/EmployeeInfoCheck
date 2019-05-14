from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from .models import Employee,Credential
from django.core.exceptions import ValidationError

class e_form(forms.ModelForm):
    first_name=forms.CharField(label='First Name',max_length=50)
    last_name=forms.CharField(label='Last Name',max_length=50)
    dob=forms.DateField(label='Date of birth',widget = forms.SelectDateWidget())
    email=forms.EmailField(label='Email-ID')
    p_number=forms.IntegerField(label='Phone number')
    adress=forms.CharField(label='Address')
    ed_qualifications=forms.CharField(label='Educational Qualifications')
    class Meta:
        model = Employee
        fields = ('first_name','last_name','dob','email','p_number','adress','ed_qualifications')

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Credential
        fields = ('username','password','email')

    def clean(self):
        data = self.cleaned_data
        # print(data)
        if not Credential.objects.filter(username=data["username"],
                                         password=data["password"],
                                         email=data["email"]).exists():
            raise ValidationError("Invalid")
        return data