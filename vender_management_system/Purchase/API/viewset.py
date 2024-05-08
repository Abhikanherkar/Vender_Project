from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from Purchase.permission import PurchasePermission
from Purchase.API.serializer import PurchaseCreateSerilizer, PurchaseListSerilizer, PrchaseStatusLogSerializer
from Purchase.models import Purchase, PurchaseStatusLog


class PrchaseViewset(ModelViewSet):
    serializer_class = PurchaseCreateSerilizer
    queryset = Purchase.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['vendor']
    permission_classes = [IsAuthenticated]

    def get_serializer_class (self, *args, **kwargs):
        print(self.action)
        serializer_class = PurchaseCreateSerilizer

        if self.action == 'create':
            return  PurchaseCreateSerilizer

        elif self.action in ['list', 'retrieve']:
            return PurchaseListSerilizer        

    def get_queryset(self):
        queryset = None
        requested_user = self.request.user
        if requested_user.user_type == 'Admin':
            queryset = Purchase.objects.all().order_by('-id')

        elif requested_user.user_type == 'Vender':
            queryset = Purchase.objects.filter(vendor = requested_user.vender_useraccount).order_by('-id')

        return queryset
    

        
class PurchseStatusLog(ModelViewSet):
    serializer_class = PrchaseStatusLogSerializer
    queryset = PurchaseStatusLog.objects.all()
    permission_classes = [IsAuthenticated]
