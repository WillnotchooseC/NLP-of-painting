import turtle
import wx


########################################################################
class MyTurtle(turtle.Turtle):
    """"""

    # ----------------------------------------------------------------------
    def __init__(self):
        """Turtle Constructor"""

        turtle.Turtle.__init__(self, shape="turtle")
        turtle.bgcolor("orange")
        screen = turtle.Screen();
        # wx.Frame.__init__(self, size=(600,300))


        # ----------------------------------------------------------------------
        # def setBackground(self,color):
        # self.bgcolor(color)

    # ----------------------------------------------------------------------
    def drawCircle(self, x, y, color, radius=50):
        """
        Moves the turtle to the correct position and draws a circle
        """
        self.penup()
        self.setposition(x, y)
        self.width(2.5)
        self.speed(10)
        self.pendown()
        # self.begin_fill()
        self.color(color)
        self.circle(radius)
        self.hideturtle()
        # self.end_fill()

    # ----------------------------------------------------------------------
    def drawSquare(self, x, y, color):
        self.penup()
        self.setposition(x, y)
        self.width(2.5)
        self.speed(10)
        self.pendown()
        self.begin_fill()
        self.color(color)
        self.forward(100)
        self.left(90)
        self.forward(100)
        self.left(90)
        self.forward(100)
        self.left(90)
        self.forward(100)
        self.end_fill()
        self.hideturtle()

    # ----------------------------------------------------------------------
    def drawDart(self, x, y, color):
        self.penup()
        self.setposition(x, y)
        self.width(2.5)
        self.speed(10)
        self.pendown()
        self.begin_fill()
        self.color(color)
        for i in range(10):
            for i in range(2):
                self.forward(50)
                self.right(60)
                self.forward(50)
                self.right(120)
            self.right(36)
        self.hideturtle()

    # ----------------------------------------------------------------------
    def drawRectangle(self, x, y, color):
        self.penup()
        self.setposition(x, y)
        self.width(2.5)
        self.speed(10)
        self.pendown()
        self.begin_fill()
        self.color(color)
        self.forward(100)
        self.left(90)
        self.forward(200)
        self.left(90)
        self.forward(100)
        self.left(90)
        self.forward(200)
        self.end_fill()
        self.hideturtle()

    # ----------------------------------------------------------------------
    def drawLadder(self, x, y, color):
        self.penup()
        self.setposition(x, y)
        self.width(2.5)
        self.speed(10)
        self.pendown()
        self.begin_fill()
        self.color(color)
        self.forward(100)
        self.left(60)
        self.forward(100)
        self.left(60)
        self.forward(100)
        self.end_fill()
        self.hideturtle()

        # ----------------------------------------------------------------------

    def draw_fractal(self, length, depth):
        if depth == 1:
            self.forward(length)
        else:
            self.draw_fractal(length, depth - 1)
            self.right(60)
        if depth == 1:
            self.forward(length)
        else:
            self.draw_fractal(length, depth - 1)
            self.left(120)
        if depth == 1:
            self.forward(length)
        else:
            self.draw_fractal(length, depth - 1)
            self.right(60)
        if depth == 1:
            self.forward(length)
        else:
            self.draw_fractal(length, depth - 1)

    # ----------------------------------------------------------------------
    def drawSnowflake(self, x, y, color):
        length = 7
        depth = 4
        self.color(color)
        self.penup()
        self.setposition(x, y)
        self.width(5)
        self.pendown()
        self.draw_fractal(length, depth - 1)
        self.left(120)
        self.draw_fractal(length, depth - 1)
        self.left(120)
        self.draw_fractal(length, depth - 1)
        self.hideturtle()

    # ----------------------------------------------------------------------
    def drawTriangle(self, x, y, color):
        self.penup()
        self.setposition(x, y)
        self.width(2.5)
        self.speed(10)
        self.pendown()
        self.begin_fill()
        self.color(color)
        self.forward(150)
        self.left(120)
        self.forward(150)
        self.left(120)
        self.forward(150)
        self.end_fill()
        self.hideturtle()

    # ----------------------------------------------------------------------
    def drawStar(self, x, y, color):

        angle = 120
        self.penup()
        self.setposition(x, y)
        self.width(2.5)
        self.speed(10)
        self.begin_fill()
        self.pendown()
        self.color(color)

        count = 0
        angle = 144
        while count <= 5:
            self.forward(200)
            self.right(angle)

            count += 1
        self.end_fill()
        self.hideturtle()


        # for side in range(5):
        # self.begin_fill()
        # self.forward(70)
        # self.right(angle)
        # self.forward(70)
        # self.right(72 - angle)

        # self.end_fill()

    # ----------------------------------------------------------------------
    def drawSmileFace(self, x, y):

        self.width(3)

        self.color("green")
        self.begin_fill()
        self.penup()
        self.setposition(x-100,y-100)
        self.down()
        self.goto(x-100, y+100)
        self.goto(x+100, y+100)
        self.goto(x+100, y-100)
        self.goto(x-100, y-100)
        self.end_fill()

        self.up()
        self.goto(x-40, y+40)
        self.color("blue")
        self.down()
        self.begin_fill()
        self.circle(10)
        self.end_fill()
        self.up()
        self.goto(x+40, y+40)
        self.down()
        self.begin_fill()
        self.circle(10)
        self.end_fill()

        self.up()
        self.color("red")
        self.goto(x-60, y-40)
        self.down()
        self.goto(x-60, y-60)
        self.goto(x+60, y-60)
        self.goto(x+60, y-40)
        self.up()

        self.goto(x, y)
        self.color("black")
        self.down()
        self.goto(x-20, y-20)
        self.goto(x+5, y-20)
        self.up()
        self.hideturtle()

    # ----------------------------------------------------------------------

    def drawOlympicSymbol(self, x, y):

        self.width(3)
        positions = [(x, y, "blue"), (x - 120, 0, "yellow"), (x + 60, y + 60, "red"),
                 (x - 60, y + 60, "green"), (x - 180, y + 60, "purple")]
        for x, y, color in positions:
             self.drawCircle(x, y, color)
        self.hideturtle()


    def RunningTurtle(self, graph, position, color):
        horizontal = 0
        vertical = 0
        if (position == 'left'):
           horizontal = -500
           vertical = 0
        if (position == 'right'):
           horizontal = 500
           vertical = 0
        if (position == 'top'):
           horizontal = 0
           vertical = 150
        if (position == 'bottom'):
           horizontal = 0
           vertical = -150
        if (position == 'middle'):
           horizontal = 0
           vertical = 0
        print horizontal, vertical, position
    # "circle" | "triangle" | "rectangle" | "square" | "star" | "OlympicSymbol" | "ladder"

    # color = 'black'
        if (graph == 'circle'):
           self.drawCircle(horizontal, vertical, color)
        if (graph == 'triangle'):
           self.drawTriangle(horizontal, vertical, color)
        if (graph == 'rectangle'):
           self.drawRectangle(horizontal, vertical, color)
        if (graph == 'square'):
           self.drawSquare(horizontal, vertical, color)
        if (graph == 'star'):
           self.drawStar(horizontal - 100, vertical, color)
        if (graph == 'OlympicSymbol'):
           self.drawOlympicSymbol(horizontal, vertical)
        if (graph == 'ladder'):
           self.drawLadder(horizontal, vertical, color)
        if (graph == 'snowflake'):
           self.drawSnowflake(horizontal - 150, vertical, color)
        if (graph == 'smileface'):
           self.drawSmileFace(horizontal , vertical)
        if (graph == 'dart'):
           self.drawDart(horizontal , vertical, color)

if __name__ == "__main__":
    t = MyTurtle()
    #t.setBackground("lightblue")
    t.drawOlympicSymbol(0, 0)
    t.drawCircle(-500, 0, "black")
    t.drawSquare(0, 150, "red")
    t.drawRectangle(0, -150, "gray")
    t.drawStar(500, 0, "skyblue")
    t.drawLadder(500, 150, "green")
    t.drawTriangle(-500, 150, "lightyellow")
    t.drawSnowflake(-200, -100, "red")
    t.drawDart(0, -100, "blue")
    t.drawSmileFace(0,0)
    turtle.getscreen()._root.mainloop()
