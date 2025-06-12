from django.contrib.auth import get_user_model
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

@api_view(['DELETE'])
@permission_classes([permissions.IsAuthenticated])
def delete_user(request):
    user = request.user
    user.delete()
    return Response({"detail": "User account deleted."}, status=status.HTTP_204_NO_CONTENT)