from django.core.mail import send_mail
from django.shortcuts import render, redirect,get_object_or_404
from .forms import ReservationForm
from django.contrib import messages
from .models import Chef
from .models import Event
from django.utils import timezone
from .forms import TicketBookingForm
from django.conf import settings
from .forms import FeedbackForm
from .models import Feedback



def index(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your feedback!')
            return redirect('index')
    else:
        form = FeedbackForm()

    upcoming_events = Event.objects.filter(date__gt=timezone.now()).order_by('date')[:5]
    recent_feedbacks = Feedback.objects.all().order_by('-created_at')[:5]

    context = {
        'upcoming_events': upcoming_events,
        'form': form,
        'feedbacks': recent_feedbacks,
    }
    return render(request, 'index.html', context)




def about(request):
    return render(request, 'about.html')        

def starter(request):
    return render(request, 'starter.html')

def maincourse(request):
    return render(request, 'maincourse.html')        

def deserts(request):
    return render(request, 'deserts.html')        

def drinks(request):
    return render(request, 'drinks.html')        


   


def reservation_view(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save()
            try:
                send_mail(
                    'Reservation Confirmation',
                    f"Dear {reservation.name},\n\nYour reservation for {reservation.persons} person(s) on {reservation.date} at {reservation.time} has been confirmed.\n\nThank you!",
                    'mehtaraj048@gmail.com',  # Replace with your email
                    [reservation.email],
                    fail_silently=False,
                )
                messages.success(request, 'Your reservation has been confirmed. A confirmation email has been sent.')
            except Exception as e:
                messages.warning(request, 'Your reservation has been confirmed, but there was an issue sending the confirmation email.')
            return redirect('reservation')  # Redirect back to the reservation page
    else:
        form = ReservationForm()

    return render(request, 'reservation.html', {'form': form})





def our_chefs(request):
    chefs = Chef.objects.all()
    return render(request, 'our_chefs.html', {'chefs': chefs})    




def book_ticket(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == 'POST':
        form = TicketBookingForm(request.POST)
        if form.is_valid():
            # Get user data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            # Send confirmation email
            send_mail(
                'Ticket Booking Confirmation',
                f'Hello {name},\n\nYour ticket for the event "{event.title}" on {event.date} has been successfully booked.Show this ticket to get the entry pass of our event.Thank you!!!!',
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )

            # Redirect to a success page or display success message
            return render(request, 'booking_success.html', {'event': event, 'name': name})

    else:
        form = TicketBookingForm()

    return render(request, 'book_ticket.html', {'form': form, 'event': event})
