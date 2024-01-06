from typing import Tuple
from .personalization import Personalization as Personalization

class Mail:
    def __init__(self) -> None: ...
    def add_personalization(self, personalization: Personalization) -> None: ...
    @property
    def from_email(self) -> Tuple[str, str]: ...
    @from_email.setter
    def from_email(self, value: Tuple[str, str]) -> None: ...
    @property
    def reply_to(self) -> Tuple[str, str]: ...
    @reply_to.setter
    def reply_to(self, value: Tuple[str, str]) -> None: ...
    @property
    def template_id(self) -> str: ...
    @template_id.setter
    def template_id(self, value: str) -> None: ...
    def get(self) -> dict[str, object]: ...