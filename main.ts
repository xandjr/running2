input.onButtonPressed(Button.A, function () {
    if (true) {
        Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_Run, 80)
        Tinybit.RGB_Car_Big(Tinybit.enColor.Blue)
        basic.pause(2000)
        Tinybit.CarCtrl(Tinybit.CarState.Car_Stop)
        basic.pause(1000)
        Tinybit.CarCtrl(Tinybit.CarState.Car_Left)
        basic.pause(200)
        Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_Run, 80)
        Tinybit.RGB_Car_Big(Tinybit.enColor.Green)
        basic.pause(1000)
        Tinybit.CarCtrl(Tinybit.CarState.Car_Stop)
        basic.pause(1000)
        Tinybit.CarCtrl(Tinybit.CarState.Car_Right)
        basic.pause(200)
        Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_Run, 70)
        basic.pause(1000)
        Tinybit.CarCtrl(Tinybit.CarState.Car_Stop)
        basic.pause(1000)
        Tinybit.CarCtrl(Tinybit.CarState.Car_Right)
        basic.pause(200)
        Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_Run, 70)
        basic.pause(2000)
        Tinybit.CarCtrl(Tinybit.CarState.Car_Stop)
    }
    music._playDefaultBackground(music.builtInPlayableMelody(Melodies.PowerDown), music.PlaybackMode.InBackground)
})
music._playDefaultBackground(music.builtInPlayableMelody(Melodies.PowerUp), music.PlaybackMode.UntilDone)
basic.pause(100)
for (let index = 0; index < 1; index++) {
    music.play(music.tonePlayable(554, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(587, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(622, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(659, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(659, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(659, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(554, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(587, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(554, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(587, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(587, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(587, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(554, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(698, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(659, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(622, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(622, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(622, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(554, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(587, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(622, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(659, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(659, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(659, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
}
while (true) {
    basic.showString("MANIVELA")
    basic.showLeds(`
        # # . # #
        # # . # #
        . . # . .
        # . . . #
        . # # # .
        `)
    basic.showIcon(IconNames.Heart)
    basic.clearScreen()
}
