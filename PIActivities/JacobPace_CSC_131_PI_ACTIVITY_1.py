# Name: Jacob Pace
# Date: 12/19/2022
# # Description:

class Room:

    def __init__(self, name):
        # Rooms have a name, exits, items, obsticals, ect...
        # Item descriptions and grabbables
        self.name = name 
        self.exits = []
        self.exitLocations = []
        self.items = []
        self.itemDescriptions = []
        self.grabbables = []
        self.grabbableDescriptions = []
        
    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def exits(self):
        return self._exits
        
    @exits.setter
    def exits(self, value):
        self._exits = value
        
    @property
    def exitLocations(self):
        return self._exitLocations
        
    @exitLocations.setter
    def exitLocations(self, value):
        self._exitLocations = value

    @property
    def items(self):
        return self._items
        
    @items.setter
    def items(self, value):
        self._items = value

    @property
    def itemDescriptions(self):
        return self._itemDescriptions
        
    @itemDescriptions.setter
    def itemDescriptions(self, value):
        self._itemDescriptions = value

    @property
    def grabbables(self):
        return self._grabbables
        
    @grabbables.setter
    def grabbables(self, value):
        self._grabbables = value

    @property
    def grabbableDescriptions(self):
        return self._grabbableDescriptions
    
    @grabbableDescriptions.setter
    def grabbableDescriptions(self, value):
        self._grabbableDescriptions = value

    # Appends the exit and room to the appropriate list
    # Exit is a string
    # Room is an instance
    def addExit(self, exit, room):
        # Appends the exit and room to the appropriate list
        self._exits.append(exit)
        self.exitLocations.append(room)
    
    #  adds an item tot he current room instance
    # item is a sting
    # desc is a string that describes the item
    def addItem(self, item, desc):
        # Append to items and the item description appropriatley
        self._items.append(item)
        self._itemDescriptions.append(desc)
     # adds an item to the grabble list
    def addGrabbable(self, item):
        self._grabbables.append(item)
        #self._grabbableDescriptions.append(desc)
     # delets an item from the grabbable list
    def delGrabbable(self, item):
        # removes the item from the grabbable list
        self._grabbables.remove(item)
        #self.grabbableDescriptions.remove(desc)

    def __str__(self):
        # room name 
        s = f"You are in {self.name}.\n"
         # next the items in the room
        s += "You see:\n"
        for item in self.items:
            s += f"{item}, "
        s += "\n"
        
        # show all possible exits
        s += "Exits:\n"
        for exit in self.exits:
            s += f"{exit}, "
        s += "\n"
        return s

###########################################################
#               START OF GAME
###########################################################
def createRooms():
    global currentRoom
    r1 = Room("Room 1")
    r2 = Room("Room 2")
    r3 = Room("Room 3")
    r4 = Room("Room 4")
    r5 = Room("Attic")
    global r6
    r6 = Room("Basement")

    # Adding to room 1

    # adding exits to room 1
    r1.addExit("east", r2)
    r1.addExit("south", r3)
    # adding grabbables to room 1
    r1.addGrabbable("key")
    # adding items to room 1
    r1.addItem("chair", "It is made of wicker and no one is sitting on it.")
    r1.addItem("table", "It is made of oak, and there is a golden key sitting on it.")

    # adding to room 2
    # adding exits to room 2
    r2.addExit("west", r1)
    r2.addExit("south", r4)
    r2.addExit("down", r6)
    # adding items to room 2
    r2.addItem("rug", "It is nice and Indian.  It also needs to be vacuumed.")
    r2.addItem("fireplace", "It is full of ashes.")

    # adding to room 3
    # adding exits to room 3
    r3.addExit("north", r1)
    r3.addExit("east", r4)
    r3.addExit("up", r5)
    # adding grabbables to room 1
    r3.addGrabbable("book")
    # adding items to room 1
    r3.addItem("bookshelves", "It is empty, go figure.")
    r3.addItem("statue", "Nothing special about it.")
    r3.addItem("desk", "The statue is resting on it, so is a book.")
    r3.addItem("ladder", "There is a drop down ladder from the ceiling, I wonder where it goes?")

    # add to room 4
    # adding exits to room 4
    r4.addExit("north", r2)
    r4.addExit("west", r3)
    r4.addExit("south", None) #DEATH
    # adding grabbables to room 4
    r4.addGrabbable("6-pack")
    # adding items to room 1
    r4.addItem("brew_rig", "Gourd is brewing some sort of oatmeal stout on the brew_rig.  A 6-pack is resting next to it.")

    r5.addExit("down", r3)
    r5.addExit("east", None)
    r5.addItem("not_much", "The floor is covered in a fine layer of dust.")

    r6.addExit("up", r2)
    r6.addItem("chest", "There is a chest that is locked, Iw onder if there is a key somewhere?")
    currentRoom = r1
    pass

