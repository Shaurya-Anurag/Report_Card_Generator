# 📄 Project Statement — Student Report Card Management System

## 🧾 Overview

The **Student Report Card Management System** is a Python-based command-line application designed to record, calculate, and store academic performance data for students. The system ensures accurate weighted score computation while maintaining an organized and persistent database using SQLite.

This project demonstrates the use of:
- Python fundamentals  
- Input validation  
- Functions and modular code design  
- SQLite database integration  
- CLI-based user interaction  
- Data formatting and presentation  

---

## 🎯 Objective

To build a simple but robust system that:

1. Accepts student details and marks  
2. Normalizes and calculates weighted scores  
3. Generates a formatted report card  
4. Stores all entries in a persistent SQLite database  
5. Allows viewing of all stored student records  

The goal is to streamline the grading workflow while providing accurate, transparent calculations.

---

## 🧮 Marking Criteria Implemented

| Component | Raw Maximum | Normalized To | Weight |
|----------|-------------|---------------|--------|
| Midterm  | 50          | 100           | 30%    |
| End Term | 100         | 100           | 30%    |
| Internal | 100         | 100           | 40%    |

Score calculations are consistent, reproducible, and validated before being saved.

---

## 🔧 Functional Requirements

### Input Features
- Student name  
- Roll number (unique)  
- Midterm marks (0–50)  
- End term marks (0–100)  
- Internal marks (0–100)

### Processing Features
- Score normalization  
- Weighted score computation  
- Final score generation  
- Data validation  
- Error handling  

### Output Features
- Formatted report card view  
- Summary of all contributions  
- Database record insertion  
- Display all saved records  

---

## 🗂 Project Structure

```bash
student-report-card/
│
├── main.py                 # Core program logic
├── student_records.db      # SQLite database (auto-generated)
├── README.md               # Main documentation
└── statement.md            # Project statement file
