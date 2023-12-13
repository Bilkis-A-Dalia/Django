from django import forms 
from django.core import validators
from typing import Any


# widgets == field to html input
class contactForm(forms.Form):
    name = forms.CharField(label='Full Name : ',help_text='Total lenght must be within 70 characters', 
        required = False, widget= forms.Textarea(attrs={'id': 'text area','class':'class1 class2',
        'placeholder': 'Enter your name: '}))
    # file = forms.FileField( )
    email = forms.EmailField(label='User Email')
    # age = forms.IntegerField()
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    age = forms.CharField(widget=forms.NumberInput)
    check = forms.BooleanField()
    birthday = forms.CharField(widget=forms.DateInput(attrs={'type':'date'}))
    appointment = forms.CharField(widget=forms.DateInput(attrs={'type':'datetime-local'}))
    CHOICES = [('s','small'),('M','medium'),('L','large')]
    size = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    MEAL= [('p','pepperoni'),('m','mashroom'),('b','beaf')]
    pizza = forms.MultipleChoiceField(choices=MEAL, widget=forms.CheckboxSelectMultiple)

# class StudentData(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.EmailField(widget=forms.EmailInput)
    
#     # def clean_name(self):
#     #     valname = self.cleaned_data['name']
#     #     if len(valname) < 10:
#     #         raise forms.ValidationError('Enter a name with atleast 10 characters')
#     #     return valname
#     # def clean_email(self):
#     #     valemail = self.cleaned_data['email']
#     #     if '.com' not in valemail:
#     #         raise forms.ValidationError('Email must have .com')
#     #     return valemail

# shortcut
# class StudentData(forms.Form):
#     name=forms.CharField(widget=forms.TextInput)
#     email=forms.EmailField(widget=forms.EmailInput)
#     def clean(self):
#         cleaned_data = super().clean()
#         valemail=self.cleaned_data['email']
#         valname=self.cleaned_data['name']
#         if '.com' not in valemail:
#             raise forms.ValidationError("Please enter a valid email address")
#         if len(valname)<10 :
#             raise forms.ValidationError("Please enter a name mor than 10 characters")


def len_check(value):
    if len(value) < 10:
        raise forms.ValidationError("Enter a value at least 10 chars")
    
class StudentData(forms.Form):
    name = forms.CharField(validators=[validators.MinLengthValidator(10,message='Enter a name with min 10 characters')])
    text = forms.CharField(widget=forms.TextInput,validators=[len_check])
    email = forms.CharField(widget=forms.EmailInput,validators=[validators.EmailValidator( message='Enter a valid email')])
    age = forms.IntegerField(validators=[validators.MaxValueValidator(34,message='age must be maximum 34'), validators.MinValueValidator(24,message='age must be 24')])
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions = ['pdf','png'],message='File extension must be ended with pdf')])

class PasswordValidationProject(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        val_pass = self.cleaned_data['password']
        val_conpass = self.cleaned_data['confirm_password']
        val_name = self.cleaned_data['name']
        if val_conpass != val_pass:
            raise forms.ValidationError('Password doesnot match')
        if len(val_name) <15:
            raise forms.ValidationError('must be atleast 15 characters')

