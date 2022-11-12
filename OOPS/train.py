'''
class Train

methods:
book a ticket
show status(no of seats)
show fare

[1, 2, 3, 4, 5]
'''

class Train:

    def __init__(self, name, noOfSeats, fare):
        self.name = name
        self.tseats = noOfSeats
        self.nSeats = list(range(1, noOfSeats+1 ))
        self.fare = fare
    
    def showDetails(self):
        print(f"Train name: {self.name}")
        print(f"Seats in Train: {self.nSeats}")
        print(f"Fare: {self.fare}")
    
    def bookTickets(self , noOfTickets):
        if noOfTickets <= len(self.nSeats):
            for i in range(noOfTickets):
                print(f"seat no booked:  {self.nSeats.pop()}")
            print(f"Please pay: {noOfTickets * self.fare}")
        else:
            print(f"{noOfTickets - len(self.nSeats)} are extra")
    
    def cancelTicket(self, ticketNum):
        if ticketNum < 0 or ticketNum > self.tseats:
            print("Enter a valid ticket number")
        else:
            if ticketNum not in self.nSeats:
                self.nSeats.append(ticketNum)
                print(f"Seat No: {ticketNum} cancelled")
            else:
                print("Check the ticket number")


t1 = Train("Rajdhani" , 5 , 50)

t1.bookTickets(4)
t1.showDetails()
t1.cancelTicket(3)
t1.showDetails()

    

