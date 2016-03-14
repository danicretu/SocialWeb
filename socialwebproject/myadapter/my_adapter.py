from allauth.account.models import EmailAddress
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

class MyAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        """
        Invoked just after a user successfully authenticates via a
        social provider, but before the login is actually processed
        (and before the pre_social_login signal is emitted).

        We're trying to solve different use cases:
        - social account already exists, just go on
        - social account has no email or email is unknown, just go on
        - social account's email exists, link social account to existing user
        """

        # Ignore existing social accounts, just do this stuff for new ones
        if sociallogin.is_existing:
            return
        if 'email' in sociallogin.account.extra_data:
            try:
                email = sociallogin.account.extra_data['email'].lower()
                email_address = EmailAddress.objects.get(email__iexact=email)
            except EmailAddress.DoesNotExist:
                return
        elif 'email-address' in sociallogin.account.extra_data:
            try:
                email = sociallogin.account.extra_data['email-address'].lower()
                email_address = EmailAddress.objects.get(email__iexact=email)
            except EmailAddress.DoesNotExist:
                return
        else:
            return

        # if it does, connect this new social login to the existing user
        user = email_address.user
        sociallogin.connect(request, user)