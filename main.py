#coding:gb2312
from tkinter import *


class gui(object):
    def __init__(self,master=None,*args,**kwargs):
        #声明tk变量
        self.root = Tk()
        self.x,self.y = 0,0
        self.bg = '#F8F8FF'
        self.font = ('Fixdsys',13)

        #四个控件
        self.cha = Canvas(self.root,width=35,height=35,bg=self.bg,borderwidth=0)
        self.question = Label(self.root,text='你最爱的人是不是我?',font=self.font,bg=self.bg)
        self.yes = Button(self.root,text='是的',font=self.font,width=10,borderwidth=1,bg=self.bg)
        self.no = Button(self.root,text='不是',font=self.font,width=10,borderwidth=1,bg=self.bg)

        self.set_root()
        self.set_widget()

        self.root.mainloop()

    def set_root(self):
        '''
        配置主窗口
        '''
        self.root.overrideredirect(True)
        self.root.config(bg='#F8F8FF')

        w,h = 500,200
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        self.x = (ws//2) - (w//2)
        self.y = (hs//2) - (h//2)
        self.root.geometry(f'{w}x{h}+{self.x}+{self.y}')

    def set_widget(self):
        '''
        配置里面的控件
        '''
        def change_word(event):
            '''
            鼠标进入事件，改变按钮显示的文本
            '''
            print(f'进入Enter事件,widget{event.widget["text"]}')
            a = event.widget['text']
            event.widget.config(bg='#7FFFAA')

            if a == '不是':
                event.widget.config(text='是的')
                if self.yes is event.widget:
                    self.no.config(text='不是')
                elif self.no is event.widget:
                    self.yes.config(text='不是')

        s_n = 1
        def move(event):
            '''
            移动不是的按钮，根据s_n的值，只移动两次，一上一下
            '''
            nonlocal s_n
            if s_n == 1:
                self.no.place(relx=0.7,rely=0.3)
                s_n += 1
            elif s_n == 2:
                self.no.place(relx=0.7,rely=0.7)
                self.no.unbind('<Enter>')
                self.no.bind('<Enter>',change_word)

        def change_end(event):
            '''
            鼠标离开按钮，背景色恢复
            '''
            event.widget.config(bg='#F8F8FF')

        def _top(string):
            '''
            用来提供创建子窗口的方法
            '''
            t = Toplevel()
            t.geometry(f'400x150+{self.x}+{self.y}')
            #t.overrideredirect(True)
            t.config(bg='#F8F8FF')
            Label(t,text=string,font=self.font,bg=self.bg).place(relx=0.2,rely=0.15)
            def top_f(event):
                nonlocal t
                t.destroy()
            b = Button(t,text='确定',font=self.font,bg=self.bg,width=10)
            b.bind('<Button-1>',top_f)
            b.place(relx=0.6,rely=0.65)


        def top(event):
            '''
            点击了文本为 是的 的按钮
            '''
            if event.widget['text'] == '是的':
                _top('就知道你喜欢我!')

        def cha_f(event):
            '''
            点击了 关闭
            '''
            _top('关闭窗口也改变不了\n你喜欢我的事实!')


        #空间绑定事件
        self.yes.bind('<Enter>',change_word)
        self.no.bind('<Enter>',move)
        self.yes.bind('<Leave>',change_end)
        self.no.bind('<Leave>',change_end)
        self.yes.bind('<Button-1>',top)
        self.no.bind('<Button-1>',top)
        self.cha.bind('<Button-1>',cha_f)
        #画关闭的两条线
        self.cha.create_line(0,0,35,35,fill='#8B4513',width=2)
        self.cha.create_line(35,0,0,35,fill='#8B4513',width=2)
        #控件布局
        self.cha.place(relx=0.85,rely=0.08)
        self.question.place(relx=0.15,rely=0.2)
        self.yes.place(relx=0.40,rely=0.7)
        self.no.place(relx=0.70,rely=0.7)

if __name__ == "__main__":
    a = gui()





