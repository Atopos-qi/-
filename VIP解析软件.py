import ttkbootstrap as ttk
import webbrowser

def Play():
    word = word_va.get()
    link = 'https://www.8090g.cn/?url=' + word
    webbrowser.open(link)


#实例化创建应用程序窗口
root = ttk.Window(
        title="VIP解析软件",        #设置窗口的标题
        themename="litera",     #设置主题
        size=(758,160),        #窗口的大小
)
root.place_window_center()    #让显现出的窗口居中
root.resizable(False,False)   #让窗口不可更改大小
root.iconbitmap('play.ico') # 加logo图标
Label_frame = ttk.Frame(root)
Label_frame.pack(pady=20)
ttk.Label(Label_frame, text='VIP 解 析 软 件', font=("微软雅黑", 30, 'bold')).pack()
input_frame = ttk.Frame(root)
input_frame.pack()
word_va = ttk.StringVar()
ttk.Label(input_frame, text='视 频 链 接:', font=("微软雅黑", 20, 'bold')).pack(side=ttk.LEFT)
entry = ttk.Entry(input_frame, width=50, font=("微软雅黑", 10, 'bold'), textvariable=word_va)
entry.pack(side=ttk.LEFT, padx=10)
ttk.Button(input_frame, text='播 放', command=Play).pack(side=ttk.LEFT)
ttk.Button(input_frame, text="清 空", command=lambda: entry.delete(0, ttk.END)).pack(side=ttk.LEFT, padx=5)



root.mainloop()