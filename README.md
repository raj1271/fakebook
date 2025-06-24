# Fakebook 🧾

Fakebook is a Django-based social media web application inspired by Facebook, built using the **WebStack** (Django, HTML/CSS, JavaScript, Bootstrap). The app features user authentication, post creation, and admin control—all served via an ASGI-compatible server using **Daphne**.

## 🔧 Features

- User registration and login
- Admin panel for managing users and posts
- Create, edit, and delete posts
- Bootstrap-powered responsive UI
- Served using `daphne` for ASGI support (WebSocket/Realtime compatibility)

---

## 🚀 Getting Started

Follow the steps below to run the project locally.

### ✅ Step 1: Clone the Repository

```bash
git clone https://github.com/raj1271/fakebook.git
cd fakebook
```

### ✅ Step 2: Create a Virtual Environment

```bash
Create a virtual environment
python -m venv env
```

### ✅ Step 3: Activate the Environment

```bash
# For Windows
env\Scripts\activate

# For macOS/Linux
source env/bin/activate
```

### ✅ Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### ✅ Step 5: Apply Migrations

```bash
python manage.py migrate
```

### ✅ Step 6: (Optional) Create a Superuser
If you want your own admin account:

```bash
python manage.py createsuperuser
```
Or use the pre-configured admin credentials:

Email: raj@fake.in

Password: 2068

### ✅ Step 7: Run the Server Using Daphne

```bash
daphne fakebook.asgi:application
```
Replace fakebook with your Django project module name if it's different.

📝 License
This project is licensed under the MIT License.

🙋‍♂️ Author: Raj R. Pawar

📧 Email: raj.pawar2821@gmail.com

🔗 LinkedIn: linkedin.com/in/raj-pawar-973033217

🐙 GitHub: github.com/raj1271

🌟 Show Your Support
If you like this project, give it a ⭐ star on GitHub to support the work!


---

Let me know if you'd like to add deployment instructions (e.g. for Heroku, Vercel, or Render), `.env` configuration, or database switching instructions.

