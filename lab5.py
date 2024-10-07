from turtle import Turtle
from math import pi, sqrt, atan
from stack import print_frame
Number = int | float
def square(t: 'Turtle', length: Number)->None:
    """square(t, length) Uses a specific turtle to draw a square of a given side length"""
    #draws four lines offset 90 degrees from each other
    for i in range(4):
        t.fd(length)
        t.rt(90)
def polygon(t: 'Turtle', length: Number, n:int)->None:
    """polygon(t, length, n) Uses a specific turtle to draw a regular polygon of a given side length with n sides"""
    # print_frame('Polygon', locals())
    #draws n lines offset 360 / n degrees from each other
    for i in range(n):
        t.fd(length)
        """the angle between the turtles current heading and the heading of the next side, at the end of a side, the
        turtle is facing the outside of the shape with the next side to its right, so it needs to turn along the
        shape's exterior angle, which is given by this formula"""
        angle:Number = 360 /n
        t.rt(angle)
        # print_frame('Polygon', locals())
def circle(t:'Turtle',r:Number)->None:
    """circle(t, r) Uses a specific turtle to draw a circle with radius r"""
    # print_frame('Circle',locals())
    circumference:Number=pi*2*r
    # print_frame('Circle', locals())
    #the side lengths of a 100 sided polygon with equal perimeter to the circle
    side_length:Number=circumference/100
    # print_frame('Circle', locals())
    #approximates the circle with a 100 sided polygon
    polygon(t,side_length,100)
def partial_polygon(t:'Turtle',length:Number,n:int,portion:float)->None:
    """partial_polygon(t, length, n, portion) Uses a specific turtle to draw part of (the n * portion sides of) an n-sided regular polygon"""
    # draws n * portion lines offset 360 / n degrees from each other
    angle: Number = 360 / n
    for i in range(round(n * portion)):
        t.fd(length)
        """the angle between the turtles current heading and the heading of the next side, at the end of a side, the
        turtle is facing the outside of the shape with the next side to its right, so it needs to turn along the
        shape's exterior angle, which is given by this formula"""
        t.rt(angle)
def arc(t:'Turtle',r:Number,angle:Number)->None:
    """arc(t, r, angle) Uses a specific turtle to draw an arc with radius r and spanning angle degrees"""
    circumference:Number=pi*2*r
    #the side lengths of a 100 sided polygon with equal perimeter to circle the arc comes from
    side_length:Number=circumference/100
    circle_fraction:Number = angle / 360
    #approximates the arc with part of 100 sided polygon
    partial_polygon(t,side_length,100,circle_fraction)
def parabola_points(width:Number,height:Number, points:int)->tuple[tuple[Number,Number],...]:
    """parabola_points(width, height, points) Returns a tuple containing a series of points along the length of a parabola
    width: width of the parabola
    height: the center height of the parabola
    points: the number of points to compute"""
    #the equation for this parabola is a(x^2) + bx
    a:Number=-4*height/width**2
    b:Number=4*height/width
    spacing:Number=width/(points-1)
    return_points:tuple=()
    for i in range(points):
        x:Number=i*spacing
        y:Number=a*x**2+b*x
        return_points = return_points + ((x,y),)
    return return_points
def parabola_lines(width:Number,height:Number)->tuple[tuple[Number,Number],...]:
    """parabola_lines(width, height) Returns the length and heading of a series of lines approximating a parabola, these are designed to be turtle instructions that will allow it to trace the parabola
    width: the width of the parabola
    height: the height of the parabola"""
    points:tuple=parabola_points(width,height,101)
    lines:tuple=()
    index:int=0
    for point_set in points[0:-1]:
        x1:Number=point_set[0]
        y1:Number=point_set[1]
        x2:Number=points[index+1][0]
        y2: Number = points[index + 1][1]
        length:Number = sqrt((x2-x1)**2+(y2-y1)**2)
        slope:Number=(y2-y1)/(x2-x1)
        radian_heading:Number=atan(slope)
        #atan gives results in radians
        heading:Number=radian_heading*180/pi
        lines = lines + ((length,heading),)
        index = index + 1
    return lines
def parabola(t,width:Number,height:Number)->None:
    """parabola(t, width, height) Uses a specific turtle to draw a parabola
    t: the turtle
    width: the width of the parabola
    height: the height of the parabola"""
    #this allows the parabola to be oriented relative to the turtle's start orientation
    start_heading:Number=t.heading()
    lines:tuple=parabola_lines(width,height)
    for line in lines:
        t.setheading(start_heading+line[1])
        t.fd(line[0])
if __name__=='__main__':
    t = Turtle()
    t.speed(0)
    # square(t, 50)
    # square(t, 100)
    # square(t,150)
    # polygon(t,50,3)
    # polygon(t,100,5)
    # polygon(t,150,6)
    # circle(t,50)
    # circle(t,100)
    # circle(t,150)
    # partial_polygon(t,100,6,1/2)
    # partial_polygon(t,200,10,4/5)
    # partial_polygon(t,100,9,2/3)
    # arc(t,50,90)
    # arc(t,100,30)
    # arc(t,150,200)
    # parabola(t,100,100)
    # parabola(t,100,50)
    # parabola(t,300,200)
    t.screen.mainloop()