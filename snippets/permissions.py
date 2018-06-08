from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    ''' Custom permission to only allow owners of an object to edit it
    '''

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowerd to any request
        # so we'll always GET, HEAD OR OPTIONS request
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permission are only allower to the owner of the snippets
        return obj.owner == request.user
