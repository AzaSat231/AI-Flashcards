from fastapi import APIRouter, HTTPException
from app.models.flashcard import GenerateRequest, GenerateResponse
from app.services.flashcard_service import generate_flashcards

router = APIRouter()


@router.post("/generate", response_model=GenerateResponse, status_code=200)
async def generate(payload: GenerateRequest):
    """
    SCRUM-10: POST /generate

    Accepts { text } from the frontend and returns a list of flashcards.

    Request body:
        text       (str, required)  — lecture notes to process
        num_cards  (int, optional)  — how many cards to generate (default: 10)

    Returns:
        flashcards  — list of { id, front, back, topic }
        total       — number of cards generated
        source_length — character count of the input
    """
    try:
        cards = generate_flashcards(payload.text, payload.num_cards)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Generation failed: {str(e)}")

    return GenerateResponse(
        flashcards=cards,
        total=len(cards),
        source_length=len(payload.text),
    )