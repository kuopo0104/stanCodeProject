"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):
        self.b_r = ball_radius
        self.p_w = paddle_width
        self.p_h = paddle_height
        self.p_off = paddle_offset
        self.br_row = brick_rows
        self.br_col = brick_cols
        self.br_w = brick_width
        self.br_h = brick_height
        self.br_off = brick_offset
        self.br_spa = brick_spacing

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.window.add(self.paddle, x=(self.window.width-paddle_width)/2, y=self.window.height-paddle_offset)
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius, ball_radius)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.window.add(self.ball, x=(self.window.width-self.ball.width)/2, y=(self.window.height-self.ball.height)/2)
        # Default initial velocity for the ball
        self.__dx = random.randint(1, MAX_X_SPEED)
        if (random.random()> 0.5):
            self.__dx = -self.__dx
        self.__dy = INITIAL_Y_SPEED
        # Initialize our mouse listeners
        onmousemoved(self.pad_move)
        onmouseclicked(self.bal_move)
        # Draw bricks
        a = -self.br_w-self.br_spa
        for i in range(brick_cols):
            b = self.br_off
            self.bri = GRect(self.br_w, self.br_h)
            self.window.add(self.bri, x=a, y=b)
            a = a + self.br_spa + self.br_w
            for j in range(brick_rows-1):
                b = b + self.br_spa + self.br_h
                self.bri2 = GRect(self.br_w, self.br_h)
                self.window.add(self.bri2, x=a, y=b)
        self.bri3 = GRect(self.br_w, self.br_h)
        self.window.add(self.bri3, x=(self.br_col-1)*(self.br_w+self.br_spa), y=self.br_off)

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def pad_move(self, mouse):
        if self.paddle.x <= 0:
            self.paddle.x = self.paddle.x+self.paddle.width-mouse.x
        self.paddle.x = mouse.x - self.paddle.width / 2

    def bal_move(self, _):
        if self.ball.x == (self.window.width-self.ball.width)/2 and self.ball.y == (self.window.height-self.ball.height)/2:
            pass








