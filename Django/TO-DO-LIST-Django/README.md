# 📝 TO-DO-LIST-Django  

![Django](https://img.shields.io/badge/Django-5.0-green?logo=django&logoColor=white)  
![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=yellow)  
![License](https://img.shields.io/badge/License-MIT-orange)  
![Status](https://img.shields.io/badge/Status-Active-success)  
![Contributions](https://img.shields.io/badge/Contributions-Welcome-brightgreen)  

A **Full Stack To-Do List Web Application** built using **Django, HTML, and CSS** with user authentication.  
Users can register, login, add tasks, edit them, mark as complete/incomplete, and delete tasks.  

---

## 🚀 Features
- ✅ User Registration & Login (Authentication)  
- ✅ Add, Edit, and Delete Tasks  
- ✅ Mark tasks as complete/incomplete  
- ✅ Organized Templates (Base, Nav, Home, Edit, Login/Register, etc.)  
- ✅ Static Files (CSS, Images)  
- ✅ SQLite database (default Django DB)  

---

## 🛠️ Tech Stack
- **Backend:** Django (Python)  
- **Frontend:** HTML, CSS  
- **Database:** SQLite3  
- **Authentication:** Django Auth System  

---

### 📂 Project Structure
```yaml
TODO_final/
│── base/                 # Core app (Task management)
│   ├── templates/        # Task templates (home, edit, etc.)
│
│── authen/               # Authentication app (login, register, logout)
│   ├── templates/        # Auth templates
│
│── static/               # CSS, images
│── manage.py             # Django project manager
│── requirements.txt      # Dependencies
│── README.md             # Documentation
│── .gitignore            # Ignored files
```
### SetUp Instructions
```
# 1️⃣ Clone the Repository
git clone https://github.com/<your-username>/TO-DO-LIST-Django.git
cd TO-DO-LIST-Django

# 2️⃣ Create & Activate Virtual Environment
python -m venv venv

# ▶ On Windows
venv\Scripts\activate

# ▶ On Mac/Linux
source venv/bin/activate

# 3️⃣ Install Dependencies
pip install -r requirements.txt

# 4️⃣ Run Migrations
python manage.py migrate

# 5️⃣ Create Superuser (for Admin Access)
python manage.py createsuperuser

# 6️⃣ Start Development Server
python manage.py runserver
```

## 📸 Screenshots

### 🏠 Home Page  
![Home Page](https://github.com/user-attachments/assets/8b67d332-e402-4fc0-8bd7-09598200afe6)

### 🔑 Login Page  
![Login Page](https://github.com/user-attachments/assets/4c120b31-9795-4584-9eb6-3cf8438a42dc)

### 📝 Register Page  
![Register Page](https://github.com/user-attachments/assets/872c62f5-30a5-4373-a074-4c2e820bd1d7)


### 🤝 Contributing
```
Contributions are welcome!

Fork the repository

Create a new feature branch (git checkout -b feature-name)

Commit your changes (git commit -m "Added feature XYZ")

Push to your branch (git push origin feature-name)

Open a Pull Request 🎉
```

### ✨ Built with ❤️ using Django ✨
