class OneLogin_Saml2_Settings:
    def __init__(
        self,
        settings: dict[str, object] | None = None,
        custom_base_path: str | None = None,
        sp_validation_only: bool | None = None,
    ) -> None: ...
    def get_sp_metadata(self) -> bytes | str: ...
    def validate_metadata(self, xml: bytes | str) -> list[str]: ...
