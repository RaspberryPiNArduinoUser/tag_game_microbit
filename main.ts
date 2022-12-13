function game2 (speed: number) {
    chaser.turn(Direction.Right, randint(0, 90))
    chaser.move(1)
    chaser.ifOnEdgeBounce()
    if (chaser.isTouchingEdge()) {
        game.setScore(game.score() + 1)
    }
    if (chaser.isTouching(player)) {
        music.startMelody(music.builtInMelody(Melodies.Wawawawaa), MelodyOptions.Once)
        game.gameOver()
    }
    basic.pause(speed)
}
input.onButtonPressed(Button.A, function () {
    player.move(1)
})
input.onButtonPressed(Button.B, function () {
    player.move(-1)
})
let player: game.LedSprite = null
let chaser: game.LedSprite = null
game.startCountdown(10000)
chaser = game.createSprite(0, 5)
player = game.createSprite(2, 0)
player.turn(Direction.Right, 90)
player.set(LedSpriteProperty.Brightness, 50)
basic.forever(function () {
    if (edubitPotentioBit.comparePot(PotCompareType.MoreThan, 800)) {
        game2(250)
    } else if (edubitPotentioBit.comparePot(PotCompareType.MoreThan, 400)) {
        game2(500)
    } else {
        game2(750)
    }
})
