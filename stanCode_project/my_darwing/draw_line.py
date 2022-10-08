"""
File: draw_line
Name:Neil
-------------------------
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked


world = GWindow()
P1 = 0
P2 = 0
A = 0
dot = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(put_dot)


def put_dot(m):
    """
    if the number of click is odd, put a dot and mark the location of it,else,draw a line between the second location and the dot.
    """
    global A
    global P1
    global P2
    global dot
    A += 1
    if A % 2 == 1:
        dot = GOval(10, 10, x=m.x-5, y=m.y-5)
        world.add(dot)
        P1 = m.x
        P2 = m.y
    else:
        line = GLine(P1, P2, m.x, m.y)
        world.add(line)
        world.remove(dot)


# def put_dot(m):
#     global A
#     global P1
#     global P2
#     A += 1
#     if A % 2 == 1:
#         dot = GOval(10, 10, x=m.x-5, y=m.y-5)
#         world.add(dot)
#         P1 = m.x
#         P2 = m.y
#     else:
#         line = GLine(P1, P2, m.x, m.y)
#         world.add(line)
#         dot = world.get_object_at(P1, P2)
#         world.remove(dot)


if __name__ == "__main__":
    main()
