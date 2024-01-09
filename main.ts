let odleglosc = 0
maqueen.MotorRun(maqueen.aMotors.M1, maqueen.Dir.CW, 30)
maqueen.MotorRun(maqueen.aMotors.M2, maqueen.Dir.CW, 30)
basic.forever(function () {
    odleglosc = maqueen.sensor(PingUnit.Centimeters)
    if (odleglosc >= 10) {
        maqueen.motorStop(maqueen.aMotors.M1)
        maqueen.motorStop(maqueen.aMotors.M2)
        maqueen.writeLED(maqueen.LED.LEDLeft, maqueen.LEDswitch.turnOn)
        maqueen.writeLED(maqueen.LED.LEDRight, maqueen.LEDswitch.turnOff)
        music.playTone(262, music.beat(BeatFraction.Whole))
        basic.pause(500)
    }
})
