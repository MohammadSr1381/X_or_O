from hebbNetwork import HebbNetwork
import tkinter as tk
import matplotlib as plt
import pandas
import copy

class TestGui :

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("test new data")
        self.window.configure(bg="honeydew2")
        self.window.geometry("600x400")
        self.button_states = [[-1 for _ in range(5)] for _ in range(5)]
        self.needed_elements()
        self.pattern_creation()
        self.window.mainloop()


        
    def needed_elements(self):
        
        frame = tk.Frame(self.window, padx=30, pady=30)
        frame.pack()

        label = tk.Label(frame, text="create your pattern" , font=("Helvetica", 20), padx=10 , pady=10)
        label.config()
        label.pack()

        button_frame = tk.Frame(self.window, bg="honeydew2")
        button_frame.pack(side="bottom", fill="both")

        button_save = tk.Button(button_frame , text="Save", bg="lightblue" , command= self.save)
        button_save.pack(side="left" , padx=10 , pady=10 , anchor="center")
        
        button_exit = tk.Button(button_frame , text="Exit" , bg="lightcoral" , command=exit)
        button_exit.pack(side="left", padx=10 , pady=10 , anchor="center")


        
    def pattern_creation(self):   
        
        pattern_frame = tk.Frame(self.window , bg="honeydew2")
        pattern_frame.pack(side="top" , anchor="center")
        self.buttons = []
        self.button_states = [] 


        for i in range(5) :
            
            button_row = []
            button_states_row =[]
            
            for j in range(5):
                
                button_click = tk.Button(pattern_frame , bg="black")
                button_click.grid(column=j , row=i , padx=10 , pady=10)
                button_row.append(button_click)
                button_states_row.append(-1)
                button_click.config(command=lambda btn=button_click, r=i, c=j: self.toggle_button(btn, r, c))
            self.buttons.append(button_row)
            self.button_states.append(button_states_row)
        
        
        
    def toggle_button(self , button , row , col):
        
        if button["bg"] == "black":
            button["bg"] = "white"
            self.button_states[row][col] = 1 
        else:
            button["bg"] = "black"
            self.button_states[row][col] = -1  
            
                
                
    def save(self):

        
        
        test_list = self.button_states
        network = HebbNetwork()
        test = network.classify(test_list)
        
        new_window = tk.Toplevel(self.window) 
        new_window.title("X_OR_O")
        
        if test ==True :
            final_label = tk.Label(new_window , text="the pattern is X")
            final_label.pack()
        else :
            final_label = tk.Label(new_window , text="the pattern is O")
            final_label.pack()
    
        for i in range(len(self.button_states)):
            for j in range(len(self.button_states[i])):
                    
                    self.button_states[i][j] = -1
                    self.buttons[i][j].config(bg = "black")
             