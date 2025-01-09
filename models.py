from pydantic import BaseModel

class NoteCreate(BaseModel):
    title: str
    content: str

class NoteUpdate(BaseModel):
    title: str = None
    content: str = None
