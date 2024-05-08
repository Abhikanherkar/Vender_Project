from datetime import datetime
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from Purchase.models import Purchase, PurchaseStatusLog


class PurchaseCreateSerilizer(ModelSerializer):
    '''This serializer is used to place a purchase order as vender and admin'''

    class Meta:
        model = Purchase
        fields = ['id', 'po_number', 'vendor', 'order_date', 'delivery_date', 'items', 'quantity']

    def validate_delivery_date(self, delivery_date):
        if not delivery_date.date() > datetime.now().date():
            raise serializers.ValidationError(detail={"Error":"delivery_date should be from future."})

        return delivery_date


class PurchaseListSerilizer(ModelSerializer):
    '''This serializer is used to get the list and detail of the puchase orders'''
    class Meta:
        model = Purchase
        fields = '__all__'


class AknowledgedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = ['acknowledgment_date', 'status']


class PrchaseStatusLogSerializer(serializers.ModelSerializer):
    '''This serializer is used to store the status update logs related to the purchase order'''
    class Meta:
        model = PurchaseStatusLog
        fields = '__all__'

    def validate(self, attrs):
        purchase_instance = attrs.get('prchase_id')
        status = attrs.get('status')

        if self.context['request'].user.user_type == 'Vender' and purchase_instance.vendor.user != self.context['request'].user:
            raise serializers.ValidationError({'Detail':"You cannot update the status of the order ass this order is not belongs to you."})

        if purchase_instance.status == status:
            raise serializers.ValidationError(detail={"Status":f'Purchase order status is already updated to {status}.'})
        
        if purchase_instance.status == 'Pending' and status not in ['Aknowledged', 'Canceled']:
            raise serializers.ValidationError({'Status':f"You can only Aknowledged or canccell this order."})
        
        if purchase_instance.status == 'Canceled':
            raise serializers.ValidationError({'Status':"Cant update status of cancelled order."})
        
        if purchase_instance.status == 'Aknowledged' and status != 'Completed':
            raise serializers.ValidationError({'Status':'You can only complete the order now.'})

        return attrs
    
    def create(self, validated_data):
        instance = super().create(validated_data)

        order_instance = instance.prchase_id

        order_instance.status = instance.status
        if instance.status == 'Aknowledged':
            order_instance.acknowledgment_date = datetime.now()
            
        order_instance.save()
        return instance



