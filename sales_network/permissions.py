from rest_framework import permissions


class IfUserEmployee(permissions.BasePermission):

    def get_permission(self, user_obj, perm, obj=None):
        return user_obj.user.is_employee
