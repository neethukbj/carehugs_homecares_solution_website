from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages 
from django.core.paginator import Paginator


from .models import *
from .forms import BookingForm
import datetime

#################
#Provider Detail
#################


def providerdetail(request, provider_id):
    provider = get_object_or_404(Provider, id=provider_id)
    service_choices = [(service.id, service.name) for service in provider.service_types.all()]
    user_profile = UserProfile.objects.get(user=request.user)
    user_profile_id = request.session.get('user_profile_id')    
    clientx = Client.objects.get(user_profile_id=user_profile_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, service_choices=service_choices)
        
        if form.is_valid():
            booking = BookingRequest(
                provider=provider,
                client_name=request.user,
                booking_date=form.cleaned_data['booking_date'],
                service_type=ServiceType.objects.get(id=form.cleaned_data['service_type']),
                start_time=form.cleaned_data['start_time'],
                end_time=form.cleaned_data['end_time'],
                about_work=form.cleaned_data['about_work'],
            )
            booking.save()
            # Redirect to the provider's page or a success page
            return redirect('notifications')
        else:
            print("error",form.errors)
    else:
        form = BookingForm(service_choices=service_choices)
    messages = Message.objects.filter(client=request.user)
    return render(request, 'home/providerdetail.html', {'clientx':clientx,'form': form, 'provider': provider,'messages':messages,"user_profile":user_profile})
 

#################
# Work Management
#################


def works(request): 
    user_profile_id = request.session.get('user_profile_id')    
    provider = Provider.objects.get(user_profile_id=user_profile_id)
    messages = Message.objects.filter(client=provider.user_profile.user).order_by('-created_at')   
    ongoing_bookings = BookingRequest.objects.filter(provider__user_profile__user=request.user, payment_status='Paid', is_completed=False)
    return render(request,'provider/works.html',{'provider': provider,"ongoing_bookings":ongoing_bookings,"messages":messages})

def complete_work(request, booking_id):
    booking = get_object_or_404(BookingRequest, id=booking_id)

    # Provider marks the work as completed
    booking.is_completed = True
    booking.status = 'Completed'
    booking.save()

    # Send a notification to the client
    Message.objects.create(
        client=booking.client_name,
        booking=booking,
        text=f"Your work for booking {booking.id} has been completed. Please confirm.",
        status='accepted'
    )

    messages.success(request, 'Work marked as completed. Notification sent to client.')
    return redirect('works')

def confirm_work(request, booking_id):
    booking = get_object_or_404(BookingRequest, id=booking_id)

    # Client confirms the work
    booking.is_confirmed = True
    booking.payment_status = 'Transferred'
    booking.save()

    # Notify the provider that payment has been transferred
    Message.objects.create(
        client=booking.provider.user_profile.user,
        booking=booking,
        text=f"Payment for booking {booking.id} has been transferred.",
        status='accepted'
    )

    messages.success(request, 'Work confirmed and payment transferred to provider.')
    return redirect('allproviders')


#################
# Provider Notifications
#################


def provider_notifications(request):
    user_profile_id = request.session.get('user_profile_id')    
    provider = Provider.objects.get(user_profile_id=user_profile_id)
    messages = Message.objects.filter(client=provider.user_profile.user).order_by('-created_at')
    # context = {
    #     'messages': messages
    # }
    #messages_list = Message.objects.filter(booking__provider__user_profile__user=request.user).order_by('-created_at')

    # Pagination (10 notifications per page)
    paginator = Paginator(messages, 10)
    page_number = request.GET.get('page')
    messages = paginator.get_page(page_number)

    context = {
        'messages': messages,
        #'messages_list':messages_list
    }
    return render(request,'provider/provider_notifications.html',context)



#################
#Booking Managament
#################


def booking_success_view(request):
    """
    View to display a success message after booking is successfully placed.
    """
    return HttpResponse("Your booking request has been sent successfully.")


@login_required
def bookings(request):
    user_profile_id = request.session.get('user_profile_id')
    
    if not user_profile_id:
        # Handle case where user_profile_id is missing
        return redirect('loginprovider')  # or another appropriate redirect
    
    try:
        provider = Provider.objects.get(user_profile_id=user_profile_id)
    except Provider.DoesNotExist:
        # Handle the case where the Provider does not exist
        return redirect('loginprovider')  # or another appropriate redirect

    # Handle booking actions
    if request.method == 'POST':
        booking_id = request.POST.get('booking_id')
        action = request.POST.get('action')
        booking = get_object_or_404(BookingRequest, id=booking_id)

        if action == 'accept':
            booking.status = 'Accepted'
            booking.save()

            message_text = f"Your booking for {booking.service_type.name} on {booking.booking_date} has been accepted!"
            payment_url = f"/payment/{booking.id}"  # Assuming there's a payment view that handles payments
            Message.objects.create(
                client=booking.client_name,
                booking=booking,
                provider=provider,
                text=message_text,
                status='accepted',
                payment_url=payment_url
            )
        elif action == 'reject':
            booking.status = 'Rejected'
            booking.save()
            message_text = f"Your booking for {booking.service_type.name} on {booking.booking_date} was rejected."
            Message.objects.create(
                client=booking.client_name,
                booking=booking,
                provider=provider,
                text=message_text,
                status='rejected'
            )
        return redirect('providerdashboard')
    today= datetime.date.today()
    upcoming_bookings = BookingRequest.objects.filter(
        provider=provider,
        status__in=['Pending'],  # Only show pending bookings
        booking_date__gte=datetime.date.today()  # Only show future bookings
    )

    # Fetch bookings for the provider
    bookings = BookingRequest.objects.filter(provider=provider)
    messages = Message.objects.filter(client=provider.user_profile.user).order_by('-created_at')
    return render(request, 'provider/page-task.html', {
        'provider': provider,
        'bookings': bookings,
        'upcoming_bookings':upcoming_bookings,
        'messages':messages,
    })



#################
# Client Notifications
#################


def notifications(request):
    
    messages = Message.objects.filter(client=request.user).order_by('-created_at')
    
    context = {
        'messages': messages
    }
    return render(request,'provider/notifications.html',context)


#################
# Payments List
#################


def payments(request):
    user_profile_id = request.session.get('user_profile_id')    
    provider = Provider.objects.get(user_profile_id=user_profile_id)
    messages = Message.objects.filter(client=provider.user_profile.user).order_by('-created_at') 
    transferred_payments = BookingRequest.objects.filter(provider__user_profile__user=request.user,payment_status='Transferred')
    return render(request,'provider/payments.html',{'provider': provider,"transferred_payments":transferred_payments,"messages":messages})

