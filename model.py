from pydantic import BaseModel, Field

class DocumentInsert(BaseModel):
    conversation_id: str
    sql: str
    response_text: str
    rating: float = Field(..., ge=0.0, le=5.0, description="Rating from 0.0 to 5.0")
