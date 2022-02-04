from rest_framework import permissions


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        if hasattr(obj, 'seller'):
            return obj.seller == request.user.seller

        return False


#
# class IsOwner2(permissions.BasePermission):
#
#     def has_object_permission(self, request, view, obj):
#         data = list(obj)
#         data = ''.join(map(str, data))
#         data = data.split('::')
#         seller = ''
#         for i in data:
#             if i == request.user.seller:
#                 seller = i
#         return seller == request.user.seller




