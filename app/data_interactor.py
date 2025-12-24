from connection import DB_Connection


class Datainteractor:

    @staticmethod
    def fetch_all_contacts():
        conn = DB_Connection.get_connection()
        if not conn:
            return []
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM contacts")
        results = cursor.fetchall()
        cursor.close()
        return results

    @staticmethod
    def fetch_contact_by_id(contact_id):
        conn = DB_Connection.get_connection()
        if not conn:
            return None
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM contacts WHERE id = %s", (contact_id,))
        result = cursor.fetchone()
        cursor.close()
        return result

    @staticmethod
    def add_contact(first_name, last_name, phone_number):
        conn = DB_Connection.get_connection()
        if not conn:
            return None
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO contacts (first_name, last_name, phone_number) VALUES (%s, %s, %s)",
            (first_name, last_name, phone_number),
        )
        conn.commit()
        contact_id = cursor.lastrowid
        cursor.close()
        return {"message": "Contact added successfully", "id": contact_id}

    @staticmethod
    def update_contact(contact_id, first_name, last_name, phone_number):
        conn = DB_Connection.get_connection()
        if not conn:
            return None
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE contacts SET first_name = %s, last_name = %s, phone_number = %s WHERE id = %s",
            (first_name, last_name, phone_number, contact_id),
        )
        conn.commit()
        cursor.close()
        return {"message": "Contact updated successfully", "id": contact_id}

    @staticmethod
    def delete_contact(contact_id):
        conn = DB_Connection.get_connection()
        if not conn:
            return None
        cursor = conn.cursor()
        cursor.execute("DELETE FROM contacts WHERE id = %s", (contact_id,))
        conn.commit()
        cursor.close()
        return {"message": "Contact deleted successfully", "id": contact_id}
