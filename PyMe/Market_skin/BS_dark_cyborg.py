from ttkbootstrap import Style
from tkinter import ttk

def SetupStyle():
    style = Style(theme = "cyborg")
    return style


def EditModeStyle():

    style = ttk.Style()

    style.configure(".TLabel",background="#060606",foreground="#ffffff")

    style.configure(".TButton",background="#2a9fd6",foreground="#ffffff",activebackground="#2a9fd6",activeforeground="#ffffff")

    style.configure(".TEntry",background="#060606",foreground="#ffffff")

    style.configure(".TText",background="#060606",foreground="#ffffff")

    style.configure(".TProgressbar",background="#060606",foreground="#ffffff")

    style.configure(".TPanedWindow",background="#060606",foreground="#ffffff",bordercolor="#060606")

    style.configure(".TLabelframe",background="#060606",foreground="#ffffff")

    style.configure(".TListbox",background="#060606",foreground="#ffffff")

    style.configure(".TCanvas",background="#060606")

    style.configure(".TCheckbutton",background="#060606",foreground="#ffffff",activebackground="#060606",activeforeground="#ffffff")

    style.configure(".TRadiobutton",background="#060606",foreground="#ffffff",activebackground="#060606",activeforeground="#ffffff")

    style.configure(".TSpinbox",background="#060606",foreground="#ffffff",activebackground="#060606",activeforeground="#ffffff")

    style.configure(".TScale",background="#060606",foreground="#ffffff",bordercolor="#060606")
    
    style.configure(".TFrame",background="#060606")

    return style

def ResetNotebook(notebook,style):
    NoteBookStyle = "PyMe.TNotebook"
    style.configure(NoteBookStyle, relief='sunken')
    style.configure(NoteBookStyle+".Heading", relief="flat")
    style.configure(NoteBookStyle, background = "#060606")
    style.configure(NoteBookStyle, selectbackground = "#060606")
    style.configure(NoteBookStyle, fieldbackground = "#060606")
    style.configure(NoteBookStyle+".Tab", background = "#060606")
    style.configure(NoteBookStyle+".Tab", foreground = "#ffffff")
    notebook.config(style=NoteBookStyle)