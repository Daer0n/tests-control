from dataclasses import dataclass
from shared.shared import ExerciseLevel, ExerciseTopic


@dataclass(frozen=True)
class GetUserFilter:
    id: int | None = None
    name: str | None = None

@dataclass(frozen=True)
class PatchUserFilter:
    id: int
    name: str | None = None
    password: str | None = None

@dataclass(frozen=True)
class GetExerciseFilter:
    theme: ExerciseTopic
    level: ExerciseLevel