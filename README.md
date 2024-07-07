# Call A Doctor App (prototype)

This project was created for the coursework: Software Engineering (5001CEM)

## Group Details

Group number: 4

Members:
- Lim Weng Hong
- Oon Jay Von
- Steven Teo Boon Jie
- Tan Koon Teng

# Prerequisites
Inside 'credentials.zip':
- .env
- client_secret.json
- credentials.json

Please copy all credential files provided in order to access all functions related to fetching data entries (Google Sheets) and sending email.

# Main Scripts

In the project's main directory, you can run:

### `Clinic_Registration`

Runs the app for fetching applicants from Google Sheets (internet connection required)

Features:
- Fetches entries from Google Sheets which receives responses from Google Forms.
- Allows user to approve/reject clinics applying to be part of the system
- Sends out appropriate email response based on approval status

### `Clinic.py`
Runs the clinic view of Call-A-Doctor's system

Features:
- Create account credentials for doctors
- Edit doctors for respective clinics
- Accepting/rejecting patient requests

### `Doctor.py`

Runs the doctor view of Call-A-Doctor's system

Features:
- View and generate prescriptions for patients

### `Patient.py`

Runs the patient view of Call-A-Doctor's system

Features:
- Search/view available clinics
- View clinic location on Google Maps
- Make appointment with clinics

# Contributions:

**Lim Weng Hong**
- Login & Registration (logics & UI) 
- Page controllers for Clinic, Doctor, and Patient views (switch pages after successful login)
- Clinic registration app

**Oon Jay Von**
- Main app for clinic view (functional logics & UI)

**Steven Teo Boon Jie**
- Main app for patient view (functional logics & UI)

**Tan Koon Teng**
- Main app for doctor view (functional logics & UI)