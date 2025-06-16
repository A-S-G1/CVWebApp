from django import forms

class FeedbackForm(forms.Form):
    # CharField for the sender's name
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400',
            'placeholder': 'Your Name'
        })
    )
    # EmailField for the sender's email address
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400',
            'placeholder': 'Your Email'
        })
    )
    # TextField for the message body
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400 h-32 resize-y',
            'placeholder': 'Your Message or Work Offer'
        }),
        max_length=1000
    )

    # ChoiceField to distinguish between general feedback and work offers
    subject_type = forms.ChoiceField(
        choices=[
            ('feedback', 'General Feedback'),
            ('offer', 'Work Offer')
        ],
        widget=forms.RadioSelect(attrs={
            'class': 'form-radio text-blue-600 ml-2' # Tailwind/custom class for radio buttons
        }),
        initial='feedback' # Default selection
    )
