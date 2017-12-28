import tkinter as tk
import numpy as np

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
        container.pack(side = "top", fill = "both", expand = True)        
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        
        # define dictionary
        self.frames = {}
        
        # add the different frames to dictionary
        for F in (StartPage,PageOne):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")
        
        # show StartPage after initialise
        self.show_frame(StartPage)
    
    # define method to bring desired frame to front  
    def show_frame(self, controller):
        frame = self.frames[controller]
        frame.tkraise()
    
    
# def RandomNumber():
#     print(np.random.randn(1))
    
        
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
        
        # add button to start page
        button1 = tk.Button(self, text = "Visit page one",
                            command = lambda: controller.show_frame(PageOne))
        button1.pack()
        


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        
        label = tk.Label(self, text= "This is page one", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        button1 = tk.Button(self, text="Back to start page",
                            command = lambda: controller.show_frame(StartPage))
        button1.pack()
    

    
    
app = BMapp()
app.mainloop()

