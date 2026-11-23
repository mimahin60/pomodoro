import tkinter as tk
from tkinter import messagebox


# ============================================================
# SETTINGS
# ============================================================

FOCUS_TIME = 25 * 60
BREAK_TIME = 5 * 60


# ============================================================
# POMODORO APP
# ============================================================

class PomodoroApp:

    def __init__(self, root):
        self.root = root

        self.root.title("Pomodoro Timer")
        self.root.geometry("420x300")
        self.root.resizable(False, False)

        self.root.attributes("-topmost", True)

        self.cycle = 0
        self.state = "focus"
        self.remaining = FOCUS_TIME
        self.timer_running = False

        # ----------------------------------------------------
        # TITLE
        # ----------------------------------------------------

        self.title_label = tk.Label(
            root,
            text="🍅 Pomodoro Timer",
            font=("Arial", 22, "bold")
        )
        self.title_label.pack(pady=(20, 10))

        # ----------------------------------------------------
        # STATE
        # ----------------------------------------------------

        self.state_label = tk.Label(
            root,
            text="FOCUS",
            font=("Arial", 14, "bold")
        )
        self.state_label.pack()

        # ----------------------------------------------------
        # TIMER
        # ----------------------------------------------------

        self.timer_label = tk.Label(
            root,
            text="25:00",
            font=("Arial", 48, "bold")
        )
        self.timer_label.pack(pady=10)

        # ----------------------------------------------------
        # PROGRESS
        # ----------------------------------------------------

        self.progress_label = tk.Label(
            root,
            text="Completed: 0.00%",
            font=("Arial", 12)
        )
        self.progress_label.pack()

        # ----------------------------------------------------
        # CYCLE
        # ----------------------------------------------------

        self.cycle_label = tk.Label(
            root,
            text="Completed Pomodoros: 0",
            font=("Arial", 11)
        )
        self.cycle_label.pack(pady=5)

        # ----------------------------------------------------
        # BUTTONS
        # ----------------------------------------------------

        button_frame = tk.Frame(root)
        button_frame.pack(pady=15)

        self.pause_button = tk.Button(
            button_frame,
            text="Pause",
            width=10,
            command=self.toggle_pause
        )
        self.pause_button.grid(row=0, column=0, padx=5)

        self.skip_button = tk.Button(
            button_frame,
            text="Skip",
            width=10,
            command=self.skip_timer
        )
        self.skip_button.grid(row=0, column=1, padx=5)

        self.quit_button = tk.Button(
            button_frame,
            text="Quit",
            width=10,
            command=self.quit_app
        )
        self.quit_button.grid(row=0, column=2, padx=5)

        # ----------------------------------------------------
        # START
        # ----------------------------------------------------

        print("🍅 Pomodoro App Started")
        print()

        self.start_focus()


    # ========================================================
    # TIMER CONTROL
    # ========================================================

    def start_focus(self):
        self.state = "focus"
        self.remaining = FOCUS_TIME
        self.timer_running = True

        self.state_label.config(text="FOCUS")
        self.pause_button.config(text="Pause")

        self.update_gui()
        self.tick()


    def start_break(self):
        self.state = "break"
        self.remaining = BREAK_TIME
        self.timer_running = True

        self.state_label.config(text="BREAK")
        self.pause_button.config(text="Pause")

        self.update_gui()
        self.tick()


    def tick(self):

        if not self.timer_running:
            return

        self.print_status()

        self.update_gui()

        if self.remaining > 0:

            self.remaining -= 1

            self.root.after(
                1000,
                self.tick
            )

        else:

            print()

            self.timer_running = False

            self.time_up()


    # ========================================================
    # GUI UPDATE
    # ========================================================

    def update_gui(self):

        mins, secs = divmod(
            self.remaining,
            60
        )

        self.timer_label.config(
            text=f"{mins:02d}:{secs:02d}"
        )

        total = (
            FOCUS_TIME
            if self.state == "focus"
            else BREAK_TIME
        )

        elapsed = total - self.remaining

        percent = (
            elapsed / total
        ) * 100

        self.progress_label.config(
            text=f"Completed: {percent:.2f}%"
        )

        self.cycle_label.config(
            text=f"Completed Pomodoros: {self.cycle}"
        )


    # ========================================================
    # TERMINAL STATUS
    # ========================================================

    def print_status(self):

        total = (
            FOCUS_TIME
            if self.state == "focus"
            else BREAK_TIME
        )

        elapsed = total - self.remaining

        percent = (
            elapsed / total
        ) * 100

        mins, secs = divmod(
            self.remaining,
            60
        )

        print(
            f"\r[{self.state.upper()}] "
            f"Remaining: {mins:02d}:{secs:02d} | "
            f"Completed: {percent:6.2f}%",
            end="",
            flush=True
        )


    # ========================================================
    # PAUSE / RESUME
    # ========================================================

    def toggle_pause(self):

        if self.timer_running:

            self.timer_running = False

            self.pause_button.config(
                text="Resume"
            )

            print("\n⏸ Timer Paused")

        else:

            self.timer_running = True

            self.pause_button.config(
                text="Pause"
            )

            print("▶ Timer Resumed")

            self.tick()


    # ========================================================
    # SKIP
    # ========================================================

    def skip_timer(self):

        self.timer_running = False

        print("\n⏭ Timer Skipped")

        self.time_up()


    # ========================================================
    # TIME UP
    # ========================================================

    def time_up(self):

        if self.state == "focus":

            self.on_focus_finished()

        else:

            self.on_break_finished()


    # ========================================================
    # FOCUS FINISHED
    # ========================================================

    def on_focus_finished(self):

        answer = messagebox.askyesno(
            "Pomodoro Finished 🍅",
            "২৫ মিনিট পড়া শেষ হয়েছে।\n"
            "৫ মিনিট বিরতি নিতে চাও?"
        )

        if answer:

            self.start_break()

        else:

            self.finish_session()


    # ========================================================
    # BREAK FINISHED
    # ========================================================

    def on_break_finished(self):

        self.cycle += 1

        self.update_gui()

        answer = messagebox.askyesno(
            "Break Finished ☕",
            f"{self.cycle} টি Pomodoro শেষ হয়েছে।\n"
            "আরেকটা সাইকেল শুরু করবে?"
        )

        if answer:

            self.start_focus()

        else:

            self.finish_session()


    # ========================================================
    # SESSION FINISHED
    # ========================================================

    def finish_session(self):

        messagebox.showinfo(
            "Session Completed 🎉",
            f"আজকে মোট {self.cycle} টি "
            "Pomodoro সাইকেল শেষ হয়েছে।"
        )

        print()
        print(
            f"Session Ended | "
            f"Total Cycles: {self.cycle}"
        )

        self.root.destroy()


    # ========================================================
    # QUIT
    # ========================================================

    def quit_app(self):

        answer = messagebox.askyesno(
            "Quit Pomodoro",
            "Pomodoro বন্ধ করতে চাও?"
        )

        if answer:

            print()
            print("Pomodoro App Closed")

            self.root.destroy()


# ============================================================
# MAIN ENTRY POINT
# ============================================================

def main():

    root = tk.Tk()

    app = PomodoroApp(root)

    root.mainloop()


# ============================================================
# DIRECT EXECUTION
# ============================================================

if __name__ == "__main__":
    main()
