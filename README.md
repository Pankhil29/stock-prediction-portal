# 📈 Stock Prediction Portal

A full-stack stock prediction application with a Django REST Framework (DRF) backend and a React (Vite) frontend.

---

## 📌 Overview

This project contains both the backend API and the frontend user interface for a stock prediction portal.

- **Backend:** Django + Django REST Framework
- **Frontend:** React (Vite)
- **Authentication:** JWT-based login and registration
- **Main Functionality:** User authentication, protected dashboard, and stock prediction API integration

---

## ✨ Features

- User registration & login
- JWT authentication with token refresh support
- Protected dashboard access
- Stock prediction API integration
- Responsive frontend UI

---

## 🛠️ Tech Stack

### **Backend**
- Python 3.10+
- Django
- Django REST Framework (DRF)
- Django REST Framework Simple JWT

### **Frontend**
- React
- React Router
- Vite
- CSS

---

## 📋 Prerequisites

Make sure the following are installed on your system:
- **Python:** 3.10+
- **Node.js:** 18+
- **Package Manager:** npm
- **Version Control:** Git

---

## 📂 Project Structure

```text
stock-prediction-portal/
├── backend-drf/            # Django backend
│   ├── accounts/           # User auth and profile logic
│   ├── api/                # API routes and prediction views
│   ├── manage.py           # Django management script
│   └── requirements.txt    # Python dependencies
├── frontend-react/         # React frontend
│   ├── src/                # React components and pages
│   ├── public/             # Static assets
│   └── package.json        # Frontend dependencies and scripts
└── README.md               # Project documentation
```

---

## 🚀 Setup & Installation

### 1. Backend Setup (Windows)

Open terminal and navigate to the backend folder:

```bash
cd backend-drf
py -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

The backend server will run at: **`http://127.0.0.1:8000/`**

---

### 2. Frontend Setup

Open a new terminal window and navigate to the frontend folder:

```bash
cd frontend-react
npm install
npm run dev
```

The frontend application will run at: **`http://localhost:5173/`**

---

## 📡 API Endpoints

The backend exposes the following API routes:

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/api/register/` | Register a new user |
| `POST` | `/api/token/` | Get JWT access and refresh tokens |
| `POST` | `/api/token/refresh/` | Refresh access token |
| `GET` | `/api/profile/` | Get authenticated user profile |
| `GET` | `/api/protected-view/` | Protected API test route |
| `POST` | `/api/predict/` | Submit a stock prediction request |

---

## 🔐 Authentication Example

This project uses JWT authentication. You can test authentication using cURL:

### Obtain Access Token
```bash
curl -X POST http://127.0.0.1:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d "{\"username\":\"your_username\",\"password\":\"your_password\"}"
```

### Access Protected Endpoint
```bash
curl -X GET http://127.0.0.1:8000/api/profile/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

---

## 🏃 Running the Full Project

To use the full application:
1. Start the backend server (`python manage.py runserver`)
2. Start the frontend server (`npm run dev`)
3. Open `http://localhost:5173/` in your browser
4. Register or log in
5. Use the dashboard and prediction features

---

## 🧪 Running Tests

### Backend Tests
```bash
cd backend-drf
python manage.py test
```