import tkinter as tk
import random

BG = "#1a1a2e"        # 深夜藍背景
PANEL = "#16213e"     # 輸入框底色
BAR_BG = "#0f3460"    # 範圍條底色
ACCENT = "#e94560"    # 主要按鈕紅
GOLD = "#ffd369"      # 標題金
GREEN = "#4ecca3"     # 安全區綠
TEXT = "#eaeaea"
MUTED = "#8d93ab"
FONT = "Arial"


class GuessNumberGame:
    MAX_ATTEMPTS = 10

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("猜數字大冒險")
        self.window.geometry("430x700")
        self.window.resizable(False, False)
        self.window.configure(bg=BG)

        self.confetti_running = False
        self.game_frame = tk.Frame(self.window, bg=BG)
        self.result_frame = tk.Frame(self.window, bg=BG)
        self.build_game_screen()
        self.new_game()

    def run(self):
        self.window.mainloop()

    # ---------- 畫面建立 ----------

    def build_game_screen(self):
        f = self.game_frame

        tk.Label(f, text="🎯 猜數字大冒險", font=(FONT, 26, "bold"),
                 bg=BG, fg=GOLD).pack(pady=(26, 2))
        tk.Label(f, text="我心裡想了一個 1 ~ 100 的數字，猜猜看！",
                 font=(FONT, 12), bg=BG, fg=MUTED).pack()

        status = tk.Frame(f, bg=BG)
        status.pack(fill="x", padx=26, pady=(18, 0))
        self.hearts_label = tk.Label(status, font=(FONT, 13), bg=BG, anchor="w")
        self.hearts_label.pack(side="left")
        self.score_label = tk.Label(status, font=(FONT, 14, "bold"),
                                    bg=BG, fg=GOLD, anchor="e")
        self.score_label.pack(side="right")

        self.emoji_label = tk.Label(f, text="🤔", font=(FONT, 56), bg=BG)
        self.emoji_label.pack(pady=(14, 0))
        self.feedback_label = tk.Label(f, text="", font=(FONT, 15, "bold"),
                                       bg=BG, fg=TEXT, wraplength=380)
        self.feedback_label.pack(pady=(4, 10))

        self.range_canvas = tk.Canvas(f, width=390, height=90,
                                      bg=BG, highlightthickness=0)
        self.range_canvas.pack(pady=2)

        self.history_label = tk.Label(f, text="", font=(FONT, 12), bg=BG,
                                      fg=MUTED, wraplength=380, justify="center")
        self.history_label.pack(pady=(4, 10))

        entry_row = tk.Frame(f, bg=BG)
        entry_row.pack(pady=8)
        self.entry = tk.Entry(entry_row, font=(FONT, 24, "bold"), width=5,
                              justify="center", bg=PANEL, fg=TEXT,
                              insertbackground=GOLD, relief="flat",
                              highlightthickness=2,
                              highlightbackground=PANEL, highlightcolor=GOLD)
        self.entry.pack(side="left", ipady=8, padx=(0, 12))
        self.entry.bind("<Return>", lambda e: self.check_guess())
        self.make_button(entry_row, "出擊！🚀", ACCENT,
                         size=16, command=self.check_guess).pack(side="left")

        self.make_button(f, "重新開始 🔄", PANEL, fg=MUTED,
                         size=11, command=self.new_game).pack(pady=(16, 0))

    def make_button(self, parent, text, bg, fg="white", size=16, command=None):
        # macOS 的 tk.Button 不吃背景色，改用 Label 模擬按鈕
        btn = tk.Label(parent, text=text, font=(FONT, size, "bold"),
                       bg=bg, fg=fg, padx=18, pady=8, cursor="hand2")
        btn.bind("<Button-1>", lambda e: command())
        btn.bind("<Enter>", lambda e: btn.config(bg=self._shade(bg, 1.25)))
        btn.bind("<Leave>", lambda e: btn.config(bg=bg))
        return btn

    @staticmethod
    def _shade(color, factor):
        r, g, b = (int(color[i:i + 2], 16) for i in (1, 3, 5))
        r, g, b = (max(0, min(255, int(v * factor))) for v in (r, g, b))
        return f"#{r:02x}{g:02x}{b:02x}"

    # ---------- 遊戲流程 ----------

    def new_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.score = 100
        self.guesses = []
        self.min_guess = 1
        self.max_guess = 100
        self.game_over = False
        self.confetti_running = False

        self.result_frame.pack_forget()
        self.game_frame.pack(fill="both", expand=True)
        self.emoji_label.config(text="🤔")
        self.feedback_label.config(text="輸入數字，按 Enter 或「出擊」！", fg=TEXT)
        self.history_label.config(text="")
        self.entry.delete(0, tk.END)
        self.entry.focus_set()
        self.update_status()
        self.draw_range()

    def check_guess(self):
        if self.game_over:
            return
        raw = self.entry.get().strip()
        try:
            guess = int(raw)
        except ValueError:
            self.react("😵", "要輸入數字啦！", warn=True)
            return
        if not 1 <= guess <= 100:
            self.react("🙈", "要在 1 ~ 100 之間喔！", warn=True)
            return
        if guess in self.guesses:
            self.react("🤨", f"{guess} 已經猜過了，換一個吧！", warn=True)
            return
        if not self.min_guess <= guess <= self.max_guess:
            self.react("🧐", f"線索說答案在 {self.min_guess} ~ {self.max_guess} 之間喔！",
                       warn=True)
            return

        self.attempts += 1
        self.entry.delete(0, tk.END)

        if guess == self.secret_number:
            self.win()
            return

        self.score = max(0, self.score - 10)
        self.guesses.append(guess)
        if guess < self.secret_number:
            self.min_guess = guess + 1
            direction = "📈 再大一點！"
        else:
            self.max_guess = guess - 1
            direction = "📉 再小一點！"

        diff = abs(guess - self.secret_number)
        if diff <= 3:
            emoji, heat = "🔥", "燙死了！答案就在旁邊！"
        elif diff <= 10:
            emoji, heat = "♨️", "好熱好熱，非常接近！"
        elif diff <= 20:
            emoji, heat = "😐", "溫溫的，有點接近了"
        else:
            emoji, heat = "🧊", "好冷……還差得遠呢"

        self.history_label.config(text="  ".join(
            f"{g}{'⬆️' if g < self.secret_number else '⬇️'}" for g in self.guesses))
        self.update_status()
        self.draw_range()

        if self.attempts >= self.MAX_ATTEMPTS:
            self.lose()
            return

        self.react(emoji, f"{direction}  {heat}")

    def update_status(self):
        remaining = self.MAX_ATTEMPTS - self.attempts
        self.hearts_label.config(text="❤️" * remaining + "🖤" * self.attempts)
        self.score_label.config(text=f"🎖 {self.score} 分")

    def draw_range(self):
        c = self.range_canvas
        c.delete("all")
        x0, x1, y = 25, 365, 46

        def vx(v):
            return x0 + (v - 1) * (x1 - x0) / 99

        c.create_rectangle(x0, y - 9, x1, y + 9, fill=BAR_BG, outline="")
        lo, hi = vx(self.min_guess), vx(self.max_guess)
        hi = max(hi, lo + 3)
        c.create_rectangle(lo, y - 9, hi, y + 9, fill=GREEN, outline="")

        c.create_text(x0, y + 24, text="1", font=(FONT, 10), fill=MUTED)
        c.create_text(x1, y + 24, text="100", font=(FONT, 10), fill=MUTED)
        if hi - lo < 40:
            c.create_text((lo + hi) / 2, y - 22,
                          text=f"{self.min_guess}~{self.max_guess}",
                          font=(FONT, 12, "bold"), fill=GREEN)
        else:
            c.create_text(lo, y - 22, text=str(self.min_guess),
                          font=(FONT, 12, "bold"), fill=GREEN)
            c.create_text(hi, y - 22, text=str(self.max_guess),
                          font=(FONT, 12, "bold"), fill=GREEN)

        for g in self.guesses:
            gx = vx(g)
            c.create_oval(gx - 4, y - 4, gx + 4, y + 4, fill=ACCENT, outline="")

        c.create_text((x0 + x1) / 2, y + 38, text="💎 寶藏就藏在綠色地帶！",
                      font=(FONT, 11), fill=MUTED)

    # ---------- 回饋效果 ----------

    def react(self, emoji, message, warn=False):
        self.emoji_label.config(text=emoji)
        self.feedback_label.config(text=message, fg=ACCENT if warn else TEXT)
        if warn:
            self.window.bell()
            self.shake()
        else:
            self.pop_emoji()

    def pop_emoji(self):
        self.emoji_label.config(font=(FONT, 66))
        self.window.after(120, lambda: self.emoji_label.config(font=(FONT, 56)))

    def shake(self):
        x, y = self.window.winfo_x(), self.window.winfo_y()
        for i, dx in enumerate([10, -10, 7, -7, 4, -4, 0]):
            self.window.after(i * 35,
                              lambda dx=dx: self.window.geometry(f"+{x + dx}+{y}"))

    # ---------- 結算畫面 ----------

    def win(self):
        self.game_over = True
        if self.attempts <= 4:
            stars, praise = "⭐⭐⭐", "太神了！你是猜數字大師！"
        elif self.attempts <= 7:
            stars, praise = "⭐⭐", "很厲害！腦筋動得真快！"
        else:
            stars, praise = "⭐", "成功過關！挑戰用更少次數吧！"
        self.show_result("🏆", f"答對了！答案就是 {self.secret_number}",
                         f"只用了 {self.attempts} 次！", stars, praise, win=True)

    def lose(self):
        self.game_over = True
        self.show_result("💔", f"可惜！答案是 {self.secret_number}",
                         "就差那麼一點點……", "",
                         "再試一次，你一定可以的！", win=False)

    def show_result(self, emoji, title, subtitle, stars, praise, win):
        self.game_frame.pack_forget()
        for child in self.result_frame.winfo_children():
            child.destroy()
        self.result_frame.pack(fill="both", expand=True)

        w, h = 430, 700
        canvas = tk.Canvas(self.result_frame, bg=BG, highlightthickness=0)
        canvas.pack(fill="both", expand=True)

        canvas.create_text(w / 2, 170, text=emoji, font=(FONT, 80))
        canvas.create_text(w / 2, 272, text=title, font=(FONT, 22, "bold"),
                           fill=GOLD if win else TEXT)
        canvas.create_text(w / 2, 312, text=subtitle, font=(FONT, 15), fill=TEXT)
        if stars:
            canvas.create_text(w / 2, 362, text=stars, font=(FONT, 34))
        canvas.create_text(w / 2, 408, text=praise, font=(FONT, 14), fill=MUTED)
        if win:
            canvas.create_text(w / 2, 448, text=f"🎖 得分：{self.score}",
                               font=(FONT, 16, "bold"), fill=GREEN)

        btn = self.make_button(canvas, "再玩一次 🎲", ACCENT,
                               size=17, command=self.new_game)
        canvas.create_window(w / 2, 525, window=btn)

        if win:
            self.start_confetti(canvas, w, h)

    def start_confetti(self, canvas, w, h):
        self.confetti_running = True
        chars = ["🎉", "🎊", "✨", "⭐", "💛", "💚", "💙"]
        self.confetti = []
        for _ in range(26):
            item = canvas.create_text(random.randint(10, w - 10),
                                      random.randint(-h, 0),
                                      text=random.choice(chars),
                                      font=(FONT, random.randint(12, 22)))
            self.confetti.append((item, random.uniform(2.5, 6)))
        self.animate_confetti(canvas, h)

    def animate_confetti(self, canvas, h):
        if not self.confetti_running or not canvas.winfo_exists():
            return
        for item, speed in self.confetti:
            canvas.move(item, random.uniform(-1, 1), speed)
            if canvas.coords(item)[1] > h + 20:
                canvas.move(item, 0, -(h + 40))
        self.window.after(40, lambda: self.animate_confetti(canvas, h))


if __name__ == "__main__":
    GuessNumberGame().run()
