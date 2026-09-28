import mysql.connector


class DonorListCreateRetrieveUpdateDelete:

    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="blood"
        )
        self.cursor = self.db.cursor()

    # 1. Read all donors
    def list(self):
        query = "SELECT * FROM donor"
        self.cursor.execute(query)
        return self.cursor.fetchall()


    def create(self, name, blood_group, phone, city, last_donation):
        query = """
        INSERT INTO donor
        (name, blood_group, phone, city, last_donation)
        VALUES (%s, %s, %s, %s, %s)
        """
        data = (name, blood_group, phone, city, last_donation)

        self.cursor.execute(query, data)
        self.db.commit()


    def retrieve(self, id):
        query = "SELECT * FROM donor WHERE id=%s"
        self.cursor.execute(query, (id,))
        return self.cursor.fetchone()

    # 4. Update donor
    def update(self, id, name, blood_group, phone, city, last_donation):
        query = """
        UPDATE donor
        SET name=%s, blood_group=%s, phone=%s,
            city=%s, last_donation=%s
        WHERE id=%s
        """
        data = (name, blood_group, phone, city, last_donation, id)

        self.cursor.execute(query, data)
        self.db.commit()

        return self.cursor.rowcount > 0


    def delete(self, id):
        query = "DELETE FROM donor WHERE id=%s"
        self.cursor.execute(query, (id,))
        self.db.commit()

        return self.cursor.rowcount > 0