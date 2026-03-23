# 🧠 Hangarin – Task & To-Do Manager

Hangarin is a modern and minimalist task management web application built with Django. It helps users organize, track, and manage their tasks efficiently with a clean interface and powerful features.

---

## 🚀 Features

### ✅ Task Management
- Create, edit, and delete tasks
- View detailed task information
- Organize tasks using categories and priorities

### 📅 Deadline Tracking
- Set deadlines with date and time picker
- Track upcoming and overdue tasks

### 🔍 Search, Filter & Sort
- Search tasks instantly
- Filter by:
  - Status (Pending, In Progress, Completed)
  - Priority
  - Category
- Sort by:
  - Newest / Oldest
  - Due date

### 📊 Dashboard Overview
- Displays:
  - Total tasks
  - Total notes
  - Total subtasks
- Status summary:
  - Pending
  - In Progress
  - Completed

### 🧩 Subtasks & Notes
- Add subtasks to tasks
- Add notes for extra details

### 👤 User Authentication
- User signup and login system
- Profile dropdown with:
  - Admin Dashboard (if admin)
  - My Profile
  - Settings
  - Inbox
  - Logout

### 🔐 Admin Panel
- Django built-in admin system
- Accessible from profile menu

### 🎨 UI / UX
- Minimalist dark theme
- Clean and modern design
- Responsive layout
- Smooth dropdown interactions

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite
- **Authentication:** Django Auth System

---

## 📂 Project Structure

```
Hangarin_Task/
│
├── Hangarin/              # Main app
├── projectsite/           # Django project config
├── templates/             # HTML templates
├── static/                # CSS, JS, images
├── requirements.txt
└── manage.py
```

---

## ⚙️ Installation Guide

### 1. Clone the Repository
```bash
git clone https://github.com/Althea09-gif/Hangarin_Task.git
cd Hangarin_Task
```

### 2. Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Migrations
```bash
python manage.py migrate
```

### 5. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 6. Run the Server
```bash
python manage.py runserver
```

---

## 🌐 Deployment

You can deploy this project using:

- PythonAnywhere
- Render
- Railway

---

## 💡 Benefits

- Improves productivity and task organization
- Easy-to-use interface
- Clean and minimalist design
- Flexible filtering system
- Scalable for future upgrades

---

## 🔮 Future Improvements

- Google & Facebook login integration
- Notification system
- Drag-and-drop task management
- Mobile optimization
- Real-time updates

---

## 👩‍💻 Developer

**Althea Lauren**  
📧 202280369@psu.palawan.edu.ph  

---

## 📌 License

This project is for educational purposes.
