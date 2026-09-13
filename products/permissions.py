from rest_framework.permissions import BasePermission

class GetForUser(BasePermission):
    def has_permission(self, request, view):
        if request.method in ["GET", "HEAD", "OPTIONS"]:
            return True
        return request.user.is_staff

#       ----EXPLICACION---- 

# from rest_framework.permissions import BasePermission
# Importa la clase base que utilizamos para crear permisos personalizados.

# class GetForUser(BasePermission):
# Crea nuestro propio permiso personalizado.

# def has_permission(self, request, view):
# DRF ejecuta este método para decidir si la petición tiene permiso.

# if request.method in ["GET", "HEAD", "OPTIONS"]:
   # return True
# Permite las peticiones de lectura.
# GET  → consultar
# HEAD → consultar información de la respuesta
# OPTIONS → consultar las opciones del endpoint

# return request.user.is_staff
# Si no es una petición de lectura, comprueba si el usuario es staff.
# True  → puede continuar
# False → DRF rechaza la petición