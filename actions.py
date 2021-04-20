#Sve akcije koje radite sa elementima, mjerenja, vklop-isklop elemenata sistema...
#Exception handling!!!

class HydroponicsPump():
    def pumpON():
        pass
        # Exception handling!!!

    def pumpOFF():
        pass
        # Exception handling!!!



class Sensors():
    def checkup(self, gpio, value):
        self.gpio=gpio
        try:
            GPIO.input(gpio, value)
            return value
        except:
            print("Nemoguće očitati vrijednost")

class Operations():
    def react(self, gpio, time)
        self.gpio=gpio
        self.time=time
        try:
            GPIO.output(gpio, GPIO.HIGH)
            time.sleep(time)
            GPIO.output(gpio, GPIO.LOW)
        except:
            print("Nemoguće obaviti operaciju")


class HydroponicsSensors():
    def measureEC():
        ec = 12.3
        # Exception handling!!!
        return ec

    def measureTemp():
        temp = 12.5
        # Exception handling!!!
        return temp

    def measurepH():
        ph = 7.5
        # Exception handling!!!
        return ph
    
class HydroponicsTankOperations():
                    
    def mainTankFloat():
        # Exception handling!!!
        pass

    def DWCTankOperations():
        # Exception handling!!!
        pass

    def mainTankTemp():
        try:
            GPIO.output(8, GPIO.HIGH)
            GPIO.output(36, GPIO.HIGH)
        except:
            Print ("Nije moguće uključiti grijanje")
class DataManipulation():
    
    def sendDataToDB():
        import urllib.request, actions
        data1 = actions.HydroponicsSensors.measureEC()
        data2 = actions.HydroponicsSensors.measureTemp()
        data3 = actions.HydroponicsSensors.measurepH()
        try:
            urllib.request.urlopen('http://accpoint.motherlandia.org/add_data.php?data1={}&data2={}&data3={}'.format(data1, data2, data3))
        except:
            print('Podaci nisu poslani...')

    def raiseAlarm():
        import urllib.request, actions
        data1 = actions.HydroponicsSensors.measureEC()
        data2 = actions.HydroponicsSensors.measureTemp()
        data3 = actions.HydroponicsSensors.measurepH()                
        try:
            urllib.request.urlopen('http://accpoint.motherlandia.org/add_data.php?data1={}&data2={}&data3={}'.format(data1, data2, data3))
            #poslati mail
        except:
            print ("Poruka nije poslana!")

    def takePhoto():
        import cv2, time
        photo_name = 'hydro_{}.png'.fromat(time.ctime())