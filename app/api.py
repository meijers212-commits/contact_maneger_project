from fastapi import FastAPI , APIRouter
from pydantic import BaseModel
from typing import Optional
from sql.database import get_connection
from data_interactor import Datainteractor as d


class Contact(BaseModel): 
    id : Optional[int] = None
    firest_name: str
    last_name: str
    phone: str

router = APIRouter()



@router.get("/contacts")
def get_all_contacts():
    return d.fetch_all_contacts()

@router.get("/contacts/{contact_id}")
def get_contact(contact_id: int):
    return d.fetch_contact_by_id(contact_id)


@router.post("/contacts")
def create_contact(contact: Contact):
    return d.add_contact(contact.firest_name, contact.last_name, contact.phone)
    

@router.put("/contacts/{contact_id}")
def update_contact(contact_id: int, contact: Contact):
    return d.update_contact(contact_id, contact.firest_name, contact.last_name, contact.phone)

@router.delete("/contacts/{contact_id}")
def delete_contact(contact_id: int):
    return d.delete_contact(contact_id)

