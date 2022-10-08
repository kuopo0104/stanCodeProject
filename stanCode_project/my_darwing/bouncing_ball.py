"""
File: 
Name:Neil
-------------------------
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
dot = GOval(SIZE, SIZE, x=START_X, y=START_Y)
window = GWindow(800, 500, title='bouncing_ball.py')
A = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    window.add(dot)
    onmouseclicked(move)


def move(_):
    """
    The only function of clicking mouse is moving the ball from(START_X, START_Y), if the number of click is above 3, locking the location of the ball.
    """
    global A
    vy = 0
    t = 0
    v0 = 0
    if dot.x == START_X and A < 3:
        A += 1
        while True:
            if dot.x >= window.width:
                break
            elif dot.x != window.width and dot.y >= window.height + SIZE:
                v0 = -vy*0.9
                t = 0
                vy = v0 + GRAVITY * t
                dot.move(VX, vy)
            else:
                vy = v0 + GRAVITY * t
                dot.move(VX, vy)
                t += 1
            pause(DELAY)
        dot.x = START_X
        dot.y = START_Y


if __name__ == "__main__":
    main()
