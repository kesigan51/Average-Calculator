import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        name = name_entry.get()
        marks_str = marks_entry.get()
        marks = [int(m) for m in marks_str.split()]
        
        if not name or not marks:
            messagebox.showwarning
            return

        avg = sum(marks) / len(marks)
        
        # Grade கணக்கிடுதல்
        if avg >= 90: grade = "A"
        elif avg >= 80: grade = "B"
        elif avg >= 70: grade = "C"
        elif avg >= 60: grade = "D"
        else: grade = "F"

        # முடிவைக் காட்டுதல்
        result_label.config(text=f"Student: {name}\nAverage: {avg:.1f}\nGrade: {grade}", fg="green")
        
    except ValueError:
        messagebox.showerror("Error", "Enter Marks(eg: 80 90 70)")


root = tk.Tk()
root.title("Average Calculator")
root.geometry("400x400")


tk.Label(root, text="STUDENT REPORT CARD", font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Student's name:").pack()
name_entry = tk.Entry(root, width=30)
name_entry.pack(pady=5)

tk.Label(root, text="Marks (Enter with Space):").pack()
marks_entry = tk.Entry(root, width=30)
marks_entry.pack(pady=5)


calc_btn = tk.Button(root, text="calculate Average", command=calculate, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
calc_btn.pack(pady=20)


result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()