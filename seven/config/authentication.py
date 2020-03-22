from rest_framework.authentication import TokenAuthentication


class MyTokenAuthentication(TokenAuthentication):

    def get_model(self):
        if self.model is not None:
            return self.model
        from apps.user.models import Token
        return Token
