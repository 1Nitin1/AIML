class Rail:
    
    def __init__(self,name,seatsLeft):
        self.name=name
        self.seatsLeft=seatsLeft

    def getStatus(self):
        return f"Train Name: {self.name}, Seats Left: {self.seatsLeft}"
    def bookTicket(self):
        if self.seatsLeft>0:
            self.seatsLeft-=1
            return "Ticket booked successfully"
        else:
            return "No seats available"
        
train1=Rail("Express",5)
print(train1.getStatus())
print(train1.bookTicket())