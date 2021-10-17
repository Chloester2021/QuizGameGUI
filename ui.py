from tkinter import *
import tkinter
from quiz_brain import QuizBrain
from data import Question_data
from question_model import Question

THEME_COLOR = "#375362"
true_path = 'images/true.png'
false_path = 'images/false.png'
refresh_path = 'images/download.png'

class QuizInterface:
    def __init__(self):
        self.question = Question
        self.get_new_list()
        self.quiz = QuizBrain(self.question_bank)


        self.window=Tk()
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
        
        refresh_img = PhotoImage(file=refresh_path).subsample(10,10)
        self.refresh_button = Button(image=refresh_img,border=0,highlightthickness=0,command=self.refresh_pressed)
        self.refresh_button.grid(row =0, column=0)

        self.score = tkinter.StringVar()
        self.score.set("Score: 0")
        self.score_text = Label(textvariable=self.score,bg=THEME_COLOR, fg='white').grid(row=0,column=1)
        self.get_next_question()
        

        self.window.mainloop()


    def get_new_list(self):
        self.question_bank = []
        self.new_questions = Question_data().question_data
        for n in self.new_questions:
            self.question_text = n["question"]
            self.question_answer = n["correct_answer"]
            new_question = self.question(self.question_text, self.question_answer)
            self.question_bank.append(new_question)
        
    def get_next_question(self): 
        self.canvas.config(bg="white")
        self.score.set(f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question() 
            self.canvas.itemconfig(self.text, text=q_text)
            self.refresh_button.config(state='disabled')
        else:
            self.canvas.itemconfig(self.text, text="You have answered all the questions. Press refresh to start again.")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')
            self.refresh_button.config(state='active')

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

    def refresh_pressed(self):
        self.score.set(f"Score: 0")
        self.true_button.config(state='active')
        self.false_button.config(state='active')
        self.refresh_button.config(state='disabled')
        self.quiz.score = 0
        self.question_bank = []
        self.get_new_list()
        self.quiz = QuizBrain(self.question_bank)
        self.get_next_question()



# everything needs to go before mainloop

