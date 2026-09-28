import mysql.connector


class DonorListCreateRetrieveUpdateDelete:

    def __init__(self):
        self.connection = mysql.connector.connect(
            user="root",
            password="root",
            host="localhost",
            database="blood_db"
        )

        print(self.connection)
        self.cursor = self.connection.cursor(dictionary=True)
        print("Successfully connected")

    def list(self):
        query = "SELECT * FROM donor"
        self.cursor.execute(query)
        records = self.cursor.fetchall()

        if records:
            return records
        else:
            print("No records found")


    def create(self, name, blood_group, phone, city, last_donation):
        query = """
        INSERT INTO donor
        (name, blood_group, phone, city, last_donation)
        VALUES (%s, %s, %s, %s, %s)
        """

        data = (name, blood_group, phone, city, last_donation)

        self.cursor.execute(query, data)
        self.connection.commit()

        print("Donor inserted successfully")


    def retrieve(self, id):
        query = "SELECT * FROM donor WHERE id=%s"
        data = (id,)

        self.cursor.execute(query, data)
        record = self.cursor.fetchone()

        if record:
            return record
        else:
            print("No record found")


    def update(self, id, name, blood_group, phone, city, last_donation):
        query = """
        UPDATE donor
        SET name=%s, blood_group=%s, phone=%s,
            city=%s, last_donation=%s
        WHERE id=%s
        """

        data = (name, blood_group, phone, city, last_donation, id)

        self.cursor.execute(query, data)
        self.connection.commit()

        if self.cursor.rowcount > 0:
            return True
        else:
            return False

    def delete(self, id):
        query = "DELETE FROM donor WHERE id=%s"
        data = (id,)

        self.cursor.execute(query, data)
        self.connection.commit()

        if self.cursor.rowcount > 0:
            return True
        else:
            return False