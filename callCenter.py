from call import Call

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue = 0

    def add(self, *newCalls):
        self.calls.extend(newCalls)
        self.queue = len(self.calls)
        return self
    def remove(self):
        self.calls.pop(0)
        self.queue = len(self.calls)
        return self
    def removeNum(self,num):
        for index,call in enumerate(self.calls):
            if call.phoneNumber == num:
                self.calls.pop(index)
        return self
    def info(self):
        for call in self.calls:
            print call.name, '~~>', str(call.phoneNumber)
        print 'This queue is', str(len(self.calls)) + ' callers long'
        return self


caller1 = Call('Wura', 425, '10 mins', 'business')
caller2 = Call('Zay', 425, '25 mins', 'programming chat')
caller3 = Call('Kunmi', 287, '42 mins', '1964 brand')

Call.allCalls(caller1,caller2,caller3)

center1 = CallCenter()
center1.add(caller1,caller2,caller3).removeNum(425).info()
