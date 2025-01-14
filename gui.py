import tkinter as tk
import random

class CricketGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Cricket Game")
        self.root.geometry("500x400")

        # Game State Variables
        self.team_a_score = 0
        self.team_b_score = 0
        self.team_a_wickets = 0
        self.team_b_wickets = 0
        self.current_team = "Team A"
        self.balls = 0
        self.max_overs = 2
        self.ball_limit = self.max_overs * 6
        self.innings = 1

        # Widgets
        self.label_status = tk.Label(root, text="Welcome to the Cricket Game!", font=("Arial", 14))
        self.label_status.pack(pady=10)

        self.button_toss = tk.Button(root, text="Toss", command=self.toss)
        self.button_toss.pack(pady=10)

        self.button_play = tk.Button(root, text="Play Ball", command=self.play_ball, state=tk.DISABLED)
        self.button_play.pack(pady=10)

        self.label_score = tk.Label(root, text="Score: 0/0", font=("Arial", 12))
        self.label_score.pack(pady=10)

        self.label_commentary = tk.Label(root, text="Commentary: ", font=("Arial", 10))
        self.label_commentary.pack(pady=10)

        self.button_restart = tk.Button(root, text="Restart Game", command=self.restart_game, state=tk.DISABLED)
        self.button_restart.pack(pady=10)

    def toss(self):
        toss_result = random.choice(["Team A", "Team B"])
        self.current_team = toss_result
        self.label_status.config(text=f"{toss_result} won the toss and will bat first!")
        self.button_toss.config(state=tk.DISABLED)
        self.button_play.config(state=tk.NORMAL)

    def play_ball(self):
        if self.balls >= self.ball_limit:
            self.switch_innings()
            return

        outcome = random.choice(["0", "1", "2", "4", "6", "W"])
        self.balls += 1
        if outcome == "W":
            if self.current_team == "Team A":
                self.team_a_wickets += 1
            else:
                self.team_b_wickets += 1
            commentary = f"WICKET! {self.current_team} lost a wicket."
        else:
            runs = int(outcome)
            if self.current_team == "Team A":
                self.team_a_score += runs
            else:
                self.team_b_score += runs
            commentary = f"{self.current_team} scored {runs} runs!"

        self.update_score()
        self.label_commentary.config(text=f"Commentary: {commentary}")

    def update_score(self):
        if self.current_team == "Team A":
            score_text = f"Score: {self.team_a_score}/{self.team_a_wickets}"
        else:
            score_text = f"Score: {self.team_b_score}/{self.team_b_wickets}"
        self.label_score.config(text=score_text)

    def switch_innings(self):
        if self.innings == 1:
            self.innings += 1
            if self.current_team == "Team A":
                self.current_team = "Team B"
                self.balls = 0
                self.label_status.config(text="Team B is now batting.")
            else:
                self.current_team = "Team A"
                self.balls = 0
                self.label_status.config(text="Team A is now batting.")
        else:
            self.declare_winner()

    def declare_winner(self):
        if self.team_a_score > self.team_b_score:
            winner = "Team A"
        elif self.team_b_score > self.team_a_score:
            winner = "Team B"
        else:
            winner = "No one! It's a tie!"
        self.label_status.config(text=f"Game Over! The winner is {winner}.")
        self.button_play.config(state=tk.DISABLED)
        self.button_restart.config(state=tk.NORMAL)

    def restart_game(self):
        self.team_a_score = 0
        self.team_b_score = 0
        self.team_a_wickets = 0
        self.team_b_wickets = 0
        self.current_team = "Team A"
        self.balls = 0
        self.innings = 1

        self.label_status.config(text="Welcome to the Cricket Game!")
        self.label_score.config(text="Score: 0/0")
        self.label_commentary.config(text="Commentary: ")
        self.button_toss.config(state=tk.NORMAL)
        self.button_play.config(state=tk.DISABLED)
        self.button_restart.config(state=tk.DISABLED)


# Create the main window
root = tk.Tk()
game = CricketGameGUI(root)
root.mainloop()
