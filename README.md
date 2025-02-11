# InterPer

InterPer is a web-based internship aggregator that scrapes and displays internship opportunities from Internshala based on user-selected skills. It helps students and job seekers find relevant internships quickly.

## 🚀 Features
- 🔍 **Skill-Based Search** – Find internships tailored to your skills.
- 🖥 **Web Scraping with Selenium** – Fetch real-time internships from Internshala.
- 📄 **Django Backend** – Stores scraped internships in a database.
- 🎨 **Modern UI** – Clean and user-friendly interface.

## 🛠️ Tech Stack
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Django
- **Scraping:** Selenium, WebDriver Manager
- **Database:** SQLite / PostgreSQL

## 📦 Installation
### **1. Clone the Repository**
```bash
git clone https://github.com/numanmaldar/InterPer.git
cd InterPer
```

### **2. Create a Virtual Environment (Optional but Recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Set Up Django Migrations**
```bash
python manage.py migrate
```

### **5. Run the Development Server**
```bash
python manage.py runserver
```
Access the app at `http://127.0.0.1:8000/`.

## 🖥️ How It Works
1. Enter your skills (e.g., Python, Data Science) to fetch relevant internships.
2. The scraper extracts internship details (title, company, location, stipend, duration) from Internshala.
3. Results are stored in the database and displayed on the frontend.
4. Click on an internship to apply.

## 🐞 Troubleshooting
- **WebDriver Issues?** Run:
  ```bash
  pip install --upgrade webdriver-manager
  ```
- **Database Issues?** Reset migrations:
  ```bash
  python manage.py flush
  python manage.py migrate
  ```

## 👨‍💻 Contributing
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch
   ```
3. Commit changes:
   ```bash
   git commit -m "Added new feature"
   ```
4. Push and create a Pull Request.

## 📜 License
This project is licensed under the **MIT License**.

---
### 💡 **Made with ❤️ by [Numan Maldar](https://github.com/numanmaldar/)**

