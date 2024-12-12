# **User Registration and Admin Promotion System**

A web application built with **FastAPI** that provides the following features:
- User registration and login.
- Promotion of specific users to admin roles.
- Admin dashboard access for promoted users.
- Basic user dashboard for non-admin users.

## **Features**

1. **User Registration**:
   - Register with an email and password.
   - Automatic redirection to the login page after successful registration.

2. **Login**:
   - Users can log in using their email and password.
   - Admin users are redirected to the admin dashboard.
   - Regular users are redirected to a user dashboard.

3. **Promote to Admin**:
   - Authorized users can promote registered users to admin status.
   - Admin privileges grant access to the admin dashboard.

4. **Dashboards**:
   - Admin Dashboard: Available only to users with admin privileges.
   - User Dashboard: Available to regular users.

## **Project Structure**

```plaintext
project/
├── main.py                # Entry point for the FastAPI application
├── db_config.py           # Database configuration
├── models.py              # SQLAlchemy models
├── routers/
│   ├── auth.py            # Routes for authentication and admin promotion
├── templates/
│   ├── home.html          # Home page
│   ├── login.html         # Login page
│   ├── register.html      # Registration page
│   ├── admin.html         # Admin dashboard
│   └── user.html          # User dashboard
├── static/
│   └── style.css          # CSS for styling
└── README.md              # Project documentation
```

## **Installation**

1. **Clone the repository**:
   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install fastapi uvicorn sqlalchemy passlib jinja2
   ```

4. **Run the application**:
   ```bash
   uvicorn main:app --reload
   ```

5. **Access the application**:
   - Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

## **Endpoints**

### **Public Endpoints**
- **`GET /auth/register`**: Registration page.
- **`POST /auth/register`**: Register a new user.
- **`GET /auth/login`**: Login page.
- **`POST /auth/login`**: Authenticate user and redirect to dashboard.

### **Admin-Specific Endpoints**
- **`POST /auth/promote-to-admin`**: Promote a registered user to admin.
- **`GET /auth/admin`**: Admin dashboard.

### **User Dashboard**
- **`GET /auth/user`**: Regular user dashboard.

## **Technologies Used**
- **Backend**: [FastAPI](https://fastapi.tiangolo.com/)
- **Database**: SQLite with SQLAlchemy ORM
- **Templating**: Jinja2
- **CSS**: Custom styling for basic UI
