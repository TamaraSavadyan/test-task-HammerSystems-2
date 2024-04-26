# from django.http import JsonResponse
# from django.views.generic import View
# from .models import InviteCode, UserProfile
# from .utils import generate_auth_code, validate_phone_number, generate_invite_code

# class UserRegistrationView(View):
#     def post(self, request):
#         phone_number = request.POST.get('phone_number')

#         if not validate_phone_number(phone_number):
#             return JsonResponse({'error': f'Invalid phone number {phone_number}'}, status=400)
        
#         user_profile = UserProfile.objects.get(phone_number=phone_number)

#         if user_profile:
#             return JsonResponse({'error': 'User with this phone number already exists'}, status=400)
      
        
#         '''
#         Valid formats 
#         +79896765432
#         86783456732
#         +1 987 123 65 43
#         9-909-900-90-90
#         8 (495) 678 32 32
#         '''

#         random_invite_code = generate_invite_code()

#         invite_code = InviteCode.objects.create(owner_code=random_invite_code)

#         auth_code = generate_auth_code()

#         user_profile = UserProfile.objects.create(
#             phone_number=phone_number, auth_code=auth_code, invite_code=invite_code
#         )

#         return JsonResponse({'message': f'User {user_profile} registered successfully'}, status=201)


# class UserAuthenticationView(View):
#     def post(self, request):
#         phone_number = request.POST.get('phone_number')
#         auth_code = request.POST.get('auth_code')

#         try:
#             user_profile = UserProfile.objects.get(phone_number=phone_number)

#             if auth_code == user_profile.auth_code:
#                 return JsonResponse({'message': 'Authentication successful'})
#             else:
#                 return JsonResponse({'error': 'Invalid authentication code'}, status=400)
            
#         except UserProfile.DoesNotExist:
#             return JsonResponse({'error': 'User does not exist'}, status=400)


from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .models import InviteCode, UserProfile
from .utils import generate_auth_code, validate_phone_number, generate_invite_code
from .serializers import UserAuthenticationSerializer, UserRegistrationSerializer
from django.shortcuts import get_object_or_404

class UserRegistrationViewSet(ViewSet):
    def create(self, request):
        phone_number = request.data.get('phone_number')

        serializer = UserRegistrationSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        if not validate_phone_number(phone_number):
            return Response({'error': f'Invalid phone number {phone_number}'}, status=status.HTTP_400_BAD_REQUEST)

        user_profile, created = UserProfile.objects.get_or_create(phone_number=phone_number)

        if not created:
            return Response({'error': f'User with this phone number {phone_number} already exists'}, status=status.HTTP_400_BAD_REQUEST)

        random_invite_code = generate_invite_code()
        invite_code = InviteCode.objects.create(owner_code=random_invite_code)
        auth_code = generate_auth_code()

        user_profile.auth_code = auth_code
        user_profile.invite_code = invite_code
        user_profile.save()

        return Response(user_profile, status=status.HTTP_201_CREATED)


class UserAuthenticationViewSet(ViewSet):
    def create(self, request):

        phone_number = request.data.get('phone_number')
        auth_code = request.data.get('auth_code')

        serializer = UserAuthenticationSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user_profile = get_object_or_404(UserProfile, phone_number=phone_number)

        if auth_code == user_profile.auth_code:
            user_profile.auth_code = None
            user_profile.save()
            return Response({'message': 'Authentication successful'})
        else:
            return Response({'error': 'Invalid authentication code'}, status=status.HTTP_400_BAD_REQUEST)


