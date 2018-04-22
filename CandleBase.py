class CandleBase:

    symbol    = ""

    starttime = 0
    stoptime  = 0

    openp  = 0
    closep = 0
    highp  = 0
    lowp   = 0


    def __init__(self, starttime, stoptime,openp,closep,highp,lowp):
        self.starttime = starttime
        self.stoptime = stoptime
        self.openp = openp
        self.closep = closep
        self.highp = highp
        self.lowp = lowp


def __str__(self):

        out_str = "%d to %d //  %.8f  %.8f  %.8f  %.8f " %(self.starttime,self.stoptime,self.openp,self.closep,self.highp,self.lowp)
 
        return out_str

