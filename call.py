count = 1
class Call(object):
    def __init__(self, name, phoneNumber, callTime, reasonForCall):
        global count
        self.name = name
        self.phoneNumber = phoneNumber
        self.callTime = callTime
        self.reasonForCall = reasonForCall
        self.num = count #we create a unique ID by giving each instance count that increases as we create new instance
        count += 1

    def allCalls(*calls):
        for call in calls:
            print call.name, 'ID is:', str(call.num) + '.','Other details:', str(call.phoneNumber), call.callTime, call.reasonForCall
