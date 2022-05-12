def convertTime3200(time, conversionFactor = 2.15):
    secTime = 60 * int(time.split(":")[0]) + float(time.split(":")[1])
    convertedSec = secTime/conversionFactor
    min, sec = divmod(convertedSec, 60)
    return "%d:%02d" % (min, sec)

def convertTime800(time, conversionFactor = 2.2):
    secTime = 60 * int(time.split(":")[0]) + float(time.split(":")[1])
    convertedSec = secTime * conversionFactor
    min, sec = divmod(convertedSec, 60)
    return "%d:%02d" % (min, sec)

def reformat(time):
    return time.split(".")[0]