def death():
    print(" " * 17 + "u" * 7)
    print(" " * 13 + "u" * 2 + "$" * 11 + "u" * 2)
    print(" " * 10 + "u" * 2 + "$" * 17 + "u" * 2)
    print(" " * 9 + "u" + "$" * 21 + "u")
    print(" " * 8 + "u" + "$" * 23 + "u")
    print(" " * 7 + "u" + "$" * 25 + "u")
    print(" " * 7 + "u" + "$" * 25 + "u")
    print(" " * 7 + "u" + "$" * 6 + "\"" + " " * 3 + "\"" + "$" * 3 + "\"" + " " * 3 + "\"" + "$" * 6 + "u")
    print(" " * 7 + "\"" + "$" * 4 + "\"" + " " * 6 + "u$u" + " " * 7 + "$" * 4 + "\"")
    print(" " * 8 + "$" * 3 + "u" + " " * 7 + "u$u" + " " * 7 + "u" + "$" * 3)
    print(" " * 8 + "$" * 3 + "u" + " " * 6 + "u" + "$" * 3 + "u" + " " * 6 + "u" + "$" * 3)
    print(" " * 9 + "\"" + "$" * 4 + "u" * 2 + "$" * 3 + " " * 3 + "$" * 3 + "u" * 2 + "$" * 4 + "\"")
    print(" " * 10 + "\"" + "$" * 7 + "\"" + " " * 3 + "\"" + "$" * 7 + "\"")
    print(" " * 12 + "u" + "$" * 7 + "u" + "$" * 7 + "u")
    print(" " * 13 + "u$\"$\"$\"$\"$\"$\"$u")
    print(" " * 2 + "u" * 3 + " " * 8 + "$" * 2 + "u$ $ $ $ $u" + "$" * 2 + " " * 7 + "u" * 3)
    print(" u" + "$" * 4 + " " * 8 + "$" * 5 + "u$u$u" + "$" * 3 + " " * 7 + "u" + "$" * 4)
    print(" " * 2 + "$" * 5 + "u" * 2 + " " * 6 + "\"" + "$" * 9 + "\"" + " " * 5 + "u" * 2 + "$" * 6)
    print("u" + "$" * 11 + "u" * 2 + " " * 4 + "\"" * 5 + " " * 4 + "u" * 4 + "$" * 10)
    print("$" * 4 + "\"" * 3 + "$" * 10 + "u" * 3 + " " * 3 + "u" * 2 + "$" * 9 + "\"" * 3 + "$" * 3 + "\"")
    print(" " + "\"" * 3 + " " * 6 + "\"" * 2 + "$" * 11 + "u" * 2 + " " + "\"" * 2 + "$" + "\"" * 3)
    print(" " * 11 + "u" * 4 + " \"\"" + "$" * 10 + "u" * 3)
    print(" " * 2 + "u" + "$" * 3 + "u" * 3 + "$" * 9 + "u" * 2 + " \"\"" + "$" * 11 + "u" * 3 + "$" * 3)
    print(" " * 2 + "$" * 10 + "\"" * 4 + " " * 11 + "\"\"" + "$" * 11 + "\"")
    print(" " * 3 + "\"" + "$" * 5 + "\"" + " " * 22 + "\"\"" + "$" * 4 + "\"\"")
    print(" " * 5 + "$" * 3 + "\"" + " " * 25 + "$" * 4 + "\"")
    return

inventory = []
inventoryDesc = []
createRooms()

while True:
    if currentRoom == None:
        death()
        break

    status = f"{currentRoom}You are carrying: {inventory}"
    print("-"*50)
    print(status)
    
    # prompt user for input
    # inputs like <verb> <noun>
    # vaild verbs : go, look, take
    # valid nouns depend on the verb
    # prompt user for information
    action = input("What to do?: ")
    action = action.lower()
    if action in ["quit", "exit", "bye"]:
        break

    # response
    response = "I don't understand.  Try a <verb> <noun>.  Valid verbs are: go, look, check, use, and take."

    # spilt words
    words = action.split()

    # if given 2 words
    if len(words) == 2:
        verb = words[0]
        noun = words[1]

        if (verb == "go"):
            response = "Invalid exit!"
            for i in range(len(currentRoom.exits)):
                if (noun == currentRoom.exits[i]):
                    currentRoom = currentRoom.exitLocations[i]
                    response = "Room changed!"
                    break

        elif (verb == "look"):
            for i in range(len(currentRoom.items)):
                if (noun == currentRoom.items[i]):
                    response = currentRoom.itemDescriptions[i]
                    break

        elif (verb == "take"):
            response = "I don't see that item here."
            for grabbable in currentRoom.grabbables:
                if (noun == grabbable):
                    grabbableDesc = grabbable.index
                    inventory.append(grabbable)
                    currentRoom.delGrabbable(grabbable)
                    response = "Yoink!"

        elif (verb == "check"):
            response = "You don't have that item right now."
            for i in range(len(inventory)):
                if (noun == inventory[i]):
                    response = f"This is a {inventory[i]}!  What can it be used for?"
                    break

        elif (verb == "use"):
            response = "You can't do that here."
            if (("key" in inventory) and (noun == "key") and (currentRoom == r6)):
                response = "You unlock and open the chest to find a note, it says:\n\"Looks like you found my chest, too bad for you, the game was rigged from the start.\nYou just released a toxic gas and now your dead lol!\""
                currentRoom = None
    print(f"\n{response}")
