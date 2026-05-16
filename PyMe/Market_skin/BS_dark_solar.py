from ttkbootstrap import Style
from tkinter import ttk

def SetupStyle():
    style = Style(theme = "solar")
    return style

def EditModeStyle():

    style = ttk.Style()

    style.configure(".TLabel",background="#002b36",foreground="#ffffff")

    style.configure(".TButton",background="#bc951a",foreground="#ffffff",activebackground="#bc951a",activeforeground="#ffffff")

    style.configure(".TEntry",background="#002b36",foreground="#ffffff")

    style.configure(".TText",background="#002b36",foreground="#ffffff")

    style.configure(".TProgressbar",background="#002b36",foreground="#ffffff")

    style.configure(".TPanedWindow",background="#002b36",foreground="#ffffff",bordercolor="#002b36")

    style.configure(".TLabelframe",background="#002b36",foreground="#ffffff")

    style.configure(".TListbox",background="#002b36",foreground="#ffffff")

    style.configure(".TCanvas",background="#002b36")

    style.configure(".TCheckbutton",background="#002b36",foreground="#ffffff",activebackground="#002b36",activeforeground="#ffffff")

    style.configure(".TRadiobutton",background="#002b36",foreground="#ffffff",activebackground="#002b36",activeforeground="#ffffff")

    style.configure(".TSpinbox",background="#002b36",foreground="#ffffff",activebackground="#002b36",activeforeground="#ffffff")

    style.configure(".TScale",background="#002b36",foreground="#ffffff",bordercolor="#002b36")
    
    style.configure(".TFrame",background="#002b36")

    return style


def ResetNotebook(notebook,style):

    NoteBookStyle = "PyMe.TNotebook"

    style.configure(NoteBookStyle, relief='sunken')

    style.configure(NoteBookStyle+".Heading", relief="flat")

    style.configure(NoteBookStyle, background = "#002b36")

    style.configure(NoteBookStyle, selectbackground = "#002b36")

    style.configure(NoteBookStyle, fieldbackground = "#002b36")

    style.configure(NoteBookStyle+".Tab", background = "#002b36")

    style.configure(NoteBookStyle+".Tab", foreground = "#ffffff")

    notebook.config(style=NoteBookStyle)