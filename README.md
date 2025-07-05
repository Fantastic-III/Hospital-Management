# Django Hospital Database Management System

This repository houses the code for a Django-based web application that serves as a Hospital Database Management System (DBMS).

## Key Features

* **Appointment Booking:** Patients can conveniently book appointments online.
* **Appointment History:** Patients can easily view their past appointment records.
* **Doctor Portal:** Doctors can log in to access their scheduled appointments and view patient details.
* **User Sessions:** User details are securely stored in sessions, eliminating the need for frequent logins.
    * Example: Users don't have to log in again each time they visit the website.

## Technologies Used

* **Frontend:** HTML, CSS
* **Backend Framework:** Django (Python)
* **Database:** Django ORM, SQLite3

## Team

* **UI/Frontend Design:** (Kalpesh Gawas)[https://github.com/Kalpesh-Gawas]
* **Backend Development & Database Management:** (Onkar Gite)[https://github.com/onkar0127], (Sailesh Bhoite)[https://github.com/Sailesh-Bhoite]

## Lessons Learned

This project provided valuable hands-on experience in various web development aspects, including:

* **Django Fundamentals:**
    * Creating and managing routes/URLs.
    * Connecting respective view functions to URLs.
* **Frontend Integration:**
    * Rendering HTML, CSS, and Image files.
* **Database Interaction:**
    * Getting data from and sending data to the Database and HTML file.
* **State Management:**
    * Using Sessions to store data.
        * Ensuring user details persist across visits without re-login.
* **User Experience:**
    * Implementing effective page redirection for seamless navigation.

## Getting Started

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Fantastic-III/Hospital-Management
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Start the development server:**
    ```bash
    python manage.py runserver
    ```

---

*This project marks a significant step in our journey towards mastering web development. Stay tuned for more exciting projects!* 💻✨
