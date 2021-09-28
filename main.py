y = 0
basic.show_icon(IconNames.HAPPY)
basic.clear_screen()
x = 2

def on_forever():
    global y
    y = 0
    while y <= 4:
        led.plot(x, y)
        basic.pause(100)
        led.unplot(x, y)
        y += 1
basic.forever(on_forever)
