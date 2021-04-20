import time
import schedule
import RPi.GPIO as GPIO
from actions2? import DataManipulation
from actions2? import Sensors
from actions2? import Operations

GPIO.setmode(GPIO.BOARD)


GPIO.setup(29, GPIO.IN)     #ecSenzor
GPIO.setup(31, GPIO.IN)     #temperatura
GPIO.setup(33, GPIO.IN)     #pH
GPIO.setup(35, GPIO.IN)     #float switch glavni tank
GPIO.setup(37, GPIO.IN)     #float switch DWC


GPIO.setup(8, GPIO.OUT)         #grijač GT
GPIO.setup(10, GPIO.OUT)        #zračna pumpa GT
GPIO.setup(12, GPIO.OUT)        #vodena pumpa GT
GPIO.setup(16, GPIO.OUT)        #pumpa voda
GPIO.setup(18, GPIO.OUT)        #pumpa ec
GPIO.setup(22, GPIO.OUT)        #solenoid EBB
GPIO.setup(24, GPIO.OUT)        #pumpa EBB
GPIO.setup(36, GPIO.OUT)        #grijač DWC
GPIO.setup(38, GPIO.OUT)        #zračna pumpa DWC
GPIO.setup(40, GPIO.OUT)        #vodena pumpa DWC


#inputi
ecCheck=Sensors.checkup(29)
TempCheck=Sensors.checkup(31)
pHCkeck=Sensors.checkup(33)
schedule.every(3).hours.do(ecCheck)
schedule.every(3).hours.do(TempCheck)
schedule.every(3).hours.do(pHCheck)

mainTankLevel=Sensors.checkup(35)
DWCTankLevel=Sensors.checkup(37)


#baratanje podacima
Report=DataManipulation.sendDataToDB()
Photo=DataManipulation.takePhoto()
Alarm=DataManipulation.raiseAlarm()

schedule.every(3).hours.do(RegularReport)
schedule.every(12).hours.do(Photo)


#tmperatura
TempResponse=Operations.react(8, 600)
TempREsponseDWC=Operations.react(36, 1200)

if TempCheck<18:
    TempResponse

if TempCheck==25:
    Alarm

if TempCheck==28:
    Alarm


#ec
ecResponsePlus=Operations.react(18, #sekundi)
ecResponseMinus=Operations.react(16, #sekundi)
mainTankAir=Operations.react(10, 90)

if ecCheck<1050:
    ecResponsePlus
    mainTankAir
if ecCheck>1300:
    ecResponseMinus
    mainTankAir

#nivo tečnosti u glavnom tanku
if mainTankLevel<1:
    ecResponsePlus
    ecResponseMinus
    mainTankAir


#EBB
ciklusNaEBB=Operations.react(12, #sekundi)
ciklusSOlenoidEBB=Operations.react(22, #sekundi)
ciklusOdEBB=Operations.react(24, #sekundi)


schedule.every(4).hours.do.(ciklusNaEBB)
schedule.every(4).hours.do.(time.sleep(600), ciklusNaEBB)
schedule.every(4).hours.do.(time.sleep(603)ciklusNaEBB)



#DWC
DWCTankAir=Operations.react(38, 180)
schedule.every(4).hours.do(DWCTankAir)

DWCPump=Operations.react(40, #vrijeme)
if mainTankLevel<1:
    DWCPump


#nepohodno za rasporede, (ostaviti za kraj)?:
while True:
    schedule.run_pending()
    time.sleep(1)