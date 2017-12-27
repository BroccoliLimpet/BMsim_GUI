import tkinter as tk

# define 'LARGE_FONT'
LARGE_FONT = ("Verdana", 12)    

# define class 'BMapp', inheriting 'Tk' from tkinter
class BMapp(tk.Tk): 
    
    # intialise class
    def __init__(self, *args, **kwargs):     
        
        # initialise inherited class 'Tk'
        tk.Tk.__init__(self, *args, **kwargs)   
        
        # define container
        container = tk.Frame(self)        
        container.pack(side="top", fill="both", expand = True)        
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        # define dictionary
        self.frames = {}
        frame = StartPage(container, self)
        self.frames[StartPage] = frame
        
        frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame(StartPage)
    
    # define method to show frame 'cont'    
    def show_frame(self, controller):
        frame = self.frames[controller]
        frame.tkraise
        
# define 'StartPage', inheriting  'Frame' from tkinter
class StartPage(tk.Frame):
    
    # initialise class
    def __init__(self, parent, controller):
        # initialise tk.Frame
        tk.Frame.__init__(self, parent)
        # define label for the start page
        label = tk.Label(self, text="This is the start page", font=LARGE_FONT)
        # pack label into window, with some padding
        label.pack(pady=10,padx=10)
        
app = BMapp()
app.mainloop()
