"""
File: my_drawing
Name:Neil
----------------------
"""

from campy.graphics.gobjects import GOval, GRect, GLabel, GPolygon, GArc
from campy.graphics.gwindow import GWindow


def main():
    """
    Title:著色師畫到一半就罷工的安妮雅

    來自Spy x family 安妮雅經典顏藝
    """
    window = GWindow(width=800, height=500, title='123')
    face = GOval(1200, 920, x=150, y=-390)
    window.add(face)
    eye_l = GArc(150, 100, 0, 180)
    eye_l.filled = True
    eye_l.fill_color = 'white'
    window.add(eye_l, x=300, y=130)
    eye_r = GArc(150, 100, 0, 180)
    eye_r.filled=True
    eye_r.fill_color = 'white'
    window.add(eye_r, x=600, y=130)
    window.add(eye_l, x=300, y=130)
    mouth = GArc(300, 200, 180, 180)
    mouth.filled = True
    mouth.fill_color = 'white'
    window.add(mouth, x=375, y=220)
    nose = GPolygon()
    nose.add_vertex((520, 210))
    nose.add_vertex((520, 220))
    window.add(nose)
    hair = GOval(1300, 1900, x=10, y=-500)
    window.add(hair)
    shaba = GArc(600, 600, 200, 140)
    window.add(shaba, x=290, y=248)
    hair2 = GArc(1700, 1000, 180, 90)
    window.add(hair2, x=130, y=0)
    hair3 = GArc(1700, 1500, 200, 70)
    window.add(hair3, x=80, y=10)
    hair4 = GArc(1900, 1700, 160, 90)
    window.add(hair4, x=70, y=-360)
    doc = GArc(600, 800, 300, 65)
    doc.filled = True
    doc.fill_color = 'black'
    window.add(doc, x=-170, y=-250)
    doc2 = GArc(40, 40, 45, 180)
    doc2.filled = True
    doc2.fill_color = 'yellow'
    window.add(doc2, x=43, y=60)
    doc3 = GArc(40, 40, 50, 180)
    doc3.filled = True
    doc3.fill_color = 'yellow'
    window.add(doc3, x=65, y=35)
    doc4 = GArc(40, 40, 55, 180)
    doc4.filled = True
    doc4.fill_color = 'yellow'
    window.add(doc4, x=87, y=3)
    hair5 = GArc(130, 150, 130, 155)
    window.add(hair5, x=200, y=-20)
    hair6 = GArc(180, 200, 150, 93)
    window.add(hair6, x=240, y=-20)
    hair7 = GArc(130, 150, 150, 155)
    window.add(hair7, x=240, y=-20)
    hair8 = GArc(180, 200, 150, 113)
    window.add(hair8, x=280, y=-60)


if __name__ == '__main__':
    main()
