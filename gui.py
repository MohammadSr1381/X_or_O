import tkinter as tk
import pandas

class Gui :

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Dataset Creator")
        self.window.configure(bg="honeydew2")
        self.window.geometry("600x400")
        self.button_states = [[-1 for _ in range(5)] for _ in range(5)]
        self.flag = False
        self.needed_elements()
        self.pattern_creation()
        self.flag_situation()
        self.window.mainloop()
        
    
   
    def flag_situation(self):
        
        flag_frame = pandas.read_csv("dataset.csv")
        if flag_frame.empty():
            pass
        else :
            self.flag = True
        
    def needed_elements(self):
        
        frame = tk.Frame(self.window, padx=30, pady=30)
        frame.pack()

        label = tk.Label(frame, text="create your pattern" , font=("Helvetica", 20), padx=10 , pady=10)
        label.config()
        label.pack()

        button_frame = tk.Frame(self.window, bg="honeydew2")
        button_frame.pack(side="bottom", fill="both")

        button_save_x = tk.Button(button_frame , text="Save as X", bg="lightblue" , command= self.save_as_x)
        button_save_x.pack(side="left" , padx=10 , pady=10 , anchor="center")
        
        button_save_o = tk.Button(button_frame , text="Save as O", bg="lightblue" , command= self.save_as_o)
        button_save_o.pack(side="left" , padx=10 , pady=10 , anchor="center")
        
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
            
                
                
    def save_as_x(self):

        dataset_dic ={"label" : 1 , "data" : self.button_states}
        data_frame = pandas.DataFrame([dataset_dic])  
        print(dataset_dic)
        
        if not self.flag : 
            data_frame = data_frame.to_csv("dataset.csv" , index=False , mode="w") 
            self.flag = True 
        else :
            data_frame = data_frame.to_csv("dataset.csv" , index=False , header=False , mode="a")
        print(self.button_states)
    
        for i in range(len(self.button_states)):
            for j in range(len(self.button_states[i])):
                    
                    self.button_states[i][j] = -1
                    self.buttons[i][j].config(bg = "black")
                    
        
    
    def save_as_o(self):
        
        dataset_dic ={"label" : -1 , "data" : self.button_states}
        data_frame = pandas.DataFrame([dataset_dic])  
        print(dataset_dic)
        
        if not self.flag : 
            data_frame = data_frame.to_csv("dataset.csv" , index=False , mode="w") 
            self.flag = True 
        else :
            data_frame = data_frame.to_csv("dataset.csv" , index=False , header=False , mode="a")
        print(self.button_states)
    
        for i in range(len(self.button_states)):
            for j in range(len(self.button_states[i])):
                    
                    self.button_states[i][j] = -1
                    self.buttons[i][j].config(bg = "black")
                    
        








