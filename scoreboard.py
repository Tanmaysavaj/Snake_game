from turtle import Turtle,Screen



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.text_turtle = Turtle()
        self.text_turtle.hideturtle()
        self.text_turtle.penup()
        self.text_turtle.color("white")
        self.text_turtle.goto(0, 260)
        self.text_turtle.write(f"Score : {self.score}",align="center",font=("Arial",24,"bold"))


    def score_update(self):
        self.text_turtle.clear()
        self.score += 1
        self.text_turtle.write(f"Score : {self.score}",align="center",font=("Arial",24,"bold"))


    def game_over(self):
        self.text_turtle.goto(0,0)
        self.text_turtle.write("Game Over!",align="center",font=("Arial",24,"bold"))