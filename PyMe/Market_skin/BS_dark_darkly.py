from ttkbootstrap import Style
from tkinter import ttk

def SetupStyle():
    style = Style(theme = "darkly")
    return style

def EditModeStyle():

    style = ttk.Style()

    style.configure(".TLabel",background="#222222",foreground="#dde3e9")

    style.configure(".TButton",background="#375a7f",foreground="#dde3e9",activebackground="#375a7f",activeforeground="#dde3e9")

    style.configure(".TEntry",background="#222222",foreground="#dde3e9")

    style.configure(".TText",background="#222222",foreground="#dde3e9")

    style.configure(".TProgressbar",background="#222222",foreground="#dde3e9")

    style.configure(".TPanedWindow",background="#222222",foreground="#dde3e9",bordercolor="#222222")

    style.configure(".TLabelframe",background="#222222",foreground="#dde3e9")

    style.configure(".TListbox",background="#222222",foreground="#dde3e9")

    style.configure(".TCanvas",background="#222222")

    style.configure(".TCheckbutton",background="#222222",foreground="#dde3e9",activebackground="#222222",activeforeground="#dde3e9")

    style.configure(".TRadiobutton",background="#222222",foreground="#dde3e9",activebackground="#222222",activeforeground="#dde3e9")

    style.configure(".TSpinbox",background="#222222",foreground="#dde3e9",activebackground="#222222",activeforeground="#dde3e9")

    style.configure(".TScale",background="#222222",foreground="#dde3e9",bordercolor="#222222")
    
    style.configure(".TFrame",background="#222222")

    return style


def ResetNotebook(notebook,style):

    NoteBookStyle = "PyMe.TNotebook"

    style.configure(NoteBookStyle, relief='sunken')

    style.configure(NoteBookStyle+".Heading", relief="flat")

    style.configure(NoteBookStyle, background = "#222222")

    style.configure(NoteBookStyle, selectbackground = "#222222")

    style.configure(NoteBookStyle, fieldbackground = "#222222")

    style.configure(NoteBookStyle+".Tab", background = "#222222")

    style.configure(NoteBookStyle+".Tab", foreground = "#dde3e9")

    notebook.config(style=NoteBookStyle)