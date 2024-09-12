import tkinter as tk

class personalityTest(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
    
    def create_widgets(self):
        self.questions = [
            "1. What describes you the best?",
            "2. What do you do for fun?",
            "3. Admit something."
        ]
        self.options = [
            ["ambitious go-getter.", "nervous around most people.", "Happy around people!", "I love my community, but not huge crowds"],
            ["something outdoors", "working hard on making things happen", "just doing my hobbies", "mainly listening to music and staring at the ceiling."],
            ["I'm scared", "I'm actually faking it", "I think about my friends more than they think about me", "I haven't showered in multiple days lol" ]
        ]
        self.labels = []
        self.buttons = []
        for i in range(len(self.questions)):
            question_label = tk.Label(self, text = self.questions[i])
            question_label.pack()
            self.labels.append(question_label)

            var = tk.StringVar(value=self.options[i][0])
            for option in self.options[i]:  #RadioButton
                button = tk.RADIOBUTTON(self, text = option, variable = var, value = option)
                button.pack()
                self.buttons.append(button)

        self.submit_button = tk.Button(self, text="Submit", command=self.submit)
        self.submit_button.pack()
    
    def submit(self):
        q1 = self.buttons[0].cget("text")
        q2 = self.buttons[1].cget("text")
        q3 = self.buttons[3].cget("text")

        if q1 == "ambitious go-getter." and q2 == "working hard on making things happen":
            adviceType = "Let someone else have the spotlight for once."
        elif q1 == "nervous around most people." and q2 == "just doing my hobbies" or q2 == "mainly listening to music and staring at the ceiling.":
            adviceType = "Don't be afraid to ask someone for help."
        elif q1 == "Happy around people!" and q2 == "just doing my hobbies" or q2 == "working hard on making things happen":
            adviceType = "Take some quiet time for thinking thoughts"
        elif q1 == "I love my community, but not huge crowds" and q2 == "something outdoors" or q2 == "just doing my hobbies":
            adviceType = "Bring your happiness to someone today"
        else:
            adviceType = "Do what you need to do, and then order your favorite food"
        
        self.result_label.configure(text=f"{adviceType}")
root = tk.Tk()
app = personalityTest(master=root)
app.mainloop()
        
        