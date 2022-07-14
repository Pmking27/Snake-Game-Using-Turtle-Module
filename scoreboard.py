from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        with open("high score.text","r" ) as hs:
            self.high_score=int(hs.read())
        self.color("white")
        self.penup()
        self.goto(0,310)
        self.text_of_scoreboard()
        
    def text_of_scoreboard(self):
        self.write(f"Score : {self.score}          High Score : {self.high_score}" , align="center",font=("Arial",20,"normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high score.text","w" ) as hs:
                hs.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()    


    def update_scoreboard(self):
        self.clear()
        self.score += 1
        self.text_of_scoreboard()