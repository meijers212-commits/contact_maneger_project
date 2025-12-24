from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from typing import Optional
from data_interactor import Datainteractor


class Contact(BaseModel):
    id: Optional[int] = None
    first_name: str
    last_name: str
    phone_number: str


router = APIRouter()


@router.get("/contacts")
def get_all_contacts():
    return Datainteractor.fetch_all_contacts()


@router.get("/contacts/{contact_id}")
def get_contact(contact_id: int):
    return Datainteractor.fetch_contact_by_id(contact_id)


@router.post("/contacts")
def create_contact(contact: Contact):
    return Datainteractor.add_contact(
        contact.first_name, contact.last_name, contact.phone_number
    )


@router.put("/contacts/{contact_id}")
def update_contact(contact_id: int, contact: Contact):
    return Datainteractor.update_contact(
        contact_id, contact.first_name, contact.last_name, contact.phone_number
    )


@router.delete("/contacts/{contact_id}")
def delete_contact(contact_id: int):
    return Datainteractor.delete_contact(contact_id)
