from ..sql.database import get_connection

def get_contacts():
    conn = get_connection()
    if not conn:
        return []
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM contacts")
    results = cursor.fetchall()
    conn.close()
    return results

class Datainteractor:
    def __init__(self):
        self.connection = get_connection()

    def fetch_all_contacts(self):
        if not self.connection:
            return []
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM contacts")
        results = cursor.fetchall()
        cursor.close()
        return results

    def fetch_contact_by_id(self, contact_id):
        if not self.connection:
            return None
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM contacts WHERE id = %s", (contact_id,))
        result = cursor.fetchone()
        cursor.close()
        return result

    def add_contact(self, first_name, last_name, phone):
        if not self.connection:
            return None
        cursor = self.connection.cursor()
        cursor.execute(
            "INSERT INTO contacts (first_name, last_name, phone_number) VALUES (%s, %s, %s)",
            (first_name, last_name, phone)
        )
        self.connection.commit()
        contact_id = cursor.lastrowid
        cursor.close()
        return {"message": "Contact added successfully", "id": contact_id}
    
    def update_contact(self, contact_id, first_name, last_name, phone):
        if not self.connection:
            return None
        cursor = self.connection.cursor()
        cursor.execute(
            "UPDATE contacts SET first_name = %s, last_name = %s, phone_number = %s WHERE id = %s",
            (first_name, last_name, phone, contact_id)
        )
        self.connection.commit()
        cursor.close()
        return {"message": "Contact updated successfully" , "id": contact_id}
    
    def delete_contact(self, contact_id):
        if not self.connection:
            return None
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM contacts WHERE id = %s", (contact_id,))
        self.connection.commit()
        cursor.close()
        return {"message": "Contact deleted successfully" , "id": contact_id}
    
    def close_connection(self):
        if self.connection:
            self.connection.close()