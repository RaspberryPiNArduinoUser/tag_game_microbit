def game2(speed: number):
    chaser.turn(Direction.RIGHT, randint(0, 90))
    chaser.move(1)
    chaser.if_on_edge_bounce()
    if chaser.is_touching_edge():
        game.set_score(game.score() + 1)
    if chaser.is_touching(player):
        music.start_melody(music.built_in_melody(Melodies.WAWAWAWAA),
            MelodyOptions.ONCE)
        game.game_over()
    basic.pause(speed)

def on_button_pressed_a():
    player.move(1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    player.move(-1)
input.on_button_pressed(Button.B, on_button_pressed_b)

player: game.LedSprite = None
chaser: game.LedSprite = None
game.start_countdown(10000)
chaser = game.create_sprite(0, 5)
player = game.create_sprite(2, 0)
player.turn(Direction.RIGHT, 90)
player.set(LedSpriteProperty.BRIGHTNESS, 50)

def on_forever():
    if edubitPotentioBit.compare_pot(PotCompareType.MORE_THAN, 800):
        game2(250)
    elif edubitPotentioBit.compare_pot(PotCompareType.MORE_THAN, 400):
        game2(500)
    else:
        game2(750)
basic.forever(on_forever)
