from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect

class VerifiedUserMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_verified

    def handle_no_permission(self):
        return redirect('verify_account')