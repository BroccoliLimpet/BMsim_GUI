import tkinter as tk

LARGE_FONT = ("Verdana", 12)

class BMapp(tk.TK):
    
    def __init__(self, *args, **kwargs):
        
        tk.TK__init__(self, *args, **kwargs)
        
        container = tk.Frame(self)        
        container.pack(side="top", fill="both", expand = True)        
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        frame = StartPage(container, self)
        self.frames[StartPage] = frame
        
        frame.grid(row=0, column=0, sticky="nsew")
        
        self.showframe(StartPage)
        
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise
        
class StartPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="This is the start page", font=LARGEFONT)
        label.pack(pady=10,padx=10)
        
app = BMapp()
app.mainloop()
        