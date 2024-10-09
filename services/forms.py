from django import forms
from .models import BookingRequest

class BookingForm(forms.Form):
    # work_location = forms.CharField(
    #     label="Work Location",
    #     max_length=100,
    #     widget=forms.TextInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': '',
    #         'id': 'exampleInputText02'
    #     })
    # )
    
    booking_date = forms.DateField(
        label="Booking Date",
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date'
        })
    )
    
    service_type = forms.ChoiceField(
        label="Service Type*",
        choices=[],  # Empty by default, to be populated dynamically
        widget=forms.Select(attrs={
            'class': 'form-control ',
            
        })
    )
    
    start_time = forms.TimeField(
        label="Start Time*",
        widget=forms.TimeInput(attrs={
            'class': 'form-control',
            'type': 'time',
            'id': 'exampleInputText05'
        })
    )
    
    end_time = forms.TimeField(
        label="End Time*",
        widget=forms.TimeInput(attrs={
            'class': 'form-control',
            'type': 'time',
            'id': 'exampleInputText05'
        })
    )
    
    about_work = forms.CharField(
        label="About Work",
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 2,
            'id': 'exampleInputText040'
        })
    )
    
    agree_to_terms = forms.BooleanField(
        label="I agree to the terms and conditions.",
        widget=forms.CheckboxInput(attrs={
            'id': 'termsCheckbox'
        })
    )

    def __init__(self, *args, **kwargs):
        service_choices = kwargs.pop('service_choices', [])
        super().__init__(*args, **kwargs)
        self.fields['service_type'].choices = service_choices

    

    class Meta:
        model = BookingRequest
        fields = ['client_name', 'booking_date', 'service_type', 'start_time', 'end_time', 'about_work', 'agree_to_terms']
