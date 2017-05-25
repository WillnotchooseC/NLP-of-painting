from Tkinter import *
import FGrammar
import turtle
import MyTurtle
import sentence
import wx


class InitialUI(object):
    def __init__(self):
        self.root = Tk()
        self.root.minsize(600, 300)
        self.string = ''
        self.frame = Frame(self.root)
        self.frame.pack()
        self.acceptInput()

    def acceptInput(self):
        r = self.frame
        k = Label(r, text='Please input your command:', font=("Helvetica", 14))
        k.pack(side='top')
        w = Label(r, text='Be careful to your spelling !!! \n This software can process '
                          'the sentence like : \n''"Please draw a red circle on the '
                          'left"''\n''"I want to draw a red circle on the right"''\n'
                          '"A red circle on the left"''\n If you are unwilling to set '
                          'the color, the default color will be black.''',
                  font=("Helvetica", 11))
        w.pack(side='bottom')
        self.e = Entry(r, text='Name', width=60)
        self.e.pack(side='left')
        self.e.focus_set()
        b = Button(r, text='Engage', width=10, height=1, command=self.gettext)
        b.pack(side='right')

    def gettext(self):
        self.string = self.e.get()
        self.root.destroy()

    def getString(self):
        return self.string

    def waitForInput(self):
        self.root.mainloop()

    def getText(self):
        # msgBox = takeInput(requestMessage)
        # loop until the user makes a decision and the window is destroyed
        self.waitForInput()
        return self.getString()


ap = InitialUI()
var = ap.getText()
# print var
Fg = FGrammar.FGrammar()
# print str(Fg.Analysis(var))
stc = sentence.Extracting(str(Fg.Analysis(var)))

print stc.ExtractGra(), stc.ExtractDir(), stc.ExtractColor()
Jog = MyTurtle.MyTurtle()
if (stc.ExtractColor() == None):
    Jog.RunningTurtle(stc.ExtractGra(), stc.ExtractDir(), "black")
else:
    Jog.RunningTurtle(stc.ExtractGra(), stc.ExtractDir(), stc.ExtractColor())
turtle.getscreen()._root.mainloop()

# Execute = Fg.Analysis(var)
# print Execute
# if(Execute):
# t = MyTurtle.MyTurtle()
# t.drawCircle(-500,0,"black")
# ta = turtle.Screen()
# ta.exitonclick()
