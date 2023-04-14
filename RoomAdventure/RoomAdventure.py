###########################################################################################
# Name: Jacob Pace
# Date: 4/14/2023
# Description: Room Adventure
###########################################################################################
import pygame
import sys
pygame.init()
WIDTH = 800
HEIGHT = 600
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Room Adventure")

white = (255, 255, 255)
black = (0,0,0)
DISPLAYSURF.fill(white)
pygame.display.flip()

font = pygame.font.SysFont("Arial", 30)
inputTextBox = pygame.Rect(550, 600, 0, 800)

Output = pygame.Rect(400, 0, 400, 550)

Room1Img = pygame.image.load('images/Room1.jpg').convert_alpha()
Room2Img = pygame.image.load('images/Room2.jpg').convert_alpha()
Room3Img = pygame.image.load('images/Room3.jpg').convert_alpha()
Room4Img = pygame.image.load('images/Room4.jpg').convert_alpha()
SkullImg = pygame.image.load('images/Skull.png').convert_alpha()

# the room class
# note that this class is fully implemented with dictionaries as illustrated in the lesson "More on Data Structures"
class Room:
	# the constructor
	def __init__(self, name, image):
		# rooms have a name, an image (the name of a file), exits (e.g., south), exit locations
		# (e.g., to the south is room n), items (e.g., table), item descriptions (for each item),
		# and grabbables (things that can be taken into inventory)
		self.name = name
		self.image = image
		self.exits = {}
		self.items = {}
		self.grabbables = []
		self.itemList = []

	# getters and setters for the instance variables
	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, value):
		self._name = value

	@property
	def image(self):
		return self._image

	@image.setter
	def image(self, value):
		self._image = value

	@property
	def exits(self):
		return self._exits

	@exits.setter
	def exits(self, value):
		self._exits = value

	@property
	def items(self):
		return self._items

	@items.setter
	def items(self, value):
		self._items = value

	@property
	def grabbables(self):
		return self._grabbables

	@grabbables.setter
	def grabbables(self, value):
		self._grabbables = value
	
	@property
	def itemList(self):
		return self._itemList
	@itemList.setter
	def itemList(self, value):
		self._itemList = value

	# adds an exit to the room
	# the exit is a string (e.g., north)
	# the room is an instance of a room
	def addExit(self, exit, room):
		# append the exit and room to the appropriate dictionary
		self._exits[exit] = room

	# adds an item to the room
	# the item is a string (e.g., table)
	# the desc is a string that describes the item (e.g., it is made of wood)
	def addItem(self, item, desc):
		# append the item and description to the appropriate dictionary
		self._items[item] = desc
		self.itemList.append(item)

	# adds a grabbable item to the room
	# the item is a string (e.g., key)
	def addGrabbable(self, item):
		# append the item to the list
		self._grabbables.append(item)

	# removes a grabbable item from the room
	# the item is a string (e.g., key)
	def delGrabbable(self, item):
		# remove the item from the list
		self._grabbables.remove(item)

	# returns a string description of the room
	def __str__(self):
		# first, the room name
		s = "You are in {}.\n".format(self.name)

		# next, the items in the room
		s += "You see: "
		for item in self.items.keys():
			s += item + " "
		s += "\n"

		# next, the exits from the room
		s += "Exits: "
		for exit in self.exits.keys():
			s += exit + " "

		return s
	
class Image:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width*scale), int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))
	

# the game class
class Game:
	# the constructor
	def __init__(self):
		""""""

	# creates the rooms
	def createRooms(self):
		pass
	# sets up the GUI
	def setupGUI(self):
		pass
	# sets the current room image
	def setRoomImage(self):
		pass
	# sets the status displayed on the right of the GUI
	def setStatus(self, status):
		pass

	# plays the game
	def play(self):
		# add the rooms to the game
		self.createRooms()
		# configure the GUI
		self.setupGUI()
		# set the current room
		self.setRoomImage()
		# set the current status
		self.setStatus("")

	# processes the player's input
	def process(self, event):
		pass


r1 = Room("Room 1", Room1Img)
Room1 = Image(0, 0, Room1Img, 1)
r2 = Room("Room 2", Room2Img)
Room2 = Image(0, 0, Room2Img, 1)
r3 = Room("Room 3", Room3Img)
Room3 = Image(0, 0, Room3Img, 1)
r4 = Room("Room 4", Room4Img)
Room4 = Image(0, 0, Room4Img, 1)
Skull = Image(0, 0, SkullImg, 1)
inv = []

r1Data = f"You are in Room 1.\nYou see: Chair, Table\nExits: East, South\nYou are carrying: {inv}"
r2Data = f"You are in Room 2.\nYou see: Rug, Fireplace\nExits: West, South\nYou are carrying: {inv}"
r3Data = f"You are in Room 3.\nYou see: Bookshelves, Statue, Desk\nExits: East, North\nYou are carrying: {inv}"
r4Data = f"You are in Room 4.\nYou see: Brew-Rig\nExits: West, North\nYou are carrying: {inv}"

	
# exits
r1.addExit("East", r2)
r1.addExit("South", r3)
r2.addExit("West", r1)
r2.addExit("South", r4)
r3.addExit("North", r1)
r3.addExit("East", r4)
r4.addExit("West", r3)
r4.addExit("North", r2)
r4.addExit("South", None)

