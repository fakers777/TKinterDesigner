from ttkbootstrap import Style
from tkinter import ttk

def SetupStyle():
    style = Style(theme = "lumen")
    return style

def EditModeStyle():

    style = ttk.Style()

    style.configure(".TLabel",background="#ffffff",foreground="#000000")

    style.configure(".TButton",background="#158cba",foreground="#ffffff",activebackground="#158cba",activeforeground="#ffffff")

    style.configure(".TEntry",background="#ffffff",foreground="#000000")

    style.configure(".TText",background="#ffffff",foreground="#000000")

    style.configure(".TProgressbar",background="#ffffff",foreground="#000000")

    style.configure(".TPanedWindow",background="#ffffff",foreground="#000000",bordercolor="#ffffff")

    style.configure(".TLabelframe",background="#ffffff",foreground="#000000")

    style.configure(".TListbox",background="#ffffff",foreground="#000000")

    style.configure(".TCanvas",background="#ffffff")

    style.configure(".TCheckbutton",background="#ffffff",foreground="#000000",activebackground="#ffffff",activeforeground="#000000")

    style.configure(".TRadiobutton",background="#ffffff",foreground="#000000",activebackground="#ffffff",activeforeground="#000000")

    style.configure(".TSpinbox",background="#ffffff",foreground="#000000",activebackground="#ffffff",activeforeground="#000000")

    style.configure(".TScale",background="#ffffff",foreground="#000000",bordercolor="#ffffff")
    
    style.configure(".TFrame",background="#ffffff")

    return style



def ResetNotebook(notebook,style):

    NoteBookStyle = "PyMe.TNotebook"

    style.configure(NoteBookStyle, relief='sunken')

    style.configure(NoteBookStyle+".Heading", relief="flat")

    style.configure(NoteBookStyle, background = "#ffffff")

    style.configure(NoteBookStyle, selectbackground = "#ffffff")

    style.configure(NoteBookStyle, fieldbackground = "#ffffff")

    style.configure(NoteBookStyle+".Tab", background = "#ffffff")

    style.configure(NoteBookStyle+".Tab", foreground = "#000000")

    notebook.config(style=NoteBookStyle)