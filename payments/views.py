import razorpay
from django.conf import settings
from django.shortcuts import render

def make_payment(request):
    # Razorpay client instance
    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

    # Payment amount (in paise, so multiply by 100)
    amount = 50000  # e.g., Rs 500

    # Create an order
    razorpay_order = client.order.create({
        "amount": amount,
        "currency": "INR",
        "payment_capture": "1"  # Auto capture payment after it is authorized
    })

    # Pass the order details and the API Key to the template
    context = {
        'razorpay_order_id': razorpay_order['id'],
        'razorpay_key': settings.RAZORPAY_KEY_ID,
        'amount': amount,
        'currency': 'INR',
    }

    return render(request, 'payment_page.html', context)

from django.http import JsonResponse
from django.conf import settings
import razorpay

def payment_success(request):
    if request.method == "POST":
        # Get payment details from Razorpay response
        payment_id = request.POST.get('razorpay_payment_id')
        order_id = request.POST.get('razorpay_order_id')
        signature = request.POST.get('razorpay_signature')

        # Verify the payment signature
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

        try:
            # Razorpay's signature verification
            params_dict = {
                'razorpay_order_id': order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
            client.utility.verify_payment_signature(params_dict)

            # Payment is successful
            # You can store the payment details in the database
            return JsonResponse({'status': 'Payment successful'})

        except razorpay.errors.SignatureVerificationError as e:
            # Signature verification failed
            return JsonResponse({'status': 'Payment failed'})
