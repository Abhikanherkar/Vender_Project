from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from Vender.models import Vender, CustomUser


class CustomTokenObtainSerializer(TokenObtainPairSerializer):
    '''This serializer has been overrided to add custom fields in the user token so in future vender can place order for himself'''

    @classmethod
    def get_token(cls, user):

        token= super().get_token(user)
        token['user_type'] = user.user_type
        
        try:
            # For superuser created from CMD created without any vender account
            token['vendeer_id'] = user.vender_useraccount.pk
        except :
            pass

        return token


class CustomVenderSeriliaer(ModelSerializer):
    class Meta():
        model = CustomUser
        fields = ['id', 'email', 'password']

class VenderSerializer(ModelSerializer):
    '''This serilizer class is used to create vender as SA'''
    user = CustomVenderSeriliaer(many = False)
    class Meta:
        model = Vender
        fields = ['user', 'id', 'name', 'contact_details', 'address', 'vendor_code']

    def create(self, validated_data):
        # create user account for the user 
        data = validated_data.get('user')
        validate = CustomVenderSeriliaer(data=data)
        validate.is_valid()
        instance = validate.save()
        instance.set_password(data.get('password'))
        instance.is_active = True
        instance.is_staff = True
        instance.user_type = 'Vender'
        
        instance.save()
        
        validated_data['user'] = instance
        return super().create(validated_data)


class VenderListSerializer(ModelSerializer):
    '''This seriliser is used to list all the avaliable venders and get the details of tthe vender by giving vender id'''
    class Meta:
        model = Vender
        fields = '__all__' 