# 📘 Student Report Card Management System

A Python-based command-line application for generating and managing student report cards with SQLite database storage. This tool takes raw exam marks, calculates weighted contributions, normalizes scores, and stores the results persistently. Ideal for beginners learning Python, SQL, CLI apps, and data validation.

---

## 🚀 Features

- 🔹 **Student Entry System** — Validated input for name, roll number, and marks  
- 🔹 **Score Normalization** — Converts midterm (out of 50) to a 100-based scale  
- 🔹 **Weighted Calculation**
  - Midterm → 30%
  - End Term → 30%
  - Internal → 40%
- 🔹 **Final Score Generation** — Clean, formatted report card
- 🔹 **SQLite Storage** — Saves all results locally in `student_records.db`
- 🔹 **View All Records** — Displays saved data in structured table format
- 🔹 **Duplicate Roll Number Protection**
- 🔹 **Error Handling & Validation**

---

## 📂 Project Structure

```bash
student-report-card/
│
├── main.py                 # Main Python script (CLI + DB logic)
├── student_records.db      # Auto-generated SQLite database
├── README.md               # Documentation
└── .gitignore              # (Optional) Python + SQLite ignores

