import tkinter as tk
from tkinter import messagebox
import random


class GuessNumberGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("猜數字遊戲")
        self.window.geometry("400x500")
        self.window.resizable(False, False)
        self.window.configure(bg="#f0f0f0")

        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.max_attempts = 10
        self.history = []

        self.create_widgets()
        self.window.mainloop()

    def create_widgets(self):
        title_frame = tk.Frame(self.window, bg="#4a90a4", height=60)
        title_frame.pack(fill="x")
        title_frame.pack_propagate(False)

        tk.Label(
            title_frame,
            text="猜數字遊戲",
            font=("Arial", 24, "bold"),
            fg="white",
            bg="#4a90a4",
        ).pack(expand=True)

        main_frame = tk.Frame(self.window, bg="#f0f0f0", padx=30, pady=20)
        main_frame.pack(fill="both", expand=True)

        info_frame = tk.Frame(main_frame, bg="#e8f4f8", relief="solid", bd=1)
        info_frame.pack(fill="x", pady=(0, 15))

        tk.Label(
            info_frame,
            text="遊戲規則",
            font=("Arial", 14, "bold"),
            bg="#e8f4f8",
            fg="#2c3e50",
        ).pack(pady=(10, 5))

        tk.Label(
            info_frame,
            text="猜一個 1 到 100 之間的數字",
            font=("Arial", 11),
            bg="#e8f4f8",
            fg="#34495e",
        ).pack()

        self.attempts_label = tk.Label(
            info_frame,
            text="剩餘次數: 10",
            font=("Arial", 12, "bold"),
            bg="#e8f4f8",
            fg="#e74c3c",
        )
        self.attempts_label.pack(pady=(5, 10))

        input_frame = tk.Frame(main_frame, bg="#f0f0f0")
        input_frame.pack(fill="x", pady=10)

        tk.Label(
            input_frame,
            text="輸入你的猜測:",
            font=("Arial", 12),
            bg="#f0f0f0",
            fg="#2c3e50",
        ).pack(anchor="w")

        entry_frame = tk.Frame(input_frame, bg="#ffffff", relief="solid", bd=2)
        entry_frame.pack(fill="x", pady=5)

        self.entry = tk.Entry(
            entry_frame,
            font=("Arial", 16),
            justify="center",
            bg="#ffffff",
            fg="#2c3e50",
            insertbackground="#2c3e50",
        )
        self.entry.pack(pady=8, padx=10, fill="x")
        self.entry.bind("<Return>", lambda e: self.check_guess())

        button_frame = tk.Frame(main_frame, bg="#f0f0f0")
        button_frame.pack(fill="x", pady=15)

        self.guess_button = tk.Button(
            button_frame,
            text="猜測!",
            font=("Arial", 14, "bold"),
            bg="#3498db",
            fg="white",
            activebackground="#2980b9",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            command=self.check_guess,
        )
        self.guess_button.pack(fill="x", ipady=5)

        reset_frame = tk.Frame(main_frame, bg="#f0f0f0")
        reset_frame.pack(fill="x", pady=(0, 10))

        self.reset_button = tk.Button(
            reset_frame,
            text="新遊戲",
            font=("Arial", 11),
            bg="#95a5a6",
            fg="white",
            activebackground="#7f8c8d",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            command=self.new_game,
        )
        self.reset_button.pack(pady=5)

        history_frame = tk.Frame(main_frame, bg="#ffffff", relief="solid", bd=1)
        history_frame.pack(fill="both", expand=True, pady=(10, 0))

        tk.Label(
            history_frame,
            text="猜測歷史",
            font=("Arial", 12, "bold"),
            bg="#ffffff",
            fg="#2c3e50",
        ).pack(pady=(8, 5))

        history_scroll_frame = tk.Frame(history_frame, bg="#ffffff")
        history_scroll_frame.pack(fill="both", expand=True, padx=10, pady=(0, 10))

        self.history_text = tk.Text(
            history_scroll_frame,
            font=("Arial", 11),
            bg="#fafafa",
            fg="#34495e",
            height=6,
            state="disabled",
            wrap="word",
        )
        self.history_text.pack(fill="both", expand=True)

    def check_guess(self):
        guess_str = self.entry.get().strip()

        if not guess_str:
            messagebox.showwarning("提示", "請輸入一個數字!")
            return

        try:
            guess = int(guess_str)
        except ValueError:
            messagebox.showerror("錯誤", "請輸入有效的整數!")
            self.entry.delete(0, tk.END)
            return

        if guess < 1 or guess > 100:
            messagebox.showwarning("提示", "數字必須在 1 到 100 之間!")
            self.entry.delete(0, tk.END)
            return

        self.attempts += 1
        remaining = self.max_attempts - self.attempts
        self.attempts_label.config(text=f"剩餘次數: {remaining}")

        if guess == self.secret_number:
            self.history.append(f"✓ {guess} - 猜對了!")
            self.show_history()
            messagebox.showinfo(
                "恭喜!",
                f"你猜對了!\n答案是 {self.secret_number}\n你用了 {self.attempts} 次猜對!",
            )
            self.guess_button.config(state="disabled")
            self.entry.config(state="disabled")
            return

        if guess < self.secret_number:
            hint = "太小了!"
            self.history.append(f"↓ {guess} - 太小了")
        else:
            hint = "太大了!"
            self.history.append(f"↑ {guess} - 太大了")

        self.show_history()

        if remaining <= 0:
            messagebox.showinfo(
                "遊戲結束",
                f"很遺憾，你用完了所有次數!\n答案是 {self.secret_number}",
            )
            self.guess_button.config(state="disabled")
            self.entry.config(state="disabled")
        else:
            messagebox.showinfo("提示", hint)

        self.entry.delete(0, tk.END)

    def show_history(self):
        self.history_text.config(state="normal")
        self.history_text.delete("1.0", tk.END)
        for item in self.history:
            self.history_text.insert(tk.END, item + "\n")
        self.history_text.see(tk.END)
        self.history_text.config(state="disabled")

    def new_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.history = []

        self.attempts_label.config(text="剩餘次數: 10")
        self.guess_button.config(state="normal")
        self.entry.config(state="normal")
        self.entry.delete(0, tk.END)
        self.history_text.config(state="normal")
        self.history_text.delete("1.0", tk.END)
        self.history_text.config(state="disabled")


if __name__ == "__main__":
    GuessNumberGame()
