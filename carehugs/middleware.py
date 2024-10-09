from django.conf import settings
from django.contrib.sessions.middleware import SessionMiddleware

class AdminSessionMiddleware(SessionMiddleware):
    def process_request(self, request):
        # Check if user is accessing the admin site
        if request.path.startswith('/admin/'):
            # Use a different session key for admin users
            request.session_engine = 'django.contrib.sessions.backends.db'
        else:
            # Use the default session key for frontend users
            request.session_engine = settings.SESSION_ENGINE
        super(AdminSessionMiddleware, self).process_request(request)

    def process_response(self, request, response):
        # Ensure the response is processed based on session type
        response = super(AdminSessionMiddleware, self).process_response(request, response)
        return response


