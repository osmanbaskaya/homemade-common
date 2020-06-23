from enum import Enum
from uuid import uuid4

from pydantic import BaseModel


class Categories(Enum):
    PANTRY_ITEM = "PI"
    PANTRY = "PA"
    ITEM = "IT"
    STORE = "ST"
    ITEM_CATEGORY = "IC"
    BRAND = "BR"


class Hid(BaseModel):
    """Generate `Homemade` Universal Unique Identifier"""

    uid_type: Categories

    class Config:
        allow_mutation = False

    def generate(self):
        return f"{self.uid_type.value}{uuid4().hex}"


PantryItemHid = Hid(uid_type=Categories.PANTRY_ITEM)
PantryHid = Hid(uid_type=Categories.PANTRY)
ItemHid = Hid(uid_type=Categories.ITEM)
StoreHid = Hid(uid_type=Categories.STORE)
ItemCategory = Hid(uid_type=Categories.ITEM_CATEGORY)
BrandHid = Hid(uid_type=Categories.BRAND)
