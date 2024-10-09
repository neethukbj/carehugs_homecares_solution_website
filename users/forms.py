from django import forms
from django.contrib.auth.models import User
from .models import *
from services.models import *

class ProviderSignupForm(forms.ModelForm):
    floating_input_class = 'floating-input form-control'  # Define a reusable class for styling

    username = forms.CharField(widget=forms.TextInput(attrs={'class': floating_input_class, 'placeholder': ' '}), label="Username")
    
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': floating_input_class, 'placeholder': ' '}), )
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': floating_input_class, 'placeholder': ' '}), label="Password")
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': floating_input_class, 'placeholder': ' '}), label="Confirm Password")
    phone_number = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': floating_input_class, 'placeholder': ' '}), label="Phone Number")
    agree_to_terms = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'custom-control-input', 'id': "customCheck1"}),
        label="I agree with the terms of use"
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password', 'phone_number', 'agree_to_terms']
    def clean(self):
        cleaned_data = super().clean()
    
    # Username validation
        username = cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            self.add_error('username', 'This username is already taken. Please choose another one.')
    
    # Password and confirm password validation
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
    
        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match")
    
        return cleaned_data
        


class ProviderPersonalForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}), label="Name")
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Age'}), label="Age")
    gender = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Gender'}), label="Gender")
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}), label="Address")
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}), label="City")
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact No.'}), label="Phone Number")
    alternate_phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Alternate Contact No.'}), label="Alternate Phone Number")

    class Meta:
        model = UserProfile
        fields = ['name', 'age', 'gender', 'address', 'city', 'phone_number', 'alternate_phone_number']


class ProviderServicesForm(forms.ModelForm):
    # service_types = forms.ChoiceField(queryset=ServiceType.objects.all(), widget=forms.ChoiceField(attrs={'class': 'form-control'}), label="Service Types")
    service_types = forms.ModelMultipleChoiceField(
        queryset=ServiceType.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        label="Service Types"
    )
    experience = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Experience'}), label="Experience")
    availability = forms.ChoiceField(
    choices=[('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('temporary', 'Temporary'),],
    widget=forms.Select(attrs={'class': 'form-control'}),
    label="availability"
    )

    #availability = forms.ChoiceField(choices=[('Full-Time', 'Full-Time'), ('Part-Time', 'Part-Time')], widget=forms.Select(attrs={'class': 'form-control'}), label="Availability")
    hourly_salary = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Salary per Hour'}), label="Hourly Salary")
    aadhar_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Aadhar No'}), label="Aadhar Number")
    bank_account = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Bank Account No'}), label="Bank Account")
    ifsc_code = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'IFSC Code'}), label="IFSC Code")
    govt_id = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}), label="Government ID",required=False )
    


    class Meta:
        model = UserProfile
        fields = ['service_types', 'experience', 'availability', 'hourly_salary', 'aadhar_number', 'bank_account', 'ifsc_code', 'govt_id']


class ProviderImageForm(forms.ModelForm):
    profile_picture = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}), label="Profile Picture",required=False )
    about_me = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Tell about You'}), label="About Me")
    # password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Password" )
    # repeat_password=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Repeat Password" )

    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'about_me']



#####Clientside starting ####

class ClientSignupForm(forms.ModelForm):
    floating_input_class = 'floating-input form-control'  # Define a reusable class for styling

    username = forms.CharField(widget=forms.TextInput(attrs={'class': floating_input_class, 'placeholder': ' '}), label="Username")
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': floating_input_class, 'placeholder': ' '}), )
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': floating_input_class, 'placeholder': ' '}), label="Password")
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': floating_input_class, 'placeholder': ' '}), label="Confirm Password")
    phone_number = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': floating_input_class, 'placeholder': ' '}), label="Phone Number")
    agree_to_terms = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'custom-control-input', 'id': "customCheck1"}),
        label="I agree with the terms of use"
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password', 'phone_number', 'agree_to_terms']
    
    def clean(self):
        cleaned_data = super().clean()
    
    # Username validation
        username = cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            self.add_error('username', 'This username is already taken. Please choose another one.')
    
    # Password and confirm password validation
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
    
        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match")
    
        return cleaned_data
        
class ClientPersonalForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}), label="Name")
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Age'}), label="Age")
    gender = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Gender'}), label="Gender")
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}), label="Address")
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}), label="City")
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact No.'}), label="Phone Number")
    alternate_phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Alternate Contact No.'}), label="Alternate Phone Number")

    class Meta:
        model = UserProfile
        fields = ['name', 'age', 'gender', 'address', 'city', 'phone_number', 'alternate_phone_number']


class ClientServicesForm(forms.ModelForm):
    # service_types = forms.ChoiceField(queryset=ServiceType.objects.all(), widget=forms.ChoiceField(attrs={'class': 'form-control'}), label="Service Types")
    service_needed = forms.ModelMultipleChoiceField(
        queryset=ServiceType.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        label="Service Types"
    )
    # experience = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Experience'}), label="Experience")
    availability = forms.ChoiceField(
    choices=[('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('temporary', 'Temporary'),],
    widget=forms.Select(attrs={'class': 'form-control'}),
    label="availability"
    )

    availability = forms.ChoiceField(choices=[('Full-Time', 'Full-Time'), ('Part-Time', 'Part-Time')], widget=forms.Select(attrs={'class': 'form-control'}), label="Availability")
    # hourly_salary = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Salary per Hour'}), label="Hourly Salary")
    aadhar_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Aadhar No'}), label="Aadhar Number")
    bank_account = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Bank Account No'}), label="Bank Account")
    ifsc_code = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'IFSC Code'}), label="IFSC Code")
    # govt_id = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}), label="Government ID",required=False )
    


    class Meta:
        model = UserProfile
        fields = ['service_needed',  'availability', 'aadhar_number', 'bank_account', 'ifsc_code']


class ClientImageForm(forms.ModelForm):
    profile_picture = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}), label="Profile Picture",required=False )
    about_work= forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Tell about You'}), label="About Me")
    # password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Password" )
    # repeat_password=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Repeat Password" )

    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'about_work']