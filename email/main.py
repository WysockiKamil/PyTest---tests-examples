from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from email_validator import validate_email, EmailNotValidError

app = FastAPI()

class EmailRequest(BaseModel):
    email: str

@app.post("/validate-email")
def validate_email_endpoint(data: EmailRequest):
    try:
        validate_email(data.email)
        return {"email": data.email, "valid": True}
    except EmailNotValidError as e:
        raise HTTPException(status_code=400, detail=str(e))