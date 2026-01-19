import tkinter as tk
from tkinter import ttk, messagebox
import random

# Flashcard data including Scientists & Inventions with added Hard questions
flashcards = [
    # General Knowledge
    {"question": "How many continents are there?", "answer": "Seven", "category": "General Knowledge", "difficulty": "Easy"},
    {"question": "Who painted the Mona Lisa?", "answer": "Leonardo da Vinci", "category": "General Knowledge", "difficulty": "Medium"},
    {"question": "What is the tallest mountain in the world?", "answer": "Mount Everest", "category": "General Knowledge", "difficulty": "Easy"},
    {"question": "Which ocean is the largest?", "answer": "Pacific Ocean", "category": "General Knowledge", "difficulty": "Easy"},
    {"question": "Who is known as the Father of Computers?", "answer": "Charles Babbage", "category": "General Knowledge", "difficulty": "Medium"},
    {"question": "What year did the first man land on the moon?", "answer": "1969", "category": "General Knowledge", "difficulty": "Hard"},
    {"question": "What is the capital of the ancient kingdom of Mesopotamia?", "answer": "Babylon", "category": "General Knowledge", "difficulty": "Hard"},

    # Chemistry
    {"question": "What is the chemical symbol for water?", "answer": "H₂O", "category": "Chemistry", "difficulty": "Easy"},
    {"question": "What is the pH of a neutral solution?", "answer": "7", "category": "Chemistry", "difficulty": "Easy"},
    {"question": "Which element is used in pencils?", "answer": "Graphite (Carbon)", "category": "Chemistry", "difficulty": "Medium"},
    {"question": "Which gas is most abundant in Earth’s atmosphere?", "answer": "Nitrogen", "category": "Chemistry", "difficulty": "Medium"},
    {"question": "What is the chemical formula of table salt?", "answer": "NaCl", "category": "Chemistry", "difficulty": "Easy"},
    {"question": "Which acid is found in the human stomach?", "answer": "Hydrochloric acid", "category": "Chemistry", "difficulty": "Medium"},
    {"question": "What is the atomic number of Uranium?", "answer": "92", "category": "Chemistry", "difficulty": "Hard"},
    {"question": "What is the process of a solid turning directly into a gas called?", "answer": "Sublimation", "category": "Chemistry", "difficulty": "Hard"},

    # Capitals
    {"question": "What is the capital of Japan?", "answer": "Tokyo", "category": "Capitals", "difficulty": "Easy"},
    {"question": "What is the capital of Australia?", "answer": "Canberra", "category": "Capitals", "difficulty": "Medium"},
    {"question": "What is the capital of Canada?", "answer": "Ottawa", "category": "Capitals", "difficulty": "Medium"},
    {"question": "What is the capital of Brazil?", "answer": "Brasília", "category": "Capitals", "difficulty": "Medium"},
    {"question": "What is the capital of Egypt?", "answer": "Cairo", "category": "Capitals", "difficulty": "Easy"},
    {"question": "What is the capital of South Korea?", "answer": "Seoul", "category": "Capitals", "difficulty": "Medium"},
    {"question": "What is the capital of Mongolia?", "answer": "Ulaanbaatar", "category": "Capitals", "difficulty": "Hard"},
    {"question": "What is the capital of Bhutan?", "answer": "Thimphu", "category": "Capitals", "difficulty": "Hard"},

    # Mathematics
    {"question": "What is 8 + 6?", "answer": "14", "category": "Mathematics", "difficulty": "Easy"},
    {"question": "What is 12 × 9?", "answer": "108", "category": "Mathematics", "difficulty": "Medium"},
    {"question": "Solve: x if 2x = 10", "answer": "5", "category": "Mathematics", "difficulty": "Medium"},
    {"question": "What is the square root of 144?", "answer": "12", "category": "Mathematics", "difficulty": "Easy"},
    {"question": "What is 15% of 200?", "answer": "30", "category": "Mathematics", "difficulty": "Medium"},
    {"question": "What is the perimeter of a square with side 5?", "answer": "20", "category": "Mathematics", "difficulty": "Easy"},
    {"question": "Convert 0.75 to a fraction.", "answer": "3/4", "category": "Mathematics", "difficulty": "Easy"},
    {"question": "What is the derivative of sin(x)?", "answer": "cos(x)", "category": "Mathematics", "difficulty": "Hard"},
    {"question": "Evaluate the integral of 1/x dx.", "answer": "ln|x| + C", "category": "Mathematics", "difficulty": "Hard"},
    {"question": "What is Euler's identity?", "answer": "e^(iπ) + 1 = 0", "category": "Mathematics", "difficulty": "Hard"},

    # Math Formulas
    {"question": "What is the formula for the area of a triangle?", "answer": "1/2 × base × height", "category": "Mathematics", "difficulty": "Medium"},
    {"question": "What is the Pythagorean Theorem?", "answer": "a² + b² = c²", "category": "Mathematics", "difficulty": "Medium"},
    {"question": "What is the formula for the area of a circle?", "answer": "π × r²", "category": "Mathematics", "difficulty": "Medium"},
    {"question": "What is the formula for the circumference of a circle?", "answer": "2πr", "category": "Mathematics", "difficulty": "Medium"},
    {"question": "What is the formula for the volume of a cylinder?", "answer": "π × r² × h", "category": "Mathematics", "difficulty": "Hard"},
    {"question": "What is the quadratic formula?", "answer": "(-b ± √(b² - 4ac)) / 2a", "category": "Mathematics", "difficulty": "Hard"},

    # Scientists & Inventions
    {"question": "Who invented the telephone?", "answer": "Alexander Graham Bell", "category": "Scientists", "difficulty": "Easy"},
    {"question": "Who developed the theory of relativity?", "answer": "Albert Einstein", "category": "Scientists", "difficulty": "Medium"},
    {"question": "Who discovered penicillin?", "answer": "Alexander Fleming", "category": "Scientists", "difficulty": "Medium"},
    {"question": "Who invented the light bulb?", "answer": "Thomas Edison", "category": "Scientists", "difficulty": "Easy"},
    {"question": "Who proposed the laws of motion?", "answer": "Isaac Newton", "category": "Scientists", "difficulty": "Medium"},
    {"question": "Who invented the World Wide Web?", "answer": "Tim Berners-Lee", "category": "Scientists", "difficulty": "Hard"},
    {"question": "Who discovered the electron?", "answer": "J.J. Thomson", "category": "Scientists", "difficulty": "Hard"},
]

class FlashcardApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Flashcard Quiz App")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        self.score = 0
        self.current_index = 0
        self.time_left = 10
        self.timer_id = None
        self.showing_answer = False

        self.selected_category = tk.StringVar()
        self.selected_difficulty = tk.StringVar()

        self.create_start_screen()

    def create_start_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Select Category:", font=("Times New Roman", 14, "italic")).pack(pady=10)
        categories = sorted(list(set(card["category"] for card in flashcards)))
        self.category_menu = ttk.Combobox(self.root, textvariable=self.selected_category, values=categories, font=("Times New Roman", 12, "italic"), state="readonly")
        self.category_menu.pack()
        self.category_menu.current(0)

        tk.Label(self.root, text="Select Difficulty:", font=("Times New Roman", 14, "italic")).pack(pady=10)
        difficulties = sorted(list(set(card["difficulty"] for card in flashcards)))
        self.difficulty_menu = ttk.Combobox(self.root, textvariable=self.selected_difficulty, values=difficulties, font=("Times New Roman", 12, "italic"), state="readonly")
        self.difficulty_menu.pack()
        self.difficulty_menu.current(0)

        tk.Button(self.root, text="Start Quiz", font=("Times New Roman", 12, "italic"), command=self.start_quiz).pack(pady=20)

    def start_quiz(self):
        cat = self.selected_category.get()
        diff = self.selected_difficulty.get()
        self.filtered_flashcards = [
            card for card in flashcards
            if card["category"] == cat and card["difficulty"] == diff
        ]
        if not self.filtered_flashcards:
            messagebox.showerror("No Cards", "No flashcards match your selection.")
            return

        random.shuffle(self.filtered_flashcards)
        self.current_index = 0
        self.score = 0
        self.show_flashcard()

    def show_flashcard(self):
        self.clear_screen()
        self.showing_answer = False
        self.time_left = 10
        self.card = self.filtered_flashcards[self.current_index]

        self.question_label = tk.Label(self.root, text=self.card["question"], font=("Times New Roman", 18, "italic"), wraplength=450, justify="center")
        self.question_label.pack(pady=20)

        self.progress = ttk.Progressbar(self.root, maximum=len(self.filtered_flashcards), length=400)
        self.progress.pack(pady=(0, 15))
        self.progress['value'] = self.current_index + 1

        self.flip_button = tk.Button(self.root, text="Flip Card", font=("Times New Roman", 12, "italic"), command=self.flip_card)
        self.flip_button.pack(pady=5)

        self.right_button = tk.Button(self.root, text="Correct", font=("Times New Roman", 12, "italic"), command=lambda: self.submit_answer(True))
        self.right_button.pack(pady=5)

        self.wrong_button = tk.Button(self.root, text="Wrong", font=("Times New Roman", 12, "italic"), command=lambda: self.submit_answer(False))
        self.wrong_button.pack(pady=5)

        self.timer_label = tk.Label(self.root, text=f"Time Left: {self.time_left}", font=("Times New Roman", 12, "italic"))
        self.timer_label.pack(pady=10)

        self.score_label = tk.Label(self.root, text=f"Score: {self.score}", font=("Times New Roman", 12, "italic"))
        self.score_label.pack()

        self.update_timer()

    def flip_card(self):
        if self.showing_answer:
            self.question_label.config(text=self.card["question"])
            self.showing_answer = False
        else:
            self.question_label.config(text=self.card["answer"])
            self.showing_answer = True

    def submit_answer(self, is_correct):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None

        if is_correct:
            self.score += 1
        self.next_card()

    def next_card(self):
        self.current_index += 1
        if self.current_index < len(self.filtered_flashcards):
            self.show_flashcard()
        else:
            self.show_result()

    def update_timer(self):
        self.timer_label.config(text=f"Time Left: {self.time_left}")
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_id = self.root.after(1000, self.update_timer)
        else:
            self.timer_id = None
            messagebox.showinfo("Time's up!", "Moving to next question.")
            self.next_card()

    def show_result(self):
        self.clear_screen()
        result_text = f"Quiz Over!\nYour Score: {self.score} / {len(self.filtered_flashcards)}"
        tk.Label(self.root, text=result_text, font=("Times New Roman", 18, "italic")).pack(pady=30)
        tk.Button(self.root, text="Restart", font=("Times New Roman", 14, "italic"), command=self.create_start_screen).pack(pady=20)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()


if __name__ == "_main_":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()