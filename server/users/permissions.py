from rest_framework.permissions import BasePermission
from .models import Auth_STATUS


class IsVerifyPermission(BasePermission):

    def has_permission(self, request, view):
        if not hasattr(request, "auth") or request.auth is None:
            return False

        token_type = request.auth.get("token_type")

        return token_type == "verify"


class CodeVerifyPermission(BasePermission):

    def has_permission(self, request, view):
        if not hasattr(request, "auth") or request.auth is None:
            return False

        current_step = request.auth.get("current_step")

        return current_step == Auth_STATUS.VERIFY_CODE


class EditPasswordPermission(BasePermission):

    def has_permission(self, request, view):
        if not hasattr(request, "auth") or request.auth is None:
            return False

        current_step = request.auth.get("current_step")

        return current_step == Auth_STATUS.EDIT_PASSWORD


class EditEmailPermissions(BasePermission):

    def has_permission(self, request, view):

        if not hasattr(request, "auth") or request.auth is None:
            return False

        token_type = request.auth.get("token_type")

        return token_type == "email"
