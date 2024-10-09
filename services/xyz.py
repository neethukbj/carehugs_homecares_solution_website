from services.models import Booking
bookings = Booking.objects.filter(client_name='rewtet')
print(bookings)
