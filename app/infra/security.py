import bcrypt


class Security:
    def hashed(self, password: str):
        salt = bcrypt.gensalt()
        hash = bcrypt.hashpw(password.encode("utf-8"), salt)
        return hash.decode("utf-8")

    def check_hash(self, hashed: str, password: str):
        return bcrypt.checkpw(password.encode("utf-8"), hashed.encode("utf-8"))
