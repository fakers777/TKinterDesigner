import tkinter
import tkinter.ttk
def SetupStyle():
    style = tkinter.ttk.Style()
    style.configure(".TLabel",background="#46a1ef",foreground="#ffffff")
    style.configure(".TButton",background="#46a1ef",foreground="#ffffff",activebackground="#eeeeee",activeforeground="#ffffff")
    style.configure(".TEntry",background="#46a1ef",foreground="#ffffff")
    style.configure(".TText",background="#46a1ef",foreground="#ffffff")
    style.configure(".TProgressbar",background="#46a1ef",troughcolor="#ffffff")
    style.configure(".TScrollbar",background="#46a1ef",troughcolor="#ffffff")
    style.configure(".TPanedWindow",background="#46a1ef",foreground="#ffffff",bordercolor="#46a1ef")
    style.configure(".TLabelframe",background="#46a1ef",foreground="#ffffff")
    style.configure(".TListbox",background="#46a1ef",foreground="#ffffff")
    style.configure(".TCanvas",background="#46a1ef")
    style.configure(".TFrame",background="#46a1ef")
    style.configure(".TCheckbutton",background="#46a1ef",foreground="#ffffff",activebackground="#46a1ef",activeforeground="#ffffff")
    style.configure(".TRadiobutton",background="#46a1ef",foreground="#ffffff",activebackground="#46a1ef",activeforeground="#ffffff")
    style.configure(".TSpinbox",background="#46a1ef",foreground="#ffffff")
    style.configure(".TScale",background="#46a1ef",foreground="#ffffff",bordercolor="#46a1ef")
    style.configure(".Treeview",background="#46a1ef",foreground="#ffffff",fieldbackground="#46a1ef")
    style.configure(".Treeview.Heading",background="#46a1ef",foreground="#ffffff",fieldbackground="#46a1ef")
    style.map("TNotebook.Tab", background=[("active","#46a1ef"),("selected", "#46a1ef")], fieldbackground=[("selected", "#46a1ef")], activebackground=[("selected","#46a1ef")], foreground=[("selected", "#ffffff")])
    style.configure(".TNotebook.Tab",background="#46a1ef",foreground="#ffffff",fieldbackground="#46a1ef")
    if 'combostyle' not in style.theme_names():
        style.theme_create('combostyle', parent='alt',
                            settings={'TCombobox':
                                        {'configure':
                                            {
                                                'foreground': '#ffffff',
                                                'selectbackground': '#eeeeee',   # 选择后的背景颜色   
                                                'fieldbackground': '#46a1ef',  #  下拉框颜色
                                                'background': '#46a1ef',     # 背景颜色
                                                "font":10,   # 字体大小
                                                "font-weight": "bold"
                                            }
                                        },

                                      'Treeview':
                                        {'configure':
                                            {
                                                'foreground': '#ffffff',
                                                'selectbackground': '#eeeeee',   # 选择后的背景颜色
                                                'fieldbackground': '#46a1ef',  #  下拉框颜色
                                                'background': '#46a1ef',     # 背景颜色
                                                "font":10,   # 字体大小
                                                "font-weight": "bold"
                                            }
                                        },

                                      'Treeview.Heading':
                                        {'configure':
                                            {
                                                'foreground': '#ffffff',
                                                'selectbackground': '#eeeeee',   # 选择后的背景颜色
                                                'fieldbackground': '#46a1ef',  #  下拉框颜色
                                                'background': '#46a1ef',     # 背景颜色
                                                "font":10,   # 字体大小
                                                "font-weight": "bold"
                                            }
                                        },

                                      'TNotebook':
                                        {'configure':
                                            {
                                                'foreground': '#ffffff',
                                                'selectbackground': '#eeeeee',   # 选择后的背景颜色
                                                'fieldbackground': '#46a1ef',  #  下拉框颜色
                                                'background': '#46a1ef',     # 背景颜色
                                                "font":10,   # 字体大小
                                                "font-weight": "bold"
                                            }
                                        },

                                      'TProgressbar':
                                        {'configure':
                                            {
                                                'troughcolor': '#46a1ef',   # 滚动条颜色
                                                'background': '#ffffff'     # 背景颜色
                                            }
                                        },

                                      'TScrollbar':
                                        {'configure':
                                            {
                                                'troughcolor': '#46a1ef',   # 滚动条颜色
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
    style.configure(NoteBookStyle, background = "#46a1ef")
    style.configure(NoteBookStyle, selectbackground = "#46a1ef")
    style.configure(NoteBookStyle, fieldbackground = "#46a1ef")
    style.configure(NoteBookStyle+".Tab", background = "#46a1ef")
    style.configure(NoteBookStyle+".Tab", foreground = "#ffffff")
    notebook.config(style=NoteBookStyle)