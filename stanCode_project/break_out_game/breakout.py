"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    # Add the animation loop here!
    ball = graphics.ball
    paddle = graphics.paddle
    window = graphics.window
    dx = graphics.get_dx()
    dy = graphics.get_dy()
    while True:
        ball.move(dx, dy)
        obj = window.get_object_at(ball.x, ball.y)
        if obj == paddle:
            dy = -dy
        elif ball.x >= window.width or ball.x <= 0:
            dx = -dx
        elif ball.y >= window.height or ball.y <= 0:
            dy = -dy
        else:
            window.remove(obj)
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
