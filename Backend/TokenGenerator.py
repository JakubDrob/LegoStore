import jwt
from datetime import datetime, timedelta, timezone

class TokenGenerator:
    def encode_token(user_id):
        """
        The encode_token function takes in a user object and returns a token
        """

        payload = {
            "exp": datetime.now(timezone.utc) + timedelta(days=1),
            "id": str(user_id),
        }
        token = jwt.encode(payload, "this is a secret key", algorithm="HS256")
        return token

    @staticmethod
    def decode_token(token):
        """
        It takes a token, decodes it, and returns the decoded token

        :param token: The token to decode
        :return: A dictionary with the user's id and username.
        """
        return jwt.decode(
            token,
            os.environ.get("SECRET_KEY"),
            algorithms="HS256",
            options={"require_exp": True},
        )

    @staticmethod
    def check_token(token):
        """
        It takes a token, and returns True if the token is valid, and False if it's not

        :param token: The token to be decoded
        :return: A boolean value.
        """
        try:
            jwt.decode(
                token,
                os.environ.get("SECRET_KEY"),
                algorithms="HS256",
                options={"require_exp": True},
            )
            return True
        except:
            return False

    @staticmethod
    def get_user_id(token):
        """
        It decodes the token, and returns the user's id

        :param token: The token that was sent to the server
        :return: The user id is being returned.
        """
        data = jwt.decode(
            token,
            os.environ.get("SECRET_KEY"),
            algorithms="HS256",
            options={"require_exp": True},
        )
        return data["id"]


token_generator = TokenGenerator()
