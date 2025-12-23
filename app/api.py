from fastapi import FastAPI , APIrouter
from pybantic import BaseModel
from typing import Optional


class Contact(BaseModel):
    id: int 
    firest_name: str
    last_name: str
    phone: str

router = APIrouter()



@router.get("/contacts")
def get_all_contacts():
    pass


@router.get("/contacts/{contact_id}")
def get_contact(contact_id: int):
    pass

@router.post("/contacts")
def create_contact(contact: BaseModel):
    new_contact = {"first_name": "John","last_name": "Doe","phone_number": "050-1234567"}
        
    return {"message": "Contact created successfully","contact id": new_contact["id"]}


@router.put("/contacts/{contact_id}")
def update_contact(contact_id: int, contact: BaseModel):
    pass

@router.delete("/contacts/{contact_id}")
def delete_contact(contact_id: int):
    pass

