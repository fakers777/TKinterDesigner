import tkinter
import tkinter.ttk
def SetupStyle():
    style = tkinter.ttk.Style()
    style.configure(".TLabel",background="#333333",foreground="#b8860b")
    style.configure(".TButton",background="#333333",foreground="#b8860b",activebackground="#000000",activeforeground="#b8860b")
    style.configure(".TEntry",background="#333333",foreground="#b8860b")
    style.configure(".TText",background="#333333",foreground="#b8860b")
    style.configure(".TProgressbar",background="#333333",troughcolor="#b8860b")
    style.configure(".TScrollbar",background="#333333",troughcolor="#b8860b")
    style.configure(".TPanedWindow",background="#333333",foreground="#b8860b",bordercolor="#333333")
    style.configure(".TLabelframe",background="#333333",foreground="#b8860b")
    style.configure(".TListbox",background="#333333",foreground="#b8860b")
    style.configure(".TCanvas",background="#333333")
    style.configure(".TFrame",background="#333333")
    style.configure(".TCheckbutton",background="#333333",foreground="#b8860b",activebackground="#333333",activeforeground="#b8860b")
    style.configure(".TRadiobutton",background="#333333",foreground="#b8860b",activebackground="#333333",activeforeground="#b8860b")
    style.configure(".TSpinbox",background="#333333",foreground="#b8860b")
    style.configure(".TScale",background="#333333",foreground="#b8860b",bordercolor="#333333")
    style.configure(".Treeview",background="#333333",foreground="#b8860b",fieldbackground="#333333")
    style.configure(".Treeview.Heading",background="#333333",foreground="#b8860b",fieldbackground="#333333")
    style.map("TNotebook.Tab", background=[("active","#333333"),("selected", "#333333")], fieldbackground=[("selected", "#333333")], activebackground=[("selected","#333333")], foreground=[("selected", "#b8860b")])
    style.configure(".TNotebook.Tab",background="#333333",foreground="#b8860b",fieldbackground="#333333")
    if 'combostyle' not in style.theme_names():
        style.theme_create('combostyle', parent='alt',
                            settings={'TCombobox':
                                        {'configure':
                                            {
                                                'foreground': '#b8860b',
                                                'selectbackground': 'black',   # 选择后的背景颜色   
                                                'fieldbackground': '#333333',  #  下拉框颜色
                                                'background': '#333333',     # 背景颜色
                                                "font":10,   # 字体大小
                                                "font-weight": "bold"
                                            }
                                        },

                                      'Treeview':
                                        {'configure':
                                            {
                                                'foreground': '#b8860b',
                                                'selectbackground': 'black',   # 选择后的背景颜色
                                                'fieldbackground': '#333333',  #  下拉框颜色
                                                'background': '#333333',     # 背景颜色
                                                "font":10,   # 字体大小
                                                "font-weight": "bold"
                                            }
                                        },

                                      'Treeview.Heading':
                                        {'configure':
                                            {
                                                'foreground': '#b8860b',
                                                'selectbackground': 'black',   # 选择后的背景颜色
                                                'fieldbackground': '#333333',  #  下拉框颜色
                                                'background': '#333333',     # 背景颜色
                                                "font":10,   # 字体大小
                                                "font-weight": "bold"
                                            }
                                        },

                                      'TNotebook':
                                        {'configure':
                                            {
                                                'foreground': '#b8860b',
                                                'selectbackground': 'black',   # 选择后的背景颜色
                                                'fieldbackground': '#333333',  #  下拉框颜色
                                                'background': '#333333',     # 背景颜色
                                                "font":10,   # 字体大小
                                                "font-weight": "bold"
                                            }
                                        },

                                      'TProgressbar':
                                        {'configure':
                                            {
                                                'troughcolor': '#333333',   # 滚动条颜色
                                                'background': '#b8860b'     # 背景颜色
                                            }
                                        },

                                      'TScrollbar':
                                        {'configure':
                                            {
                                                'troughcolor': '#333333',   # 滚动条颜色
                                                'background': '#b8860b'     # 背景颜色
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
    style.configure(NoteBookStyle, background = "#333333")
    style.configure(NoteBookStyle, selectbackground = "#333333")
    style.configure(NoteBookStyle, fieldbackground = "#333333")
    style.configure(NoteBookStyle+".Tab", background = "#333333")
    style.configure(NoteBookStyle+".Tab", foreground = "#b8860b")
    notebook.config(style=NoteBookStyle)
