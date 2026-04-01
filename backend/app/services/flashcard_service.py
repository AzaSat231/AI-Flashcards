"""
Flashcard generation service.
Currently returns stub data — will be replaced with AI (Claude/OpenAI) integration.
"""
from typing import List
from app.models.flashcard import Flashcard


def generate_flashcards(text: str, num_cards: int = 10) -> List[Flashcard]:
    """
    Generate flashcards from the provided text.

    Args:
        text: The lecture notes / study material.
        num_cards: How many flashcards to produce.

    Returns:
        A list of Flashcard objects.

    TODO: Replace stub logic with AI model call (Llama model).
    """
    # --- STUB: return placeholder cards until AI is wired up ---
    stub_cards = [
        Flashcard(
            id=i + 1,
            front=f"Key concept #{i + 1} from your notes",
            back=f"Explanation #{i + 1} — AI-generated answer will appear here.",
            topic="General",
        )
        for i in range(min(num_cards, 5))  # cap stub at 5
    ]
    return stub_cards