from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import generate

app = FastAPI(
    title="AI Flashcard Generator",
    description="Convert lecture notes into interactive flashcards using AI",
    version="1.0.0",
)

# CORS — allow frontend dev server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(generate.router, prefix="/api", tags=["generate"])


@app.get("/")
async def root():
    return {"message": "AI Flashcard Generator API", "status": "running"}


@app.get("/health")
async def health():
    print("Hello")
    return {"status": "ok"}