import sqlite3
from datetime import datetime

# Initialize database
def init_db():
    conn = sqlite3.connect('student_records.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            roll_number TEXT UNIQUE NOT NULL,
            midterm REAL,
            endterm REAL,
            internal REAL,
            midterm_contribution REAL,
            endterm_contribution REAL,
            internal_contribution REAL,
            final_score REAL,
            date_recorded TIMESTAMP
        )
    ''')
    conn.commit()
    return conn

def calculate_contributions(midterm, endterm, internal):
    """Calculate individual contributions and final score"""
    # Normalize scores to 100
    midterm_normalized = (midterm / 50) * 100
    endterm_normalized = (endterm / 100) * 100
    internal_normalized = (internal / 100) * 100
    
    # Calculate contributions (30%, 30%, 40%)
    midterm_contribution = midterm_normalized * 0.30
    endterm_contribution = endterm_normalized * 0.30
    internal_contribution = internal_normalized * 0.40
    
    # Final score out of 100
    final_score = midterm_contribution + endterm_contribution + internal_contribution
    
    return {
        'midterm_contrib': round(midterm_contribution, 2),
        'endterm_contrib': round(endterm_contribution, 2),
        'internal_contrib': round(internal_contribution, 2),
        'final_score': round(final_score, 2)
    }

def input_student_data():
    """Input student marks and calculate report card"""
    print("\n" + "="*60)
    print("STUDENT REPORT CARD ENTRY SYSTEM")
    print("="*60)
    
    try:
        name = input("Enter student name: ").strip()
        if not name:
            print("Error: Name cannot be empty!")
            return None
        
        roll_number = input("Enter roll number: ").strip()
        if not roll_number:
            print("Error: Roll number cannot be empty!")
            return None
        
        # Input marks
        while True:
            try:
                midterm = float(input("Enter midterm marks (out of 50): "))
                if 0 <= midterm <= 50:
                    break
                else:
                    print("Midterm marks should be between 0 and 50!")
            except ValueError:
                print("Please enter a valid number!")
        
        while True:
            try:
                endterm = float(input("Enter end term marks (out of 100): "))
                if 0 <= endterm <= 100:
                    break
                else:
                    print("End term marks should be between 0 and 100!")
            except ValueError:
                print("Please enter a valid number!")
        
        while True:
            try:
                internal = float(input("Enter internal marks (out of 100): "))
                if 0 <= internal <= 100:
                    break
                else:
                    print("Internal marks should be between 0 and 100!")
            except ValueError:
                print("Please enter a valid number!")
        
        # Calculate contributions
        contributions = calculate_contributions(midterm, endterm, internal)
        
        return {
            'name': name,
            'roll_number': roll_number,
            'midterm': midterm,
            'endterm': endterm,
            'internal': internal,
            'midterm_contrib': contributions['midterm_contrib'],
            'endterm_contrib': contributions['endterm_contrib'],
            'internal_contrib': contributions['internal_contrib'],
            'final_score': contributions['final_score']
        }
    
    except KeyboardInterrupt:
        print("\nOperation cancelled!")
        return None

def display_report_card(student_data):
    """Display the calculated report card"""
    print("\n" + "="*60)
    print("REPORT CARD")
    print("="*60)
    print(f"Name: {student_data['name']}")
    print(f"Roll Number: {student_data['roll_number']}")
    print("-" * 60)
    print("MARKS OBTAINED:")
    print(f"  Midterm (out of 50):        {student_data['midterm']:.2f}")
    print(f"  End Term (out of 100):      {student_data['endterm']:.2f}")
    print(f"  Internal (out of 100):      {student_data['internal']:.2f}")
    print("-" * 60)
    print("SCORE CONTRIBUTIONS:")
    print(f"  Midterm Contribution (30%): {student_data['midterm_contrib']:.2f}/30")
    print(f"  End Term Contribution (30%): {student_data['endterm_contrib']:.2f}/30")
    print(f"  Internal Contribution (40%): {student_data['internal_contrib']:.2f}/40")
    print("-" * 60)
    print(f"FINAL SCORE (out of 100):   {student_data['final_score']:.2f}")
    print("="*60 + "\n")

def save_to_database(conn, student_data):
    """Save student data to database"""
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO students (name, roll_number, midterm, endterm, internal,
                                 midterm_contribution, endterm_contribution, 
                                 internal_contribution, final_score, date_recorded)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            student_data['name'],
            student_data['roll_number'],
            student_data['midterm'],
            student_data['endterm'],
            student_data['internal'],
            student_data['midterm_contrib'],
            student_data['endterm_contrib'],
            student_data['internal_contrib'],
            student_data['final_score'],
            datetime.now()
        ))
        conn.commit()
        print("✓ Record saved to database successfully!")
        return True
    except sqlite3.IntegrityError:
        print("✗ Error: This roll number already exists in the database!")
        return False
    except Exception as e:
        print(f"✗ Database error: {e}")
        return False

def view_all_records(conn):
    """View all student records from database"""
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students ORDER BY date_recorded DESC')
    records = cursor.fetchall()
    
    if not records:
        print("No records found in database!")
        return
    
    print("\n" + "="*100)
    print("ALL STUDENT RECORDS")
    print("="*100)
    print(f"{'Name':<20} {'Roll No':<12} {'Midterm':<10} {'End Term':<10} {'Internal':<10} {'Final':<10} {'Date':<20}")
    print("-"*100)
    
    for record in records:
        print(f"{record[1]:<20} {record[2]:<12} {record[3]:<10.2f} {record[4]:<10.2f} {record[5]:<10.2f} {record[8]:<10.2f} {record[10]:<20}")
    print("="*100 + "\n")

def main():
    """Main program loop"""
    conn = init_db()
    
    while True:
        print("\n" + "="*60)
        print("MAIN MENU")
        print("="*60)
        print("1. Add new student marks")
        print("2. View all records")
        print("3. Exit")
        print("="*60)
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == '1':
            student_data = input_student_data()
            if student_data:
                display_report_card(student_data)
                confirm = input("Do you want to save this record? (yes/no): ").strip().lower()
                if confirm in ['yes', 'y']:
                    save_to_database(conn, student_data)
        
        elif choice == '2':
            view_all_records(conn)
        
        elif choice == '3':
            print("Thank you for using the system. Goodbye!")
            conn.close()
            break
        
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
