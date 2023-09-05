def on_button_pressed_a():
    if True:
        Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_RUN, 80)
        Tinybit.RGB_Car_Big(Tinybit.enColor.BLUE)
        basic.pause(2000)
        Tinybit.car_ctrl(Tinybit.CarState.CAR_STOP)
        basic.pause(1000)
        Tinybit.car_ctrl(Tinybit.CarState.CAR_LEFT)
        basic.pause(200)
        Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_RUN, 80)
        Tinybit.RGB_Car_Big(Tinybit.enColor.GREEN)
        basic.pause(1000)
        Tinybit.car_ctrl(Tinybit.CarState.CAR_STOP)
        basic.pause(1000)
        Tinybit.car_ctrl(Tinybit.CarState.CAR_RIGHT)
        basic.pause(200)
        Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_RUN, 70)
        basic.pause(1000)
        Tinybit.car_ctrl(Tinybit.CarState.CAR_STOP)
        basic.pause(1000)
        Tinybit.car_ctrl(Tinybit.CarState.CAR_RIGHT)
        basic.pause(200)
        Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_RUN, 70)
        basic.pause(2000)
        Tinybit.car_ctrl(Tinybit.CarState.CAR_STOP)
    music._play_default_background(music.built_in_playable_melody(Melodies.POWER_DOWN),
        music.PlaybackMode.IN_BACKGROUND)
input.on_button_pressed(Button.A, on_button_pressed_a)

music._play_default_background(music.built_in_playable_melody(Melodies.POWER_UP),
    music.PlaybackMode.UNTIL_DONE)
basic.pause(100)
for index in range(1):
    music.play(music.tone_playable(554, music.beat(BeatFraction.HALF)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(587, music.beat(BeatFraction.HALF)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(622, music.beat(BeatFraction.HALF)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(659, music.beat(BeatFraction.HALF)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(659, music.beat(BeatFraction.HALF)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(659, music.beat(BeatFraction.HALF)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(554, music.beat(BeatFraction.HALF)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(587, music.beat(BeatFraction.HALF)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(554, music.beat(BeatFraction.HALF)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(587, music.beat(BeatFraction.HALF)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(587, music.beat(BeatFraction.HALF)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(587, music.beat(BeatFraction.HALF)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(554, music.beat(BeatFraction.HALF)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(698, music.beat(BeatFraction.HALF)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(659, music.beat(BeatFraction.HALF)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(622, music.beat(BeatFraction.HALF)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(622, music.beat(BeatFraction.HALF)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(622, music.beat(BeatFraction.HALF)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(554, music.beat(BeatFraction.HALF)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(587, music.beat(BeatFraction.HALF)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(622, music.beat(BeatFraction.HALF)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(659, music.beat(BeatFraction.HALF)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(659, music.beat(BeatFraction.HALF)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(659, music.beat(BeatFraction.HALF)),
        music.PlaybackMode.UNTIL_DONE)
while True:
    basic.show_string("MANIVELA")
    basic.show_leds("""
        # # . # #
        # # . # #
        . . # . .
        # . . . #
        . # # # .
        """)
    basic.show_icon(IconNames.HEART)
    basic.clear_screen()