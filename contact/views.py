from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings # To access EMAIL_BACKEND, DEFAULT_FROM_EMAIL etc.
from .forms import FeedbackForm

def feedback_form_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST) # Initialize form with POST data
        if form.is_valid():
            # Get cleaned data from the form
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject_type = form.cleaned_data['subject_type']

            # Determine email subject based on subject type
            subject_prefix = "Feedback" if subject_type == "feedback" else "Work Offer"
            full_subject = f"Portfolio - {subject_prefix} from {name} ({email})"
            
            # Construct the email body
            email_body = f"Name: {name}\n" \
                         f"Email: {email}\n" \
                         f"Type: {subject_type.replace('_', ' ').title()}\n" \
                         f"Message:\n{message}"

            try:
                # Send the email
                # The email will be printed to your Django server console if EMAIL_BACKEND is 'console.EmailBackend'
                send_mail(
                    full_subject, # Subject of the email
                    email_body,   # Body of the email
                    settings.DEFAULT_FROM_EMAIL, # Sender's email address (from settings.py)
                    [settings.DEFAULT_FROM_EMAIL], # Recipient's email address (your email)
                    fail_silently=False, # Raise an exception if email sending fails
                )
                # On successful sending, re-render the form with a success message
                return render(request, 'contact/feedback.html', {
                    'form': FeedbackForm(), # Provide a new, empty form
                    'success_message': 'Thank you for your message! I will get back to you shortly.'
                })
            except Exception as e:
                # Log any errors that occur during email sending
                print(f"Error sending email: {e}")
                # Re-render the form with an error message, preserving user input
                return render(request, 'contact/feedback.html', {
                    'form': form,
                    'error_message': 'There was an error sending your message. Please try again later.'
                })
        else:
            # If the form is not valid, re-render the form with validation errors
            return render(request, 'contact/feedback.html', {'form': form})
    else:
        form = FeedbackForm() # For GET requests, create an empty form
    return render(request, 'contact/feedback.html', {'form': form})
