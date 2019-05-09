from constants import constant as c


def write(serial_port, string):
    serial_port.write(str(string))


# -----Clear-----
def clear(serial_port):
    write(serial_port, c.esc+"[0;0H")
    for y in range(c.WINDOW_HEIGHT):
        row = c.esc + "[%d;0H" % (y,)
        write(serial_port, row)
        for x in range(c.WINDOW_WIDTH):
            write(serial_port, c.colorBlack)
    write(serial_port, c.esc+"[0;0H")


def clear_line(serial_port):
    write(serial_port, c.esc+"[1A")
    for x in range(c.WINDOW_WIDTH):
        write(serial_port, c.esc+"[40m ")
    write(serial_port, c.esc+"[%sD" % (c.WINDOW_WIDTH,))


def clear_ball(serial_port, ball):
    write(serial_port, c.esc+"[%s;%sH" % (ball.y, ball.x))
    write(serial_port, c.colorBlack)


# -----Draw Bats-----
def draw_left_bat(serial_port, left_bat):
    write(serial_port, c.esc+"[0;0H")
    for y in range(left_bat.y, left_bat.y+c.BAT_SIZE):
        bat = "[%d;%dH" % (y, left_bat.x)
        write(serial_port, c.esc+bat)
        write(serial_port, c.colorBlue)


def draw_right_bat(serial_port, right_bat):
    write(serial_port, c.esc+"[0;0H")
    for y in range(right_bat.y, right_bat.y+c.BAT_SIZE):
        bat = "[%d;%dH" % (y, right_bat.x)
        write(serial_port, c.esc+bat)
        write(serial_port, c.colorBlue)


def draw_bats(serial_port, left_bat, right_bat):
    draw_left_bat(serial_port, left_bat)
    draw_right_bat(serial_port, right_bat)



# -----Draw Center-----
def draw_center(serial_port):
    b=1  # for 2 bit counter starting at 1 makes it pretty
    middle="[0;%dH" % (c.WINDOW_WIDTH/2,)
    write(serial_port, c.esc+middle)
    for x in range(c.WINDOW_HEIGHT):
        if b == 3:  # 2 bits are full
            b=0  # "overflow"
            write(serial_port, c.colorYellow)
        elif b < 2:
            b += 1
            write(serial_port, c.colorBlack)
        else:
            b += 1
            write(serial_port, c.colorYellow)
        write(serial_port, c.esc+"[1B")
        write(serial_port, c.esc+"[1D")



# -----Draw Scores-----
def score_sequence(score):
    scores=[
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

def draw_left_score(serial_port, left_score):
    xOffset = c.WINDOW_WIDTH / 4
    y_offset = c.WINDOW_HEIGHT / 10
    string = score_sequence(left_score)
    write(serial_port, chr(27)+"[%d;%dH" % (y_offset, xOffset))
    for x in string:
        write(serial_port, x)


def draw_right_score(serial_port, right_score):
    xOffset = c.WINDOW_WIDTH - (c.WINDOW_WIDTH/4)
    y_offset = c.WINDOW_HEIGHT / 10
    string = score_sequence(right_score)
    write(serial_port, chr(27)+"[%d;%dH" % (y_offset, xOffset))
    for x in string:
        write(serial_port, x)


def draw_scores(serial_port, ball, left_score, right_score):
    draw_left_score(serial_port, left_score)
    draw_right_score(serial_port, right_score)
    write(serial_port, c.esc+"[40m ")
    write(serial_port, c.esc+"[0;0H")
    write(serial_port, c.esc + "[%s;%sH" % (ball.y, ball.x))



# ------Draw Ball-----
def draw_ball(serial_port, ball):
    write(serial_port, c.esc+"[1D"+c.colorBlack)
    write(serial_port, c.esc + "[%s;%sH" % (ball.y, ball.x))
    write(serial_port, c.colorWhite)



# -----Draw Initial-----
def draw_init(serial_port, ball, left_bat, right_bat, left_score, right_score):
    clear(serial_port)
    draw_bats(serial_port, left_bat, right_bat)
    draw_center(serial_port)
    draw_scores(serial_port, ball, left_score, right_score)
    draw_ball(serial_port, ball)



# -----Debug-----
def draw_area(serial_port):
    left_x_offset=c.WINDOW_WIDTH / 4
    right_x_offset=c.WINDOW_WIDTH - left_x_offset
    y_offset=(c.WINDOW_HEIGHT / 10)
    for x in range(c.WINDOW_WIDTH):
        for y in range(c.WINDOW_HEIGHT):
            write(serial_port, c.esc+"[%s;%sH" % (y, x))
            if x > left_x_offset-1 and x < left_x_offset+3:
                if y > y_offset-1 and y < y_offset+5:
                    write(serial_port, c.colorCyan)
            elif x > right_x_offset-1 and x < right_x_offset+3:
                if y > y_offset-1 and y < y_offset+5:
                    write(serial_port, c.colorCyan)
