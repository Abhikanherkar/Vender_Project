from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from Vender.API.serializer import VenderSerializer, VenderListSerializer
from Vender.API.serializer import CustomTokenObtainSerializer
from Vender.models import Vender


class CustomTokenViewset(TokenObtainPairView):
    """
    Takes a set of user credentials and returns an access and refresh JSON web
    token pair to prove the authentication of those credentials.
    """

    serializer_class = CustomTokenObtainSerializer

class VenderCreateViewset(ModelViewSet):
    serializer_class = VenderSerializer
    permission_classes = [IsAuthenticated]
    queryset = Vender.objects.all().order_by('-id')
    
    def get_serializer_class(self):
    
        serilizer_class = None
        if self.action == 'create':
            serilizer_class = VenderSerializer

        elif self.action in  ['list', 'retrieve', 'update']:
            serilizer_class = VenderListSerializer

        return serilizer_class
    
    def get_queryset(self):
        queryset = None

        # SA can perform crud operation on all the venders
        if self.request.user.user_type == 'Admin':
            queryset = Vender.objects.all()
        
        else:
            queryset = Vender.objects.filter(user = self.request.user)

        return queryset
    

    def perform_destroy(self, instance):
        # delete the user account incase of vender instance delete operation
        user_instance = instance.user
        user_instance.delete()
        instance.delete()
