import unittest
import sqlite3
import os
from datetime import datetime

class TestMySideBarDatabaseQueries(unittest.TestCase):

    doctor_email = "danieltan717@gmail.com"

    def setUp(self):
        self.connection = sqlite3.connect('Python\Call-A-Doctor\db\database.db')  # Adjust with your actual database path
        self.cursor = self.connection.cursor()

    def tearDown(self):
        self.connection.close()

    def test_highlight_appointment_dates(self):
        query = "SELECT DISTINCT APPOINTMENT_DATE FROM APPOINTMENT WHERE DOCTOR_EMAIL = ?"
        self.cursor.execute(query, (self.doctor_email,))
        result = self.cursor.fetchall()
        expected_dates = [('01-07-2024',), ('16-06-2024',), ('17-06-2024',), ('22-06-2024',)]  # Adjust based on your test data
        self.assertEqual(result, expected_dates)

    def test_load_appointments(self):
        # Get today's date in the format "dd-MM-yyyy"
        today_date = datetime.now().strftime("%d-%m-%Y")

        # Query to fetch appointments for today for the specified doctor
        query = """
                SELECT APPOINTMENT.APPOINTMENT_ID, APPOINTMENT.APPOINTMENT_DATE, APPOINTMENT.APPOINTMENT_TIME, PATIENT.PATIENT_NAME
                FROM APPOINTMENT
                JOIN PATIENT ON APPOINTMENT.PATIENT_EMAIL = PATIENT.PATIENT_EMAIL
                WHERE APPOINTMENT.APPOINTMENT_DATE = ? AND APPOINTMENT.DOCTOR_EMAIL = ?
                """
        self.cursor.execute(query, (today_date, self.doctor_email))
        result = self.cursor.fetchall()
        self.assertIsNotNone(result)

    def test_load_approvals(self):
        expected_approvals = [
            (1, 'lee', 'John', 1),
            (2, 'lee', 'adam', 4),
            (4, 'lee', 'adam', 2)
        ]

        query = """
                SELECT A.APPROVAL_ID, D1.DOCTOR_NAME AS DOCTOR_NAME_SEND, P.PATIENT_NAME, A.RECORD_ID
                FROM PATIENT_RECORD_APPROVAL A
                LEFT JOIN DOCTORS D1 ON A.DOCTOR_EMAIL_SEND = D1.DOCTOR_EMAIL
                LEFT JOIN PATIENT P ON A.PATIENT_EMAIL = P.PATIENT_EMAIL
                WHERE A.DOCTOR_EMAIL_RECEIVED = ?
                AND A.STATUS = 0
                """
        self.cursor.execute(query, (self.doctor_email,))
        result = self.cursor.fetchall()

        self.assertEqual(len(result), len(expected_approvals))

        for i in range(len(expected_approvals)):
            self.assertEqual(result[i][0], expected_approvals[i][0])  # Approval ID
            self.assertEqual(result[i][1], expected_approvals[i][1])  # Doctor Name Send
            self.assertEqual(result[i][2], expected_approvals[i][2])  # Patient Name
            self.assertEqual(result[i][3], expected_approvals[i][3])  # Record ID

    def test_show_appointments(self):
        expected_appointment = (1, '01-07-2024', '12:00', 'John', 'Daniel')  # Expected values for one specific appointment

        query = """
                SELECT A.APPOINTMENT_ID, A.APPOINTMENT_DATE, A.APPOINTMENT_TIME, P.PATIENT_NAME, D.DOCTOR_NAME
                FROM APPOINTMENT A
                LEFT JOIN PATIENT P ON A.PATIENT_EMAIL = P.PATIENT_EMAIL
                LEFT JOIN DOCTORS D ON A.DOCTOR_EMAIL = D.DOCTOR_EMAIL
                WHERE A.APPOINTMENT_ID = 1
                AND A.DOCTOR_EMAIL = ?
                """
        self.cursor.execute(query, (self.doctor_email,))
        result = self.cursor.fetchone()

        self.assertIsNotNone(result)  # Ensure there is a result

        # Compare each field with the expected values
        self.assertEqual(result[0], expected_appointment[0])  # APPOINTMENT ID
        self.assertEqual(result[1], expected_appointment[1])  # Appointment Date
        self.assertEqual(result[2], expected_appointment[2])  # Appointment Time
        self.assertEqual(result[3], expected_appointment[3])  # Patient Name
        self.assertEqual(result[4], expected_appointment[4])  # Doctor Name

    def test_populate_profile_info(self):
        # Define expected profile info values
        expected_values = {
            'DOCTOR_NAME': 'Daniel',
            'CLINIC_NAME': 'pantai',
            'DOCTOR_ADDRESS': 'tanjung tokong',
            'DOCTOR_PHONENO': '0164234232',
            'DOCTOR_EMAIL': 'danieltan717@gmail.com'
        }

        # Execute query to fetch profile info for the doctor
        query = """
                SELECT DOCTOR_NAME, CLINIC_NAME, DOCTOR_ADDRESS, DOCTOR_PHONENO, DOCTOR_EMAIL 
                FROM DOCTORS 
                WHERE DOCTOR_EMAIL = ?
                """
        self.cursor.execute(query, (self.doctor_email,))
        result = self.cursor.fetchone()

        # Assert that all extracted values match the expected ones
        self.assertIsNotNone(result)
        self.assertEqual(result[0], expected_values['DOCTOR_NAME'])
        self.assertEqual(result[1], expected_values['CLINIC_NAME'])
        self.assertEqual(result[2], expected_values['DOCTOR_ADDRESS'])
        self.assertEqual(result[3], expected_values['DOCTOR_PHONENO'])
        self.assertEqual(result[4], expected_values['DOCTOR_EMAIL'])

if __name__ == '__main__':
    unittest.main()
