from rest_framework import permissions

class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Verifica si el usuario es el propietario del objeto o si es un administrador
        return obj == request.user or request.user.is_staff
