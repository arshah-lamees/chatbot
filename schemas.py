from pydantic import BaseModel

class UserMessage(BaseModel):
    message: str

class BotResponse(BaseModel):
    response: str 