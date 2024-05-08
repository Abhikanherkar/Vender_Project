from rest_framework.permissions import BasePermission


class PurchasePermission(BasePermission):
    message = 'You do not have permission to perform this action.'
    def has_permission(self, request, view):
        requested_user = request.user
        if requested_user.user_type == 'Admin' and request.method in ['GET', 'POST']:
            return True
        
        elif requested_user.user_type == 'Vender' and request.method in ['GET', 'POST', 'PATCH']:
            return True
        
    def has_object_permission(self, request, view, obj):
        requested_user = request.user
        if request.method == 'PATCH' and obj.acknowledgment_date:
            self.message = "Order has been already aknoledged."
            return False

        if (obj.vendor.user == requested_user and request.method in ['GET', 'PATCH']) or (requested_user.user_type == 'Admin' and request.method in ['GET',]):
            return True
        