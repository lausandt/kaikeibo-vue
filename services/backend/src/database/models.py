from decimal import Decimal
from typing import Any

from tortoise.fields import data, relational
from tortoise.models import Model


class User(Model):
    """
    The User model
    """

    id: int = data.IntField(pk=True)
    email: str = data.CharField(max_length=50, unique=True)
    name: str | None = data.CharField(max_length=50, null=True, default=None)
    family_name: str | None = data.CharField(
        max_length=50, null=True, default=None
    )
    password_hash: str = data.CharField(max_length=128)
    created_at = data.DatetimeField(auto_now_add=True)
    modified_at = data.DatetimeField(auto_now=True)
    is_active = data.BooleanField(default=True)
    is_superuser = data.BooleanField(default=False)

    def full_name(self) -> str:
        """
        Returns the best name
        """
        if self.name or self.family_name:
            return f"{self.name or ''} {self.family_name or ''}".strip()
        return self.email

    class PydanticMeta:
        computed = ["full_name"]
        exclude = ["password_hash"]

class Entry(Model):

    id: int = data.IntField(pk=True)
    title: str = data.CharField(max_length=225)
    amount: Decimal = data.DecimalField(max_digits=20, decimal_places=2)
    description: str = data.TextField()
    supplier: str | None = data.CharField(max_length=255, null=True)
    interval: str = data.CharField(max_length=225)
    created_at: Any = data.DatetimeField(auto_now_add=True)
    url: str = data.CharField(max_length=225)
    author = relational.ForeignKeyField("models.User", related_name="note")



