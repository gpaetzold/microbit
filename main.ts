let y = 0
basic.showIcon(IconNames.Happy)
basic.clearScreen()
let x = 2
basic.forever(function () {
    y = 0
    while (y <= 4) {
        led.plot(x, y)
        basic.pause(100)
        led.unplot(x, y)
        y += 1
    }
})
