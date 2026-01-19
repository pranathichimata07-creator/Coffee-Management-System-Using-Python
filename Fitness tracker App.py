import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import csv
from datetime import datetime, timedelta
import tkinter.font as tkFont

class FitnessTracker:
    def _init_(self, root):
        self.root = root
        self.root.title("Fitness Tracker with Progress Bars and Martial Arts")
        self.data = []
        self.goal_minutes = 300
        self.goal_calories = 2000

        # Set default font
        self.default_font = tkFont.Font(family="Times New Roman", size=11)

        # Exercise categories with exercises including Martial Arts
        self.exercise_map = {
            "Flexibility": ["Downward Dog", "Warrior Pose", "Tree Pose", "Cobra Pose", "Child’s Pose"],
            "Strength": ["Push-Ups", "Sit-Ups", "Plank", "Wall Sits", "Glute Bridges", "Leg Raises", "Dips"],
            "Cardio": ["Running", "Cycling", "Jump Rope", "Swimming", "Rowing", "High Knees"],
            "Martial Arts": [
                "Shadow Boxing", "Kicks (Roundhouse, Front, Side)", "Punching Bag Work",
                "Speed Bag Drills", "Defensive Dodges", "Grappling Techniques"
            ]
        }

        # UI Setup with font applied

        tk.Label(root, text="Exercise Type", font=self.default_font).grid(row=0, column=0)
        self.exercise_type_var = tk.StringVar()
        self.exercise_type_menu = ttk.Combobox(root, textvariable=self.exercise_type_var,
                                               values=list(self.exercise_map.keys()), font=self.default_font)
        self.exercise_type_menu.grid(row=0, column=1)
        self.exercise_type_menu.set("Cardio")
        self.exercise_type_menu.bind("<<ComboboxSelected>>", self.update_exercises)

        tk.Label(root, text="Exercise", font=self.default_font).grid(row=1, column=0)
        self.workout_var = tk.StringVar()
        self.workout_menu = ttk.Combobox(root, textvariable=self.workout_var, font=self.default_font)
        self.workout_menu.grid(row=1, column=1)
        self.update_exercises()

        tk.Label(root, text="Duration (mins)", font=self.default_font).grid(row=2, column=0)
        self.duration_var = tk.StringVar()
        tk.Entry(root, textvariable=self.duration_var, font=self.default_font).grid(row=2, column=1)

        tk.Label(root, text="Calories Burned", font=self.default_font).grid(row=3, column=0)
        self.calories_var = tk.StringVar()
        tk.Entry(root, textvariable=self.calories_var, font=self.default_font).grid(row=3, column=1)

        tk.Label(root, text="Date (YYYY-MM-DD)", font=self.default_font).grid(row=4, column=0)
        self.date_var = tk.StringVar(value=datetime.today().strftime('%Y-%m-%d'))
        tk.Entry(root, textvariable=self.date_var, font=self.default_font).grid(row=4, column=1)

        tk.Button(root, text="Add Workout", command=self.add_entry, font=self.default_font).grid(row=5, column=0, columnspan=2, pady=5)
        tk.Button(root, text="View Weekly Progress", command=self.view_progress, font=self.default_font).grid(row=6, column=0, columnspan=2)

        tk.Label(root, text="Weekly Goal (mins)", font=self.default_font).grid(row=7, column=0)
        self.goal_minutes_var = tk.StringVar(value=str(self.goal_minutes))
        tk.Entry(root, textvariable=self.goal_minutes_var, font=self.default_font, width=10).grid(row=7, column=1)

        tk.Label(root, text="Weekly Goal (kcal)", font=self.default_font).grid(row=8, column=0)
        self.goal_calories_var = tk.StringVar(value=str(self.goal_calories))
        tk.Entry(root, textvariable=self.goal_calories_var, font=self.default_font, width=10).grid(row=8, column=1)

        tk.Button(root, text="Update Goals", command=self.update_goals, font=self.default_font).grid(row=9, column=0, columnspan=2)

        tk.Button(root, text="Save to File", command=self.save_to_file, font=self.default_font).grid(row=10, column=0)
        tk.Button(root, text="Load from File", command=self.load_from_file, font=self.default_font).grid(row=10, column=1)

        tk.Label(root, text="Duration Progress", font=self.default_font).grid(row=11, column=0)
        self.duration_bar = ttk.Progressbar(root, length=200)
        self.duration_bar.grid(row=11, column=1)

        tk.Label(root, text="Calorie Progress", font=self.default_font).grid(row=12, column=0)
        self.calorie_bar = ttk.Progressbar(root, length=200)
        self.calorie_bar.grid(row=12, column=1)

        self.output_text = tk.Text(root, height=10, width=50, font=self.default_font)
        self.output_text.grid(row=13, column=0, columnspan=2, pady=10)

    def update_exercises(self, event=None):
        selected_type = self.exercise_type_var.get()
        exercises = self.exercise_map.get(selected_type, [])
        self.workout_menu['values'] = exercises
        if exercises:
            self.workout_var.set(exercises[0])

    def add_entry(self):
        ex_type = self.exercise_type_var.get()
        workout = self.workout_var.get()
        duration = self.duration_var.get()
        calories = self.calories_var.get()
        date_str = self.date_var.get()

        if not all([ex_type, workout, duration, calories, date_str]):
            messagebox.showerror("Error", "Please fill all fields.")
            return

        try:
            duration = int(duration)
            calories = int(calories)
            datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Invalid duration, calories, or date.")
            return

        self.data.append((ex_type, workout, duration, calories, date_str))
        messagebox.showinfo("Success", "Workout added.")
        self.clear_inputs()

    def view_progress(self):
        self.output_text.delete("1.0", tk.END)
        self.update_goals(silent=True)
        week_data = self.get_current_week_data()

        total_duration = sum(e[2] for e in week_data)
        total_calories = sum(e[3] for e in week_data)

        self.output_text.insert(tk.END, "=== This Week's Workouts ===\n")
        for i, (et, w, d, c, date) in enumerate(week_data, 1):
            self.output_text.insert(tk.END, f"{i}. {date} - {et} - {w} - {d} mins - {c} kcal\n")

        self.output_text.insert(tk.END, "\n=== Weekly Progress ===\n")
        self.output_text.insert(tk.END, f"Total Duration: {total_duration} / {self.goal_minutes} mins\n")
        self.output_text.insert(tk.END, f"Total Calories: {total_calories} / {self.goal_calories} kcal\n")

        dur_pct = min(100, int((total_duration / self.goal_minutes) * 100)) if self.goal_minutes else 0
        cal_pct = min(100, int((total_calories / self.goal_calories) * 100)) if self.goal_calories else 0

        self.duration_bar['value'] = dur_pct
        self.calorie_bar['value'] = cal_pct

    def get_current_week_data(self):
        today = datetime.today().date()
        start = today - timedelta(days=today.weekday())
        end = start + timedelta(days=6)
        return [e for e in self.data if start <= datetime.strptime(e[4], "%Y-%m-%d").date() <= end]

    def update_goals(self, silent=False):
        try:
            self.goal_minutes = int(self.goal_minutes_var.get())
            self.goal_calories = int(self.goal_calories_var.get())
            if not silent:
                messagebox.showinfo("Updated", "Goals updated.")
        except ValueError:
            messagebox.showerror("Error", "Invalid goal values.")

    def save_to_file(self):
        filepath = filedialog.asksaveasfilename(defaultextension=".csv")
        if filepath:
            with open(filepath, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Type", "Workout", "Duration", "Calories", "Date"])
                writer.writerows(self.data)
            messagebox.showinfo("Saved", "Data saved to file.")

    def load_from_file(self):
        filepath = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if filepath:
            with open(filepath, 'r') as f:
                reader = csv.reader(f)
                next(reader)  # skip header
                self.data = []
                for row in reader:
                    try:
                        ex_type, workout, duration, calories, date_str = row
                        self.data.append((ex_type, workout, int(duration), int(calories), date_str))
                    except ValueError:
                        continue
            messagebox.showinfo("Loaded", "Data loaded from file.")

    def clear_inputs(self):
        self.duration_var.set("")
        self.calories_var.set("")
        self.date_var.set(datetime.today().strftime('%Y-%m-%d'))

if __name__ == "_main_":
    root = tk.Tk()
    app = FitnessTracker(root)
    root.mainloop()