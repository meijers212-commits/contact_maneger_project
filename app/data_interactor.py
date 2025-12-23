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