# items
r1.addItem("Chair", "It's a chair, you can try sitting on it I guess.")
r1.addGrabbable("Key")
r1.addItem("Table", "More of a coffe table, but what do I know? I mean, other than that key sitting on it")
r2.addItem("Rug", "You could walk on it, but it looks pretty dirty.")
r2.addItem("Fireplace", "It is currently being used, but as far as you can tell there is no one else here.")
r3.addGrabbable("Book")
r3.addItem("Bookshelves", "They hold books. Hey there's a weirdly looking animated one there!")
r3.addItem("Desk", "You can see a statue on the desk.")
r3.addItem("Statue", "He's just a little dude. Just vibing.")
r4.addGrabbable("6-pack")
r4.addItem("Brew-Rig", "Used to create an elegant beverage. Oh, there's also a 6-pack on the ground, nice.")


def blit_text(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width = 800
    max_height = 550
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

def box_text(surface, font, x_start, x_end, y_start, text, colour):
        x = x_start
        y = y_start
        words = text.split(' ')

        for word in words:
            word_t = font.render(word, True, colour)
            if word_t.get_width() + x <= x_end:
                surface.blit(word_t, (x, y))
                x += word_t.get_width() * 1.1
            else:
                y += word_t.get_height() * 1.1
                x = x_start
                surface.blit(word_t, (x, y))
                x += word_t.get_width() * 1.1


def RunGame():
	Room1.draw(DISPLAYSURF)
	box_text(DISPLAYSURF, font, 400, 750, 50, r1Data, black)
	pygame.display.flip()
	currentRoom = "Room 1"
	playerInput = ""
	textOut = "Whenever you submit text, the result will display here!  Some commands you can do are 'go', 'look', and 'take'."
	asked = False
	dead = False
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.display.quit()
				pygame.quit()
				break
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					textOut = playerInput.strip()
					playerInput = ""
					asked = True
				if event.key == pygame.K_BACKSPACE:
					playerInput = playerInput[:-1]
				else:
					playerInput += event.unicode
		check = textOut.lower()
		checker = check.split(" ")
		# Room 1 checker
		if currentRoom == "Room 1":
			roomData = r1Data
			if "quit" in checker or "exit" in checker or "bye" in checker or "sionara!" in checker:
				dead = True
			if "go" in checker:
				if "east" in checker:
					currentRoom = "Room 2"
					asked = False
				if "south" in checker:
					currentRoom = "Room 3"
					asked = False
			elif "look" in checker:
				for word in checker:
					word = word.capitalize()
					if word in r1.itemList:
						textOut = r1.items[word]
						asked = True
			elif "take" in checker:
				if "key" in checker:
					inv.append("Key")
					asked = True

		# Room 2 checker
		if currentRoom == "Room 2":
			roomData = r2Data
			if "quit" in checker or "exit" in checker or "bye" in checker or "sionara!" in checker:
				dead = True
			if "go" in checker:
				if "west" in checker:
					currentRoom = "Room 1"
					asked = False
				if "south" in checker:
					currentRoom = "Room 4"
					asked = False
			elif "look" in checker:
				for word in checker:
					word = word.capitalize()
					if word in r1.itemList:
						textOut = r1.items[word]
						asked = True


		# Room 3 checker
		if currentRoom == "Room 3":
			roomData = r3Data
			if "quit" in checker or "exit" in checker or "bye" in checker or "sionara!" in checker:
				dead = True
			if "go" in checker:
				if "east" in checker:
					currentRoom = "Room 4"
					asked = False
				if "north" in checker:
					currentRoom = "Room 1"
					asked = False
			elif "look" in checker:
				for word in checker:
					word = word.capitalize()
					if word in r1.itemList:
						textOut = r1.items[word]
						asked = True
			elif "take" in checker:
				if "book" in checker:
					inv.append("Book")
					asked = True

		# Room 4 checker
		if currentRoom == "Room 4":
			roomData = r4Data
			if "quit" in checker or "exit" in checker or "bye" in checker or "sionara!" in checker:
				dead = True
			if "go" in checker:
				if "west" in checker:
					currentRoom = "Room 3"
					asked = False
				if "north" in checker:
					currentRoom = "Room 2"
					asked = False
				if "south" in checker:
					dead = True
			elif "look" in checker:
				for word in checker:
					word = word.capitalize()
					if word in r1.itemList:
						textOut = r1.items[word]
						asked = True
			elif "take" in checker:
				if "6-pack" in checker:
					inv.append("6-pack")
					asked = True
		
		# Done checking
		if dead:
			DISPLAYSURF.fill(black)
			Skull.draw(DISPLAYSURF)
		else:
			DISPLAYSURF.fill(white)
			Room1.draw(DISPLAYSURF) if currentRoom == "Room 1" else None
			Room2.draw(DISPLAYSURF) if currentRoom == "Room 2" else None
			Room3.draw(DISPLAYSURF) if currentRoom == "Room 3" else None
			Room4.draw(DISPLAYSURF) if currentRoom == "Room 4" else None
			pygame.draw.rect(DISPLAYSURF, black, inputTextBox)
			pygame.draw.rect(DISPLAYSURF, white, Output)
			text_surface = font.render(playerInput.strip(), True, black) if not playerInput.isspace() else font.render("", True, black)
			DISPLAYSURF.blit(text_surface, (0, 550))
			blit_text(DISPLAYSURF,roomData, (400, 0), font, black)			
			blit_text(DISPLAYSURF, textOut , (400, 150), font, black) if asked else blit_text(DISPLAYSURF, "Whenever you submit text, the result will display here!  Some commands you can do are 'go', 'look', and 'take'." , (400, 150), font, black)

		pygame.display.flip()
		clock.tick(60)

RunGame()