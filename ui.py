THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain
class Ui(Tk):
    def __init__(self, quiz_brain: QuizBrain):
        super().__init__()
        self.config(padx=20, pady=20, bg=THEME_COLOR)
        self.title('Quiz brain')
        self.quiz = quiz_brain
        self.label = Label(text='score:0', fg='black', bg=THEME_COLOR, font=('Arial', 30, 'bold'))
        self.label.grid(column=2, row=0)
        self.canvas = Canvas(width=500, height=450, highlightthickness=0)
        self.question = self.canvas.create_text(250, 225, text=f'Question', font=('Arial', 20, 'italic'), width=300)
        self.canvas.grid(column=0, row=1, columnspan=3, pady=50, padx=50)
        image_wrong = PhotoImage(file='false.png')
        self.button = Button(image=image_wrong, highlightthickness=0)
        self.button.grid(column=0, row=2)
        image_right = PhotoImage(file='true.png')
        self.but = Button(image=image_right, highlightthickness=0)
        self.but.grid(column=2, row=2)
        self.nextquestion()
        self.false = "False"
        self.true = "True"
        self.mainloop()
    def nextquestion(self):
        self.canvas.config(bg='white')
        self.button.config(command=self.evaluate)
        self.but.config(command=self.evaluate_right)
        if self.quiz.still_has_questions():
            q1 = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q1)
        else:
            self.canvas.itemconfig(self.question, text=f'Game completed')
            self.button.config(command=self.zero)
            self.but.config(command=self.zero)
            self.but.destroy()
            self.button.destroy()
    def evaluate(self):
        score = self.quiz.check_answer(self.false)
        if score:
            self.label.config(self.label, text=f'score:{score}')
            self.nextquestion()
        else:
            self.canvas.itemconfig(bg='green')
            self.after(1000, self.nextquestion)
    def evaluate_right(self):
        score = self.quiz.check_answer(self.true)
        if score:
            self.label.config(self.label, text=f'score:{score}')
            self.nextquestion()
        else:
            self.canvas.config(bg='red')
            self.after(1000, self.nextquestion)
    def zero(self):
        pass