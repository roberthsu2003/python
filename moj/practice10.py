import random
import tkinter as tk
from tkinter import messagebox

class GuessNumberGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("猜數字遊戲")
        self.window.geometry("420x380")
        self.window.resizable(False, False)
        self.window.configure(bg="#2c3e50")
        
        self.min_val = 1
        self.max_val = 100
        self.count = 0
        self.target = random.randint(1, 100)
        
        self.create_widgets()
    
    def create_widgets(self):
        title = tk.Label(self.window, text="猜數字遊戲", font=("Arial", 24, "bold"),
                        bg="#2c3e50", fg="#ecf0f1")
        title.pack(pady=15)
        
        self.range_label = tk.Label(self.window, text=f"請猜 {self.min_val} ~ {self.max_val} 之間的數字",
                                   font=("Arial", 14), bg="#2c3e50", fg="#f39c12")
        self.range_label.pack(pady=10)
        
        self.count_label = tk.Label(self.window, text="已猜次數: 0",
                                   font=("Arial", 12), bg="#2c3e50", fg="#ecf0f1")
        self.count_label.pack()
        
        input_frame = tk.Frame(self.window, bg="#2c3e50")
        input_frame.pack(pady=15)
        
        self.entry = tk.Entry(input_frame, font=("Arial", 16), width=10, justify="center")
        self.entry.pack(side="left", padx=5)
        self.entry.bind("<Return>", lambda event: self.make_guess())
        
        self.guess_btn = tk.Button(input_frame, text="猜!", font=("Arial", 12, "bold"),
                                  bg="#27ae60", fg="white", width=6, command=self.make_guess)
        self.guess_btn.pack(side="left", padx=5)
        
        self.result_label = tk.Label(self.window, text="", font=("Arial", 16, "bold"),
                                    bg="#2c3e50", fg="#ecf0f1", height=2)
        self.result_label.pack(pady=10)
        
        self.restart_btn = tk.Button(self.window, text="再玩一次", font=("Arial", 12),
                                    bg="#3498db", fg="white", width=12, command=self.restart_game)
        self.restart_btn.pack(pady=5)
        self.restart_btn.pack_forget()
        
        self.quit_btn = tk.Button(self.window, text="結束遊戲", font=("Arial", 12),
                                 bg="#e74c3c", fg="white", width=12, command=self.window.quit)
        self.quit_btn.pack(pady=5)
    
    def make_guess(self):
        try:
            guess = int(self.entry.get())
        except ValueError:
            messagebox.showwarning("錯誤", "請輸入數字!")
            return
        
        if guess < self.min_val or guess > self.max_val:
            messagebox.showwarning("超出範圍", f"請輸入 {self.min_val} ~ {self.max_val} 之間的數字!")
            return
        
        self.count += 1
        self.count_label.config(text=f"已猜次數: {self.count}")
        
        if guess == self.target:
            self.result_label.config(text=f"賓果!猜對了!\n答案是: {self.target}", fg="#2ecc71")
            self.entry.config(state="disabled")
            self.guess_btn.config(state="disabled")
            self.ask_continue()
        elif guess > self.target:
            self.max_val = guess - 1
            self.result_label.config(text="再小一點", fg="#e74c3c")
        else:
            self.min_val = guess + 1
            self.result_label.config(text="再大一點", fg="#e74c3c")
        
        self.range_label.config(text=f"請猜 {self.min_val} ~ {self.max_val} 之間的數字")
        self.entry.delete(0, tk.END)
    
    def ask_continue(self):
        answer = messagebox.askyesno("是否繼續", "你還要繼續玩嗎？")
        if answer:
            self.restart_game()
        else:
            self.window.quit()
    
    def restart_game(self):
        self.min_val = 1
        self.max_val = 100
        self.count = 0
        self.target = random.randint(1, 100)
        
        self.range_label.config(text=f"請猜 {self.min_val} ~ {self.max_val} 之間的數字")
        self.count_label.config(text="已猜次數: 0")
        self.result_label.config(text="")
        
        self.entry.config(state="normal")
        self.entry.delete(0, tk.END)
        self.guess_btn.config(state="normal")
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = GuessNumberGame()
    game.run()
