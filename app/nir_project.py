from typing import Optional
from pydantic import BaseModel

class Contact_for_nir(BaseModel):
    id: Optional[int] = None
    first_name: str
    last_name: str
    phone_number: str

    def convert_to_dict(id,first_name,last_name,phone_number):
        d = {"id":id,"first_name":first_name,"last_name":last_name,"phone_number":phone_number}
        return d