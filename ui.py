from tkinter import *
import tkinter
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
true_path = 'images/true.png'
false_path = 'images/false.png'

class QuizInterface:
    # pass a data object of Quizbrain as quiz_brain
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.configure(bg=THEME_COLOR, padx=20, pady=20)
        
        self.canvas = Canvas(height = 250, width = 300, bg='white')
        self.text = self.canvas.create_text(125,120,text='Hello',font=('arial',15,'italic'), width = 250)
        self.canvas.grid(row=1, column=0, columnspan=2,sticky=(W,E), pady=50)

        true_img = PhotoImage(file=true_path)
        self.true_button = Button(image=true_img,border=0,highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row =2, column=0,padx=20, pady=20)
        
        false_img = PhotoImage(file=false_path)
        self.false_button = Button(image=false_img,border=0,highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row =2, column=1,padx=20, pady=20)
        self.score = tkinter.StringVar()
        self.score.set("Score: 0")
        self.score_text = Label(textvariable=self.score,bg=THEME_COLOR, fg='white').grid(row=0,column=1)
        self.get_next_question()
        

        self.window.mainloop()
        
    def get_next_question(self): 
        self.canvas.config(bg="white")
        self.score.set(f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question() 
            self.canvas.itemconfig(self.text, text=q_text)
        else:
            self.canvas.itemconfig(self.text, text="You have answered all the questions.")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def true_pressed(self):
        is_right = self.quiz.check_answer(user_answer="True")
        self.feedback(is_right)


    def false_pressed(self):
        is_right = self.quiz.check_answer(user_answer="False")
        self.feedback(is_right)


    def feedback(self,is_right):
        if is_right:           
            self.canvas.config(bg="green")
            self.window.after(1000, self.get_next_question)
        else:
            self.canvas.config(self.canvas, bg="red")
            self.window.after(1000, self.get_next_question)


        
# everything needs to go before mainloop

