from dataclasses import dataclass


@dataclass(frozen=True)
class GetUserFilter:
    id: int | None = None
    name: str | None = None

@dataclass(frozen=True)
class PatchUserFilter:
    id: int
    name: str | None = None
    password: str | None = None