from rest_framework.permissions import BasePermission

class VenderCrud(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if request.method in  ['POST'] and request.user.user_type not in ['Admin']:
            return False
        else :
            return True
        
    def has_object_permission(self, request, view, obj):
        requested_user = request.user
        if requested_user.user_type == 'Admin':
            return True
        
        elif requested_user.vender_useraccount.pk == obj.pk:
            return True
        
        else:
            return False
    
        
    