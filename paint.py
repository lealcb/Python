from tkinter import *
from tkinter.colorchooser import askcolor


class Paint(object):

    DEFAULT_PEN_SIZE = 5.0
    DEFAULT_COLOR = 'white'

    def __init__(self):
        self.root = Tk()

        self.botao_caneta = Button(self.root, text='Caneta', command=self.use_pen)
        self.botao_caneta.grid(row=0, column=0)

        self.botao_pincel = Button(self.root, text='Pincel', command=self.use_brush)
        self.botao_pincel.grid(row=0, column=1)

        self.botao_cor = Button(self.root, text='Cor', command=self.choose_color)
        self.botao_cor.grid(row=0, column=2)

        self.botao_borracha = Button(self.root, text='Borracha', command=self.use_eraser)
        self.botao_borracha.grid(row=0, column=3)

        self.botao_escolhe_tamanho = Scale(self.root, from_=1, to=2.0, orient=HORIZONTAL)
        self.botao_escolhe_tamanho.grid(row=0, column=4)

        self.c = Canvas(self.root, bg='black', width=600, height=600)
        self.c.grid(row=1, columnspan=5)

        self.setup()
        self.root.mainloop()

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.line_width = self.botao_escolhe_tamanho.get()
        self.color = self.DEFAULT_COLOR
        self.eraser_on = False
        self.active_button = self.botao_caneta
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)

    def use_pen(self):
        self.activate_button(self.botao_caneta)

    def use_brush(self):
        self.activate_button(self.botao_pincel)

    def choose_color(self):
        self.eraser_on = False
        self.color = askcolor(color=self.color)[1]

    def use_eraser(self):
        self.activate_button(self.botao_borracha, eraser_mode=True)

    def activate_button(self, some_button, eraser_mode=False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode

    def paint(self, event):
        self.line_width = self.botao_escolhe_tamanho.get()
        paint_color = 'white' if self.eraser_on else self.color
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=self.line_width, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x, self.old_y = None, None


if __name__ == '__main__':
    Paint()