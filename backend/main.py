from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from email_service import send_email

app = FastAPI()

# Enable CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ProposalResponse(BaseModel):
    has_boyfriend: bool = None
    proposal_response: bool = None

@app.post("/api/has-boyfriend")
async def has_boyfriend(data: ProposalResponse):
    """Handle 'Do you have a boyfriend?' response"""
    if data.has_boyfriend:
        # Send email - she has a boyfriend
        email_body = """
        <h2>She Already Has a Boyfriend 💔</h2>
        <p>Unfortunately, she mentioned that she already has a boyfriend.</p>
        <p>Don't worry! There are many other amazing people out there. Keep your head up! 💪</p>
        """
        send_email(
            subject="Proposal Update: She Has a Boyfriend",
            body=email_body
        )
        return {"status": "rejected", "message": "She has already a boyfriend"}
    else:
        return {"status": "continue", "message": "Proceed to proposal"}

@app.post("/api/proposal-response")
async def proposal_response(data: ProposalResponse):
    """Handle final proposal response"""
    if data.proposal_response:
        # Send email - proposal accepted
        email_body = """
        <h2>Proposal Accepted! 🎉</h2>
        <p><strong>Congratulations!</strong> Your proposal has been accepted!</p>
        <p>She said YES! 💕</p>
        <p>This is the beginning of an amazing journey together. Enjoy this special moment!</p>
        <p style="margin-top: 20px;">
            <strong>With love,</strong><br/>
            Your Proposal App 💖
        </p>
        """
        send_email(
            subject="🎉 Proposal Accepted! 🎉",
            body=email_body
        )
        return {"status": "accepted", "message": "Proposal accepted!"}
    else:
        return {"status": "rejected", "message": "Proposal rejected"}

@app.get("/")
async def root():
    return {"message": "Proposal App Backend Running"}
