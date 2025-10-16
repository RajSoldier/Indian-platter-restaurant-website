from django import forms
from .models import Reservation
from .models import Feedback

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'email', 'phone', 'persons', 'date', 'time', 'message']

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your full name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email address'}),  # Removed default
            'phone': forms.TextInput(attrs={'placeholder': 'Enter your phone number'}),
            'persons': forms.NumberInput(attrs={'min': 1}),
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'message': forms.Textarea(attrs={'placeholder': 'Leave a special message (optional)', 'rows': 3}),
        }

    # Set default value for the email field using 'initial'
    def __init__(self, *args, **kwargs):
        super(ReservationForm, self).__init__(*args, **kwargs)
        self.fields['email'].initial = 'example@example.com'


class TicketBookingForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()



class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['message', 'recommendation']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Please share your thoughts...'}),
            'recommendation': forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')])
        }
        labels = {
            'recommendation': 'Would you recommend us to others?'
        }    