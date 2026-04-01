# AI Flashcard Generator

> Convert lecture notes into interactive flashcards using AI — with spaced repetition and progress tracking.

## Project Structure

```
flashcard-app/
├── backend/          ← FastAPI (Python)
│   ├── app/
│   │   ├── main.py           # App entry point + CORS
│   │   ├── routers/
│   │   │   └── generate.py   # POST /api/generate  (SCRUM-10)
│   │   ├── models/
│   │   │   └── flashcard.py  # Pydantic request/response schemas
│   │   └── services/
│   │       └── flashcard_service.py  # Generation logic (stub → AI)
│   ├── requirements.txt
│   ├── .env.example
│   └── run.py
└── frontend/         ← (coming soon)
```

## Backend Setup

### 1. Install dependencies
```bash
cd backend
pip install -r requirements.txt
```

### 2. Configure environment
```bash
cp .env.example .env
# Edit .env with your API keys
```

### 3. Run the server
```bash
python run.py
# Server starts at http://localhost:8000
```

### 4. Explore the API
- Swagger UI: http://localhost:8000/docs
- ReDoc:       http://localhost:8000/redoc
- Health:      http://localhost:8000/health

## API Endpoints

### `POST /api/generate`
Convert text notes into flashcards.

**Request**
```json
{
  "text": "Photosynthesis is the process by which...",
  "num_cards": 10
}
```

**Response**
```json
{
  "flashcards": [
    { "id": 1, "front": "What is photosynthesis?", "back": "...", "topic": "Biology" }
  ],
  "total": 10,
  "source_length": 342
}
```

## Jira Tickets Covered

| Ticket   | Description                                      | Status |
|----------|--------------------------------------------------|--------|
| SCRUM-9  | Initialize FastAPI project, run on localhost:8000 | ✅ Done |
| SCRUM-10 | POST /generate endpoint accepting `{ text }`     | ✅ Done |