from pydantic import BaseModel

from shared.shared import ExerciseLevel
from shared.shared import ExerciseTopic

class SaveUserDto(BaseModel):
    name: str
    role: str
    password: str

class SaveExerciseDto(BaseModel):
    theory: str
    theme: ExerciseTopic
    level: ExerciseLevel

class SaveQuestionDto(BaseModel):
    question_text: str
    exercise_id: int

class SaveAnswerDto(BaseModel):
    text: str
    is_correct: bool
    question_id: int