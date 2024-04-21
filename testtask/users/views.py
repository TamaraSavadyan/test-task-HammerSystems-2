from django.http import JsonResponse
from django.views.generic import View
from .models import UserProfile
from .utils import generate_auth_code, validate_phone_number

class UserRegistrationView(View):
    def post(self, request):
        phone_number = request.POST.get('phone_number')

        if not validate_phone_number(phone_number):
            return JsonResponse({'error': f'Invalid phone number {phone_number}'}, status=400)
        
        '''
        Valid formats 
        +79896765432
        86783456732
        +1 987 123 65 43
        9-909-900-90-90
        8 (495) 678 32 32
        '''

        auth_code = generate_auth_code()

        user_profile = UserProfile.objects.create(
            phone_number=phone_number, auth_code=auth_code
        )

        return JsonResponse({'message': f'User {user_profile} registered successfully'}, status=201)
