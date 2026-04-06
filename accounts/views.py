from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import UserProfile

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Return user profile details including remaining search credits
        and active subscription package.
        """
        profile, created = UserProfile.objects.get_or_create(user=request.user)
        
        return Response({
            'username': request.user.username,
            'email': request.user.email,
            'phone': profile.phone,
            'is_verified': profile.is_verified,
            'searches_left': profile.searches_left,
            'leads_scraped': profile.leads_scraped,
            'package': {
                'name': profile.package.name if profile.package else "No Package",
                'is_active': True if profile.package else False,
                'lead_limit': profile.package.lead_limit if profile.package else 0,
            } if profile.package else None,
            'joined_at': request.user.date_joined,
        })
