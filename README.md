
# Lost & Found Tracker – Flask Mini Project

A web-based **Lost & Found Tracker** application built using **Flask**, designed to help users report and search for lost or found items within a campus or community environment.

---

## Features

- Report lost or found items with an image and contact info
- View all reported items with filters: Lost / Found / All
- View full item details including contact and location
- Upload and preview item images
- Contact details available to help retrieve items
- Sort items by most recently reported

---

## Tech Stack

| Technology     | Purpose                          |
|----------------|----------------------------------|
| Python         | Backend logic                    |
| Flask          | Web framework                    |
| SQLite         | Lightweight embedded database    |
| Jinja2         | Templating engine for HTML pages |
| Bootstrap 5    | UI styling and responsiveness    |
| HTML/CSS       | Frontend templates               |

---

##  Folder Structure

```
lost_and_found/
├── app.py
├── lost_and_found.db
├── static/
│   └── uploads/         # Uploaded images
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── report.html
│   └── item_detail.html
└── README.md
```

---

## How to Run the App

1. **Clone the repository**
```bash
git clone https://github.com/PrasannaKumar-IT/lost_and_found.git
cd lost-and-found-tracker
```

2. **Install dependencies**
```bash
pip install flask flask_sqlalchemy
```

3. **Start the Flask app**
```bash
python app.py
```

4. Open your browser and navigate to:
```
http://127.0.0.1:5000/
```



## Author

**PrasannaKumar S**  
GitHub: [@PrasannaKumar-IT](https://github.com/PrasannaKumar-IT)  
LinkedIn: [linkedin.com/in/prasannakumar9624](https://www.linkedin.com/in/prasannakumar9624)

