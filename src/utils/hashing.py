from passlib.context import CryptContext

PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash:
    def bcrypt(password: str):
        return PWD_CONTEXT.hash(password)

    def verify(plain_password, hashed_password):
        return PWD_CONTEXT.verify(plain_password, hashed_password)
