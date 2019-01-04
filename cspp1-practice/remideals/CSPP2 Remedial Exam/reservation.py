class reservation:
    def __init__(self, cname, roomnumber=500):
        self.cname=cname
        self.roomnumber=roomnumber
    # def __init__(self, cname):
    #   self.cname = cname
    def setroomnumber(self,newroomnumber):
        self.roomnumber=newroomnumber
    def setcname(self,newcname):
        self.cname=newcname
    def getroomnumber(self):
        return self.roomnumber
    def getcname(self):
        return self.cname

class hotel:
    def __init__(self):
        self.rooms=[None, None, None, None, None]
        self.size=5
        self.count=0
    
    def reservationRoom(self,cname):
        if self.size == self.count:
            print("All Rooms are reserved")
            return
        # print("count is ",self.count)
        # print("reservationRoom.....",self.size)
        for i in range(self.size):
            if self.rooms[i]  == None:
                obj = reservation(cname)
                obj.setroomnumber(i+1)
                self.rooms[i] = obj
                self.count += 1
                return i + 1
        return -1

    def reservingRoom(self, cname, roomnumber):
        if self.size == self.count:
            print("All Rooms are reserved")
        elif (self.rooms[roomnumber-1] == None):
            obj1 = reservation(cname,roomnumber)
            self.rooms[roomnumber-1] = obj1
            self.count += 1
            return True
        # elif (self.rooms[roomnumber] != None):
            # print(".......kranthikumar.........")
        else:
            # print(".......kranthikumar.........")
            print("Room is already reserved")
        return False

    def printReservations(self):
        for i in range(self.size):
            # print("kranthi kumar...............")
            if self.rooms[i] != None:
                print(self.rooms[i].getcname()+" "+str(self.rooms[i].getroomnumber()))
    
    def cancelReservations(self, cname):
        for i in range(self.size):
            if self.rooms[i]!=None and self.rooms[i].getcname()==cname:
                self.rooms[i]=None
                self.count=self.count-1
            
    def buildRooms(self, roomnumber):
        if roomnumber>0:
            for i in range(roomnumber):
                self.rooms.append(None)
            self.size =self.size + roomnumber
            return True
        else:
            return False

class Solution1:
    hotel=hotel()
    input_data=int(input())
    c=0
    while c<input_data:
        tokens = str(input())
        tokens=tokens.split(" ")
        if tokens[0] == "reserve":
            cname = tokens[1]
            roomnumber = -1
            if cname!= None:
                roomnumber = hotel.reserveRoom(cname)
                # break
                # print("kranthi kumar")
                # print(cname,roomnumber)
            elif roomnumber != -1:
                print(cname+ " " +str(roomnumber))

        if tokens[0] == "reserveN":
            cname = tokens[1]
            if cname == None:
                roomnumber = -1
            else :
                roomnumber = int(tokens[2])
            if(hotel.reservingRoom(cname,roomnumber)):
                print(cname+" "+str(roomnumber))

        if tokens[0] == "print":
            hotel.printReservations()
        

        if tokens[0] == "cancel":
            cname = tokens[1]
            if cname!=None:
                hotel.cancelReservations(cname)
                print(cname+" "+"now has no reservations.")
            else:
                print("No input")

        if tokens[0] == "build":
            roomnumber = int(tokens[1]);
            if(hotel.buildRooms(roomnumber)):
                print("Added"+" "+str(roomnumber)+" "+"more rooms")
            else:
                print("No rooms are added")
        c=c+1

def main():
    Solution = Solution1()
if __name__ == '__main__':
        main()

