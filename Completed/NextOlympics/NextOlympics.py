class NextOlympics:
    def countDays(self, today):
        TwntThrd_JUL2021 = date(2021,7,23)
        tdc=today.split('.')
        tad=date(int(tdc[0]),int(tdc[1]),int(tdc[2]))
        diff=TwntThrd_JUL2021 - tad
        return diff.days 
