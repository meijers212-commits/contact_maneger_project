from fastapi import FastAPI, APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from nir_project import Contact_for_nir
from data_interactor import Datainteractor


class Contact(BaseModel):
    id: Optional[int] = None
    first_name: str
    last_name: str
    phone_number: str


router = APIRouter()


@router.get("/contacts")
def get_all_contacts():
    try:
        return Datainteractor.fetch_all_contacts()
    except Exception as error:
        raise HTTPException(status_code=400, detail=error)


@router.get("/contacts/{contact_id}")
def get_contact(contact_id: int):
    try:
        return Datainteractor.fetch_contact_by_id(contact_id)
    except Exception as error:
        raise HTTPException(status_code=400, detail=error)


@router.post("/contacts")
def create_contact(contact: Contact):
    try:
        d = Contact_for_nir.convert_to_dict(
            contact.first_name, contact.last_name, contact.phone_number
        )
        return Datainteractor.add_contact(
            d["first_name"], d["last_name"], d["phone_number"]
        )
    except Exception as error:
        raise HTTPException(status_code=400, detail=error)


@router.put("/contacts/{contact_id}")
def update_contact(contact_id: int, contact: Contact):
    try:
        d = Contact_for_nir.convert_to_dict(
            contact_id, contact.first_name, contact.last_name, contact.phone_number
        )
        return Datainteractor.update_contact(
            contact_id, d["first_name"], d["last_name"], d["phone_number"]
        )
    except Exception as error:
        raise HTTPException(status_code=400, detail=error)


@router.delete("/contacts/{contact_id}")
def delete_contact(contact_id: int):
    try:
        return Datainteractor.delete_contact(contact_id)
    except Exception as error:
        raise HTTPException(status_code=400, detail=error)
