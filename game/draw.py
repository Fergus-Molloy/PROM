from constants import constant as c

# -----Clear-----
def clear():
    write = c.esc+"[0;0H"
    for y in range(c.WINDOW_HEIGHT):
        row = c.esc + "[%d;0H" % (y,)
        write += row
        for x in range(c.WINDOW_WIDTH):
            write += c.colorBlack
    write += c.esc+"[0;0H"
    return write

def clear_line():
    write = c.esc+"[1A"
    for x in range(c.WINDOW_WIDTH):
        write += c.esc+"[40m "
    write += c.esc+"[%sD" % (c.WINDOW_WIDTH,)
    return write


# -----Draw Bats-----
def drawLeftBat(left_bat):
    write = c.esc+"[0;0H"
    for y in range(left_bat.y, left_bat.y+c.BAT_SIZE):
        bat = "[%d;%dH" % (y, left_bat.x)
        write += c.esc+bat
        write += c.colorBlue
    return write

def drawRightBat(right_bat):
    write = c.esc+"[0;0H"
    for y in range(right_bat.y, right_bat.y+c.BAT_SIZE):
        bat = "[%d;%dH" % (y, right_bat.x)
        write += c.esc+bat
        write +=c.colorBlue
    return write

def drawBats(left_bat, right_bat):
    write = drawLeftBat(left_bat)
    write += drawRightBat(right_bat)
    return write


# -----Draw Center-----
def drawCenter():
    b = 1  # for 2 bit counter starting at 1 makes it pretty
    middle = "[0;%dH" % (c.WINDOW_WIDTH/2,)
    write = c.esc+middle
    for x in range(c.WINDOW_HEIGHT):
        if b == 3:  # 2 bits are full
            b = 0  # "overflow"
            write += c.colorYellow
        elif b < 2:
            b += 1
            write += c.colorBlack
        else:
            b += 1
            write += c.colorYellow
        write += c.esc+"[1B"
        write += c.esc+"[1D"
    return write


# -----Draw Scores-----
def scoreSequence(score):
    scores = [
        c.zero,
        c.one,
        c.two,
        c.three,
        c.four,
        c.five,
        c.six,
        c.seven,
        c.eight,
        c.nine
    ]
    return scores[score]

def drawLeftScore(left_score):
    xOffset = c.WINDOW_WIDTH / 4
    y_offset = c.WINDOW_HEIGHT / 10
    string = scoreSequence(left_score)
    write = chr(27)+"[%d;%dH" % (y_offset, xOffset)
    for x in string:
        write += x
    return write

def drawRightScore(right_score):
    xOffset = c.WINDOW_WIDTH - (c.WINDOW_WIDTH/4)
    y_offset = c.WINDOW_HEIGHT / 10
    string = scoreSequence(right_score)
    write = chr(27)+"[%d;%dH" % (y_offset, xOffset)
    for x in string:
        write += x
    return write

def drawScores(ball, left_score, right_score):
    drawLeftScore(left_score)
    drawRightScore(right_score)
    write = c.esc+"[40m "
    write += c.esc+"[0;0H"
    write += c.esc + "[%s;%sH" % (ball.y, ball.x)
    return write


# ------Draw Ball-----
def drawBall(ball):
    write = c.esc+"[1D"+c.colorBlack
    write += c.esc + "[%s;%sH" % (ball.y, ball.x)
    write += c.colorWhite
    return write

def clearBall(ball):
    write = c.esc+"[%s;%sH" % (ball.y, ball.x)
    write += c.colorBlack
    return write


# -----Draw Initial-----
def drawInit(ball, left_bat, right_bat, left_score, right_score):
    write = clear()
    write += drawBats(left_bat, right_bat)
    write += drawCenter()
    write += drawScores(ball, left_score, right_score)
    write +=drawBall(ball)
    return write


# -----Debug-----
def drawArea():
    left_x_offset = c.WINDOW_WIDTH / 4
    right_x_offset = c.WINDOW_WIDTH - left_x_offset
    y_offset = (c.WINDOW_HEIGHT / 10)
    for x in range(c.WINDOW_WIDTH):
        for y in range(c.WINDOW_HEIGHT):
            write += c.esc+"[%s;%sH" % (y, x)
            if x > left_x_offset-1 and x < left_x_offset+3:
                if y > y_offset-1 and y < y_offset+5:
                    write += c.colorCyan
            elif x > right_x_offset-1 and x < right_x_offset+3:
                if y > y_offset-1 and y < y_offset+5:
                    write += c.colorCyan
    return write
