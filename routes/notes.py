from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from database import notes_collection
from models import NoteCreate, NoteUpdate
from bson import ObjectId

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

# Homepage - List Notes
@router.get("/")
async def read_notes(request: Request):
    notes = list(notes_collection.find())
    return templates.TemplateResponse("index.html", {"request": request, "notes": notes})

# Create Note Page
@router.get("/create")
async def create_note_page(request: Request):
    return templates.TemplateResponse("create.html", {"request": request})

# Add a Note
@router.post("/create")
async def create_note(title: str = Form(...), content: str = Form(...)):
    note = {"title": title, "content": content}
    notes_collection.insert_one(note)
    return RedirectResponse("/", status_code=303)

# Update Note Page
@router.get("/update/{id}")
async def update_note_page(request: Request, id: str):
    note = notes_collection.find_one({"_id": ObjectId(id)})
    return templates.TemplateResponse("update.html", {"request": request, "note": note})

# Update a Note
@router.post("/update/{id}")
async def update_note(id: str, title: str = Form(None), content: str = Form(None)):
    updated_data = {"title": title, "content": content}
    notes_collection.update_one({"_id": ObjectId(id)}, {"$set": updated_data})
    return RedirectResponse("/", status_code=303)

# Delete a Note
@router.get("/delete/{id}")
async def delete_note(id: str):
    notes_collection.delete_one({"_id": ObjectId(id)})
    return RedirectResponse("/", status_code=303)
