from uuid import uuid4


class Hid:
    """Generate `Homemade` Universal Unique Identifier"""

    def __init__(self, prefix):
        self.prefix = prefix

    def __call__(self):
        return f"{self.prefix}{uuid4().hex}"
