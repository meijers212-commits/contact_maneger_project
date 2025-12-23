from fastapi import FastAPI
from pybantic import BaseModel
from typing import Optional


class Contact(BaseModel):
    id: int 
    firest_name: str
    last_name: str
    phone: str


app = FastAPI()



@app.get("/contacts")
def get_all_contacts():
    pass


@app.get("/contacts/{contact_id}")
def get_contact(contact_id: int):
    pass

@app.post("/contacts")
def create_contact(contact: BaseModel):
    new_contact = {"first_name": "John","last_name": "Doe","phone_number": "050-1234567"}
        
    return {"message": "Contact created successfully","contact id": new_contact["id"]}


@app.put("/contacts/{contact_id}")
def update_contact(contact_id: int, contact: BaseModel):
    pass

@app.delete("/contacts/{contact_id}")
def delete_contact(contact_id: int):
    pass


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)