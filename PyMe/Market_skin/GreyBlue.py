import tkinter
import tkinter.ttk
def SetupStyle():
    style = tkinter.ttk.Style()
    style.configure(".TLabel",background="#22272e",foreground="#adbac7")
    style.configure(".TButton",background="#22272e",foreground="#adbac7",activebackground="#444c56",activeforeground="#adbac7")
    style.configure(".TEntry",background="#22272e",foreground="#adbac7")
    style.configure(".TText",background="#22272e",foreground="#adbac7")
    style.configure(".TProgressbar",background="#22272e",troughcolor="#adbac7")
    style.configure(".TScrollbar",background="#22272e",troughcolor="#adbac7")
    style.configure(".TPanedWindow",background="#22272e",foreground="#adbac7",bordercolor="#22272e")
    style.configure(".TLabelframe",background="#22272e",foreground="#adbac7")
    style.configure(".TListbox",background="#22272e",foreground="#adbac7")
    style.configure(".TCanvas",background="#22272e")
    style.configure(".TFrame",background="#22272e")
    style.configure(".TCheckbutton",background="#22272e",foreground="#adbac7",activebackground="#22272e",activeforeground="#adbac7")
    style.configure(".TRadiobutton",background="#22272e",foreground="#adbac7",activebackground="#22272e",activeforeground="#adbac7")
    style.configure(".TSpinbox",background="#22272e",foreground="#adbac7")
    style.configure(".TScale",background="#22272e",foreground="#adbac7",bordercolor="#22272e")
    style.configure(".Treeview",background="#22272e",foreground="#adbac7",fieldbackground="#22272e")
    style.configure(".Treeview.Heading",background="#22272e",foreground="#adbac7",fieldbackground="#22272e")
    style.map("TNotebook.Tab", background=[("active","#22272e"),("selected", "#22272e")], fieldbackground=[("selected", "#22272e")], activebackground=[("selected","#22272e")], foreground=[("selected", "#adbac7")])
    style.configure(".TNotebook.Tab",background="#22272e",foreground="#adbac7",fieldbackground="#22272e")
    if 'combostyle' not in style.theme_names():
        style.theme_create('combostyle', parent='alt',
                            settings={'TCombobox':
                                        {'configure':
                                            {
                                                'foreground': '#adbac7',
                                                'selectbackground': '#444c56',   # 选择后的背景颜色   
                                                'fieldbackground': '#22272e',  #  下拉框颜色
                                                'background': '#22272e',     # 背景颜色
                                                "font":10,   # 字体大小
                                                "font-weight": "bold"
                                            }
                                        },
                                      'Treeview.Heading':
                                        {'configure':
                                            {
                                                'foreground': '#adbac7',
                                                'selectbackground': '#444c56',   # 选择后的背景颜色
                                                'fieldbackground': '#22272e',  #  下拉框颜色
                                                'background': '#22272e',     # 背景颜色
                                                "font":10,   # 字体大小
                                                "font-weight": "bold"
                                            }
                                        },
                                      'Treeview':
                                        {'configure':
                                            {
                                                'foreground': '#adbac7',
                                                'selectbackground': '#444c56',   # 选择后的背景颜色
                                                'fieldbackground': '#22272e',  #  下拉框颜色
                                                'background': '#22272e',     # 背景颜色
                                                "font":10,   # 字体大小
                                                "font-weight": "bold"
                                            }
                                        },

                                      'TNotebook':
                                        {'configure':
                                            {
                                                'foreground': '#adbac7',
                                                'selectbackground': '#444c56',   # 选择后的背景颜色
                                                'fieldbackground': '#22272e',  #  下拉框颜色
                                                'background': '#22272e',     # 背景颜色
                                                "font":10,   # 字体大小
                                                "font-weight": "bold"
                                            }
                                        },

                                      'TProgressbar':
                                        {'configure':
                                            {
                                                'troughcolor': '#22272e',   # 滚动条颜色
                                                'background': '#adbac7'     # 背景颜色
                                            }
                                        },

                                      'TScrollbar':
                                        {'configure':
                                            {
                                                'troughcolor': '#22272e',   # 滚动条颜色
                                                'background': '#adbac7'     # 背景颜色
                                            }
                                        },

                                      'TScrollbar':
                                        {'configure':
                                            {
                                                'troughcolor': '#22272e',   # 滚动条颜色
                                                'background': '#adbac7'     # 背景颜色
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
    style.configure(NoteBookStyle, background = "#22272e")
    style.configure(NoteBookStyle, selectbackground = "#22272e")
    style.configure(NoteBookStyle, fieldbackground = "#22272e")
    style.configure(NoteBookStyle+".Tab", background = "#22272e")
    style.configure(NoteBookStyle+".Tab", foreground = "#adbac7")
    notebook.config(style=NoteBookStyle)