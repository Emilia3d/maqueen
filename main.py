odleglosc = 0

def on_forever():
    global odleglosc
    maqueen.motor_run(maqueen.aMotors.M1, maqueen.Dir.CW, 30)
    maqueen.motor_run(maqueen.aMotors.M2, maqueen.Dir.CW, 30)
    odleglosc = maqueen.sensor(PingUnit.CENTIMETERS)
    if odleglosc >= 10:
        maqueen.motor_stop(maqueen.aMotors.M1)
        maqueen.motor_stop(maqueen.aMotors.M2)
        maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_ON)
        maqueen.write_led(maqueen.LED.LED_RIGHT, maqueen.LEDswitch.TURN_OFF)
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
        basic.pause(500)
basic.forever(on_forever)
