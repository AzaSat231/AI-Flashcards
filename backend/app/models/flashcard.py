from pydantic import BaseModel, Field
from typing import List, Optional


class GenerateRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=10,
        max_length=50000,
        description="The lecture notes or text to generate flashcards from",
        example="Photosynthesis is the process by which plants convert sunlight into glucose...",
    )
    num_cards: Optional[int] = Field(
        default=10,
        ge=1,
        le=50,
        description="Number of flashcards to generate (1-50)",
    )


class Flashcard(BaseModel):
    id: int
    front: str = Field(description="The question or concept side of the flashcard")
    back: str = Field(description="The answer or explanation side of the flashcard")
    topic: Optional[str] = Field(default=None, description="Topic or category tag")


class GenerateResponse(BaseModel):
    flashcards: List[Flashcard]
    total: int
    source_length: int = Field(description="Character count of the input text")