import tkinter as tk
import random

class ColorGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Color Game")
        
        self.colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown']
        
        self.score = 0
        
        self.color_label = tk.Label(self.root, text="", font=("Helvetica", 18))
        self.color_label.pack(pady=20)
        
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)
        
        self.buttons = []
        for color in self.colors:
            button = tk.Button(self.button_frame, text=color, width=10, command=lambda c=color: self.check_answer(c))
            button.pack(side=tk.LEFT, padx=5)
            self.buttons.append(button)
        
        self.status_label = tk.Label(self.root, text="")
        self.status_label.pack(pady=10)
        
        self.update_color()
        
        self.root.mainloop()
    
    def update_color(self):
        color_name = random.choice(self.colors)
        color_value = random.choice(self.colors)
        self.color_label.config(text=color_name, fg=color_value)
    
    def check_answer(self, selected_color):
        correct_color = self.color_label.cget('text')
        if selected_color == correct_color:
            self.score += 1
            self.status_label.config(text="Correct!", fg="green")
        else:
            self.status_label.config(text="Incorrect!", fg="red")
        self.status_label.after(1000, self.clear_status)
        self.update_color()
    
    def clear_status(self):
        self.status_label.config(text="")

if __name__ == "__main__":
    game = ColorGame()
