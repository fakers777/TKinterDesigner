import tkinter
import tkinter.ttk
def SetupStyle():
    style = tkinter.ttk.Style()
    style.configure(".TLabel",background="#2b2b2b",foreground="#ffffff")
    style.configure(".TButton",background="#2b2b2b",foreground="#ffffff",activebackground="#eeeeee",activeforeground="#ffffff")
    style.configure(".TEntry",background="#2b2b2b",foreground="#ffffff")
    style.configure(".TText",background="#2b2b2b",foreground="#ffffff")
    style.configure(".TProgressbar",background="#2b2b2b",troughcolor="#ffffff")
    style.configure(".TScrollbar",background="#2b2b2b",troughcolor="#ffffff")
    style.configure(".TPanedWindow",background="#2b2b2b",foreground="#ffffff",bordercolor="#2b2b2b")
    style.configure(".TLabelframe",background="#2b2b2b",foreground="#ffffff")
    style.configure(".TListbox",background="#2b2b2b",foreground="#ffffff")
    style.configure(".TCanvas",background="#2b2b2b")
    style.configure(".TFrame",background="#2b2b2b")
    style.configure(".TCheckbutton",background="#2b2b2b",foreground="#ffffff",activebackground="#2b2b2b",activeforeground="#ffffff")
    style.configure(".TRadiobutton",background="#2b2b2b",foreground="#ffffff",activebackground="#2b2b2b",activeforeground="#ffffff")
    style.configure(".TSpinbox",background="#2b2b2b",foreground="#ffffff")
    style.configure(".TScale",background="#2b2b2b",foreground="#ffffff",bordercolor="#2b2b2b")
    style.configure(".Treeview",background="#2b2b2b",foreground="#ffffff",fieldbackground="#2b2b2b")
    style.configure(".Treeview.Heading",background="#2b2b2b",foreground="#ffffff",fieldbackground="#2b2b2b")
    style.map("TNotebook.Tab", background=[("active","#2b2b2b"),("selected", "#2b2b2b")], fieldbackground=[("selected", "#2b2b2b")], activebackground=[("selected","#2b2b2b")], foreground=[("selected", "#ffffff")])
    style.configure(".TNotebook.Tab",background="#2b2b2b",foreground="#ffffff",fieldbackground="#2b2b2b")
    if 'combostyle' not in style.theme_names():
        style.theme_create('combostyle', parent='alt',
                            settings={'TCombobox':
                                        {'configure':
                                            {
                                                'foreground': '#ffffff',
                                                'selectbackground': '#eeeeee',   # 选择后的背景颜色   
                                                'fieldbackground': '#2b2b2b',  #  下拉框颜色
                                                'background': '#2b2b2b',     # 背景颜色
                                                "font":10,   # 字体大小
                                                "font-weight": "bold"
                                            }
                                        },

                                      'Treeview':
                                        {'configure':
                                            {
                                                'foreground': '#ffffff',
                                                'selectbackground': '#eeeeee',   # 选择后的背景颜色
                                                'fieldbackground': '#2b2b2b',  #  下拉框颜色
                                                'background': '#2b2b2b',     # 背景颜色
                                                "font":10,   # 字体大小
                                                "font-weight": "bold"
                                            }
                                        },

                                      'Treeview.Heading':
                                        {'configure':
                                            {
                                                'foreground': '#ffffff',
                                                'selectbackground': '#eeeeee',   # 选择后的背景颜色
                                                'fieldbackground': '#2b2b2b',  #  下拉框颜色
                                                'background': '#2b2b2b',     # 背景颜色
                                                "font":10,   # 字体大小
                                                "font-weight": "bold"
                                            }
                                        },

                                      'TNotebook':
                                        {'configure':
                                            {
                                                'foreground': '#ffffff',
                                                'selectbackground': '#eeeeee',   # 选择后的背景颜色
                                                'fieldbackground': '#2b2b2b',  #  下拉框颜色
                                                'background': '#2b2b2b',     # 背景颜色
                                                "font":10,   # 字体大小
                                                "font-weight": "bold"
                                            }
                                        },

                                      'TProgressbar':
                                        {'configure':
                                            {
                                                'troughcolor': '#2b2b2b',   # 滚动条颜色
                                                'background': '#ffffff'     # 背景颜色
                                            }
                                        },

                                      'TScrollbar':
                                        {'configure':
                                            {
                                                'troughcolor': '#2b2b2b',   # 滚动条颜色
                                                'background': '#ffffff'     # 背景颜色
                                            }
                                        }
                                     }
                            )
    style.theme_use('combostyle')
    return style

def ResetNotebook(notebook,style):
    NoteBookStyle = "PyMe.TNotebook"
    style.configure(NoteBookStyle, relief='sunken')
    style.configure(NoteBookStyle+".Heading", relief="flat")
    style.configure(NoteBookStyle, background = "#2b2b2b")
    style.configure(NoteBookStyle, selectbackground = "#2b2b2b")
    style.configure(NoteBookStyle, fieldbackground = "#2b2b2b")
    style.configure(NoteBookStyle+".Tab", background = "#2b2b2b")
    style.configure(NoteBookStyle+".Tab", foreground = "#ffffff")
    notebook.config(style=NoteBookStyle)