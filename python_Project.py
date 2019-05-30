
class Board:


	def __init__(self):
		self.boardVisual = [[" ~ "]*10 for n in range(10)]

		# boardShoot will also serve as the bot's board
		self.boardShoot = [[0]*8 for n in range(8)]
		self.boardPlayer = [[0]*8 for n in range(8)]


		self.firstShipSlot = True
		self.hasToBeVertical = False
		self.hasToBeHorizontal = False

		self.lastInputedRow = -3
		self.lastInputedCol = -3

		self.row = 0
		self.col = 0

		self.bots5SlottedShip = []
		self.bots4SlottedShip = []
		self.bots3SlottedShip = []

		self.players5SlottedShip = []
		self.players4SlottedShip = []
		self.players3SlottedShip = []

		self.isPlayers5SlottedShipHit = False
		self.isPlayers4SlottedShipHit = False
		self.isPlayers3SlottedShipHit = False
		

 ############################################################################################

 	def stopBlinkingEverything(self):

		blink = "\033[05m{}"
		white = "\033[1;37;40m{}"
		red = "\033[1;91;40m{}"

 		for row in range(10):
			for col in range(10):
				temp = self.boardVisual[row][col]

				if temp == blink.format(white.format(" O ")):
					self.boardVisual[row][col] = white.format(" O ")

				elif temp == blink.format(red.format(" X ")):
					self.boardVisual[row][col] = red.format(" X ")



	def createBoard(self):
		# Top Border
		for col in range(10):
			self.boardVisual[0][col] = "***"


		# Bottom Border
		for col in range(10):
			self.boardVisual[9][col] = "***"


		# Left Border
		for row in range(10):
			self.boardVisual[row][0] = "* "

			if row == 0:
				self.boardVisual[row][0] = "   *"

			elif row == 1:
				self.boardVisual[row][0] = "A  *"

			elif row == 2:
				self.boardVisual[row][0] = "B  *"

			elif row == 3:
				self.boardVisual[row][0] = "C  *"

			elif row == 4:
				self.boardVisual[row][0] = "D  *"

			elif row == 5:
				self.boardVisual[row][0] = "E  *"

			elif row == 6:
				self.boardVisual[row][0] = "F  *"

			elif row == 7:
				self.boardVisual[row][0] = "G  *"

			elif row == 8:
				self.boardVisual[row][0] = "H  *"

			elif row == 9:
				self.boardVisual[row][0] = "   *"


		# Right Border
		for row in range(10):
			self.boardVisual[row][9] = "*"

 ############################################################################################


	def printBoard(self):
		cyan = "\033[25m\033[1;36;40m{}" 
		gray = "\033[25m\033[1;90;40m{}"

		print ("      1   2   3   4   5   6   7   8  ")

		for row in range(10):
			for col in range(10):
				if (col == 9):
					if self.boardVisual[row][col] != " ~ " and self.boardVisual[row][col] != " # " and self.boardVisual[row][col] != " O ":
						print(gray.format(self.boardVisual[row][col]))

				elif self.boardVisual[row][col] != " ~ " and self.boardVisual[row][col] != " # " and self.boardVisual[row][col] != " O ":
					print(gray.format(self.boardVisual[row][col])),
				elif self.boardVisual[row][col] == " ~ ":
					#print(self.boardVisual[row][col]),
					print(cyan.format(self.boardVisual[row][col])),
				else:
					print(self.boardVisual[row][col]),

 ############################################################################################


	def repPlayerBoard(self , slot , shipColor):
		row = 0
		col = 0
		slot = slot.upper()

		if slot[0] == "A":
			row = 0

		elif slot[0] == "B":
			row = 1

		elif slot[0] == "C":
			row = 2

		elif slot[0] == "D":
			row = 3

		elif slot[0] == "E":
			row = 4

		elif slot[0] == "F":
			row = 5

		elif slot[0] == "G":
			row = 6

		elif slot[0] == "H":
			row = 7




		if slot[1] == "1":
			col = 0

		elif slot[1] == "2":
			col = 1

		elif slot[1] == "3":
			col = 2

		elif slot[1] == "4":
			col = 3

		elif slot[1] == "5":
			col = 4

		elif slot[1] == "6":
			col = 5

		elif slot[1] == "7":
			col = 6

		elif slot[1] == "8":
			col = 7


		self.boardPlayer[row][col] = 3
		self.boardVisual[row + 1][col + 1] = shipColor.format(" # ")

 ############################################################################################


	def isIncorrectInput(self , slot , slotNum):
		correctInput = False
		correctRow = False
		correctCol = False
		row , col = 0 , 0
			
		slot = slot.upper()

		if slot[0] == "A":
			row = 0
			correctRow = True

		elif slot[0] == "B":
			row = 1 
			correctRow = True

		elif slot[0] == "C":
			row = 2 
			correctRow = True

		elif slot[0] == "D":
			row = 3
			correctRow = True

		elif slot[0] == "E":
			row = 4
			correctRow = True

		elif slot[0] == "F":
			row = 5
			correctRow = True

		elif slot[0] == "G":
			row = 6
			correctRow = True

		elif slot[0] == "H":
			row = 7
			correctRow = True

		else:
			print("Input Error: (A - H and 1 - 8)")
			return True



		if slot[1] == "1":
			col = 0
			correctCol = True

		elif slot[1] == "2":
			col = 1
			correctCol = True

		elif slot[1] == "3":
			col = 2
			correctCol = True

		elif slot[1] == "4":
			col = 3
			correctCol = True

		elif slot[1] == "5":
			col = 4
			correctCol = True

		elif slot[1] == "6":
			col = 5
			correctCol = True

		elif slot[1] == "7":
			col = 6
			correctCol = True

		elif slot[1] == "8":
			col = 7
			correctCol = True 

		else:
			print("Input Error: (A - H and 1 - 8)")
			return True


		if self.boardPlayer[row][col] == 3:
			correctRow = False
			correctCol = False
			print("Error: Ship is already placed there")


		if not self.firstShipSlot and correctRow and correctCol:
			if self.boardPlayer[row][col] == 3:
				correctRow = False
				correctCol = False
				correctInput = True # to skip the "can't split ship" comment
				print("Error: Ship is already placed there")

			elif slotNum >= 2:
				if self.hasToBeHorizontal:
					if col + 1 != 8 and not correctInput:
						if self.boardPlayer[row][col + 1] == 3:
							correctInput = True

					if col - 1 != -1 and not correctInput:
						if self.boardPlayer[row][col - 1] == 3:
							correctInput = True

				elif self.hasToBeVertical:
					if row + 1 != 8 and not correctInput:
						if self.boardPlayer[row + 1][col] == 3:
							correctInput = True

					if row - 1 != -1 and not correctInput:
						if self.boardPlayer[row - 1][col] == 3:
							correctInput = True


			else:

				if col + 1 != 8 and not correctInput:
					if self.boardPlayer[row][col + 1] == 3:
						correctInput = True

				if col - 1 != -1 and not correctInput:
					if self.boardPlayer[row][col - 1] == 3:
						correctInput = True

				if row + 1 != 8 and not correctInput:
					if self.boardPlayer[row + 1][col] == 3:
						correctInput = True

				if row - 1 != -1 and not correctInput:
					if self.boardPlayer[row - 1][col] == 3:
						correctInput = True

			
			if not correctInput:
				correctRow = False
				correctCol = False
				print("Error: Can't split ship") 


		if correctRow and correctCol:
			self.firstShipSlot = False

			if self.lastInputedRow == -3 and self.lastInputedCol == -3:
				self.lastInputedRow = row
				self.lastInputedCol = col

			elif self.lastInputedRow == row + 1 or self.lastInputedRow == row - 1:
				self.hasToBeVertical = True

			elif self.lastInputedCol == col + 1 or self.lastInputedCol == col - 1:
				self.hasToBeHorizontal = True

			return False
	

		return True


 ############################################################################################


	def getPlayerInputedRow(self , slotStr):
			
		row = -1
		slotStr = slotStr.upper()

		if slotStr[0] == "A":
			row = 0
			
		elif slotStr[0] == "B":
			row = 1 
			

		elif slotStr[0] == "C":
			row = 2 
			

		elif slotStr[0] == "D":
			row = 3
			

		elif slotStr[0] == "E":
			row = 4
			

		elif slotStr[0] == "F":
			row = 5
			

		elif slotStr[0] == "G":
			row = 6
			

		elif slotStr[0] == "H":
			row = 7

		return row
			
 ############################################################################################

 	def getPlayerInputedCol(self, slotStr):

 		col = -1
 		slotStr = slotStr.upper()

 		if slotStr[1] == "1":
			col = 0
			
		elif slotStr[1] == "2":
			col = 1
			
		elif slotStr[1] == "3":
			col = 2
			
		elif slotStr[1] == "4":
			col = 3
			
		elif slotStr[1] == "5":
			col = 4
			
		elif slotStr[1] == "6":
			col = 5
			
		elif slotStr[1] == "7":
			col = 6
			
		elif slotStr[1] == "8":
			col = 7
		
		return col

 ############################################################################################


	def placePlayerShips(self):
		
		gray = "\033[1;90;40m"
		green = "\033[1;92;40m{}"
		yellow = "\033[1;93;40m{}"
		magenta = "\033[1;95;40m{}"

		slotNum = 0
		print(green.format("Place 5 Slot Ship: (1 slot at a time, Exp: A1)"))

		while slotNum != 5:
			slotStr = raw_input( green.format(str(slotNum + 1) + " Slot: "))

			while len(slotStr) > 2 or len(slotStr) < 2 or self.isIncorrectInput(slotStr , slotNum):
				
				if len(slotStr) > 2 or len(slotStr) < 2:
					print("Input Error: (Input Ex: A5 or B2 ect.)")
				
				print("Try Again")
				slotStr = raw_input( str(slotNum + 1) + " Slot: ")

			row = self.getPlayerInputedRow(slotStr)
			col = self.getPlayerInputedCol(slotStr)
			self.players5SlottedShip.append(str(row)+str(col))

			shipColor = green
			slotNum += 1
			self.repPlayerBoard(slotStr, shipColor)
			print(gray.format("\nPlayerBoard"))
			self.printBoard()


		slotNum = 0
		self.firstShipSlot = True
		self.hasToBeHorizontal = False
		self.hasToBeVertical = False
		self.lastInputedRow = -3
		self.lastInputedCol = -3
		print(yellow.format("Place 4 Slot Ship: (1 slot at a time, Exp: A1)"))

		while slotNum != 4:
			slotStr = raw_input( yellow.format(str(slotNum + 1) + " Slot: "))

			while len(slotStr) > 2 or len(slotStr) < 2 or self.isIncorrectInput(slotStr , slotNum):
				
				if len(slotStr) > 2 or len(slotStr) < 2:
					print("Input Error: (Input Ex: A5 or B2 ect.)")
				
				print("Try Again")
				slotStr = raw_input( str(slotNum + 1) + " Slot: ")


			row = self.getPlayerInputedRow(slotStr)
			col = self.getPlayerInputedCol(slotStr)
			self.players4SlottedShip.append(str(row)+str(col))

			slotNum += 1
			shipColor = yellow
			self.repPlayerBoard(slotStr , shipColor)
			print(gray.format("\nPlayerBoard"))
			self.printBoard()



		slotNum = 0
		self.firstShipSlot = True
		self.hasToBeHorizontal = False
		self.hasToBeVertical = False
		self.lastInputedRow = -3
		self.lastInputedCol = -3
		print(magenta.format("Place 3 Slot Ship: (1 slot at a time, Exp: A1)"))

		while slotNum != 3:
			slotStr = raw_input( magenta.format(str(slotNum + 1) + " Slot: "))

			while len(slotStr) > 2 or len(slotStr) < 2 or self.isIncorrectInput(slotStr , slotNum):
				
				if len(slotStr) > 2 or len(slotStr) < 2:
					print("Input Error: (Input Ex: A5 or B2 ect.)")
				
				print("Try Again")
				slotStr = raw_input( str(slotNum + 1) + " Slot: ")


			row = self.getPlayerInputedRow(slotStr)
			col = self.getPlayerInputedCol(slotStr)
			self.players3SlottedShip.append(str(row)+str(col))

			slotNum += 1
			shipColor = magenta
			self.repPlayerBoard(slotStr , shipColor)
			print(gray.format("\nPlayerBoard"))
			self.printBoard()

 ############################################################################################

 	def placeBotsShips(self):

 		self.placeBots5SlottedShip()
 		self.placeBots4SlottedShip()
 		self.placeBots3SlottedShip()
 		

 ############################################################################################


 	def placeBots5SlottedShip(self):
 		import random
		
		row = random.randint(0,7)
		col = random.randint(0,7)

		unusedNums = [0,1,2,3,4,5]
		botPlacedShip = False

		while not botPlacedShip:
			temp = len(unusedNums) - 1 
			randIdx = random.randint(0,temp)
			randNum = unusedNums[randIdx]
			unusedNums.pop(randIdx)

			if randNum == 0:
				# Center place left and right (Horizontally)
				if col + 2 <= 7 and col - 2 >= 0 and self.boardShoot[row][col] != 3 and self.boardShoot[row][col + 1] != 3 and self.boardShoot[row][col + 2] != 3 and self.boardShoot[row][col-1] != 3 and self.boardShoot[row][col-2] != 3:
					self.boardShoot[row][col] = 3
					self.boardShoot[row][col + 1] = 3
					self.boardShoot[row][col + 2] = 3
					self.boardShoot[row][col - 1] = 3
					self.boardShoot[row][col - 2] = 3

					self.bots5SlottedShip.append(str(row) + str(col))
					self.bots5SlottedShip.append(str(row) + str(col+1))
					self.bots5SlottedShip.append(str(row) + str(col+2))
					self.bots5SlottedShip.append(str(row) + str(col-1))
					self.bots5SlottedShip.append(str(row) + str(col-2))
					
					botPlacedShip = True

			elif randNum == 1:
				# Center place up and down (Vertically)
				if row + 2 <= 7 and row - 2 >= 0 and self.boardShoot[row][col] != 3 and self.boardShoot[row+1][col] != 3 and self.boardShoot[row+2][col] != 3 and self.boardShoot[row-1][col] != 3 and self.boardShoot[row-2][col] != 3:
					self.boardShoot[row][col] = 3
					self.boardShoot[row + 1][col] = 3
					self.boardShoot[row + 2][col] = 3
					self.boardShoot[row - 1][col] = 3
					self.boardShoot[row - 2][col] = 3

					self.bots5SlottedShip.append(str(row) + str(col))
					self.bots5SlottedShip.append(str(row+1) + str(col))
					self.bots5SlottedShip.append(str(row+2) + str(col))
					self.bots5SlottedShip.append(str(row-1) + str(col))
					self.bots5SlottedShip.append(str(row-2) + str(col))
					
					botPlacedShip = True


			elif randNum == 2:
				# Edge/Corner place right and right (Horizontally)
				if col + 4 <= 7 and self.boardShoot[row][col] != 3 and self.boardShoot[row][col+1] != 3 and self.boardShoot[row][col+2] != 3 and self.boardShoot[row][col+3] != 3 and self.boardShoot[row][col+4] != 3:
					self.boardShoot[row][col] = 3
					self.boardShoot[row][col + 1] = 3
					self.boardShoot[row][col + 2] = 3
					self.boardShoot[row][col + 3] = 3
					self.boardShoot[row][col + 4] = 3
					self.bots5SlottedShip.append(str(row) + str(col))
					self.bots5SlottedShip.append(str(row) + str(col+1))
					self.bots5SlottedShip.append(str(row) + str(col+2))
					self.bots5SlottedShip.append(str(row) + str(col+3))
					self.bots5SlottedShip.append(str(row) + str(col+4))
					
					botPlacedShip = True

			elif randNum == 3:
				# Edge/Corner place left and left (Horizontally)
				if col - 4 >= 0 and self.boardShoot[row][col] != 3 and self.boardShoot[row][col-1] != 3 and self.boardShoot[row][col-2] != 3 and self.boardShoot[row][col-3] != 3 and self.boardShoot[row][col-4] != 3:
					self.boardShoot[row][col] = 3
					self.boardShoot[row][col - 1] = 3
					self.boardShoot[row][col - 2] = 3
					self.boardShoot[row][col - 3] = 3
					self.boardShoot[row][col - 4] = 3
					self.bots5SlottedShip.append(str(row) + str(col))
					self.bots5SlottedShip.append(str(row) + str(col-1))
					self.bots5SlottedShip.append(str(row) + str(col-2))
					self.bots5SlottedShip.append(str(row) + str(col-3))
					self.bots5SlottedShip.append(str(row) + str(col-4))
					
					botPlacedShip = True

			elif randNum == 4:
				# Edge/Corner place up and up (Vertically)
				if row + 4 <= 7 and self.boardShoot[row][col] != 3 and self.boardShoot[row+1][col] != 3 and self.boardShoot[row+2][col] != 3 and self.boardShoot[row+3][col] != 3 and self.boardShoot[row+4][col] != 3:
					self.boardShoot[row][col] = 3
					self.boardShoot[row + 1][col] = 3
					self.boardShoot[row + 2][col] = 3
					self.boardShoot[row + 3][col] = 3
					self.boardShoot[row + 4][col] = 3
					self.bots5SlottedShip.append(str(row) + str(col))
					self.bots5SlottedShip.append(str(row+1) + str(col))
					self.bots5SlottedShip.append(str(row+2) + str(col))
					self.bots5SlottedShip.append(str(row+3) + str(col))
					self.bots5SlottedShip.append(str(row+4) + str(col))
					
					botPlacedShip = True

			elif randNum == 5:
				# Edge/Corner place down and down (Vertically)
				if row - 4 >= 0 and self.boardShoot[row][col] != 3 and self.boardShoot[row-1][col] != 3 and self.boardShoot[row-2][col] != 3 and self.boardShoot[row-3][col] != 3 and self.boardShoot[row-4][col] != 3:
					self.boardShoot[row][col] = 3
					self.boardShoot[row - 1][col] = 3
					self.boardShoot[row - 2][col] = 3
					self.boardShoot[row - 3][col] = 3
					self.boardShoot[row - 4][col] = 3
					self.bots5SlottedShip.append(str(row) + str(col))
					self.bots5SlottedShip.append(str(row-1) + str(col))
					self.bots5SlottedShip.append(str(row-2) + str(col))
					self.bots5SlottedShip.append(str(row-3) + str(col))
					self.bots5SlottedShip.append(str(row-4) + str(col))
					
					botPlacedShip = True

			if len(unusedNums) == 0 and not botPlacedShip:
				unusedNums = [0,1,2,3,4,5]
				row = random.randint(0,7)
				col = random.randint(0,7)

 ############################################################################################


 	def placeBots4SlottedShip(self):
 		import random
		
		row = random.randint(0,7)
		col = random.randint(0,7)

		unusedNums = [0,1,2,3]
		botPlacedShip = False

		while not botPlacedShip:
			temp = len(unusedNums) - 1
			randIdx = random.randint(0,temp)
			randNum = unusedNums[randIdx]
			unusedNums.pop(randIdx)


			if randNum == 0:
				# Edge/Corner place right and right and left (Horizontally)
				if col - 1 >= 0 and col + 2 <= 7 and self.boardShoot[row][col] != 3 and self.boardShoot[row][col+1] != 3 and self.boardShoot[row][col+2] != 3 and self.boardShoot[row][col-1] != 3:
					self.boardShoot[row][col] = 3
					self.boardShoot[row][col + 1] = 3
					self.boardShoot[row][col + 2] = 3
					self.boardShoot[row][col - 1] = 3
					self.bots4SlottedShip.append(str(row) + str(col))
					self.bots4SlottedShip.append(str(row) + str(col+1))
					self.bots4SlottedShip.append(str(row) + str(col+2))
					self.bots4SlottedShip.append(str(row) + str(col-1))
					
					botPlacedShip = True

			elif randNum == 1:
				# Edge/Corner place left and left and right (Horizontally)
				if col + 1 <= 7 and col - 2 >= 0 and self.boardShoot[row][col] != 3 and self.boardShoot[row][col-1] != 3 and self.boardShoot[row][col-2] != 3 and self.boardShoot[row][col+1] != 3:
					self.boardShoot[row][col] = 3
					self.boardShoot[row][col - 1] = 3
					self.boardShoot[row][col - 2] = 3
					self.boardShoot[row][col + 1] = 3
					self.bots4SlottedShip.append(str(row) + str(col))
					self.bots4SlottedShip.append(str(row) + str(col-1))
					self.bots4SlottedShip.append(str(row) + str(col-2))
					self.bots4SlottedShip.append(str(row) + str(col+1))
					
					botPlacedShip = True

			elif randNum == 2:
				# Edge/Corner place up and up and down(Vertically)
				if row - 1 >= 0 and row + 2 <= 7 and self.boardShoot[row][col] != 3 and self.boardShoot[row+1][col] != 3 and self.boardShoot[row+2][col] != 3 and self.boardShoot[row-1][col] != 3:
					self.boardShoot[row][col] = 3
					self.boardShoot[row + 1][col] = 3
					self.boardShoot[row + 2][col] = 3
					self.boardShoot[row - 1][col] = 3
					self.bots4SlottedShip.append(str(row) + str(col))
					self.bots4SlottedShip.append(str(row+1) + str(col))
					self.bots4SlottedShip.append(str(row+2) + str(col))
					self.bots4SlottedShip.append(str(row-1) + str(col))
					
					botPlacedShip = True

			elif randNum == 3:
				# Edge/Corner place down and down and up (Vertically)
				if row + 1 <= 7 and row - 2 >= 0 and self.boardShoot[row][col] != 3 and self.boardShoot[row-1][col] != 3 and self.boardShoot[row-2][col] != 3 and self.boardShoot[row+1][col] != 3:
					self.boardShoot[row][col] = 3
					self.boardShoot[row - 1][col] = 3
					self.boardShoot[row - 2][col] = 3
					self.boardShoot[row + 1][col] = 3
					self.bots4SlottedShip.append(str(row) + str(col))
					self.bots4SlottedShip.append(str(row-1) + str(col))
					self.bots4SlottedShip.append(str(row-2) + str(col))
					self.bots4SlottedShip.append(str(row+1) + str(col))
					
					botPlacedShip = True

			if len(unusedNums) == 0 and not botPlacedShip:
				unusedNums = [0,1,2,3]
				row = random.randint(0,7)
				col = random.randint(0,7)


 ############################################################################################


	def placeBots3SlottedShip(self):
		import random
		
		row = random.randint(0,7)
		col = random.randint(0,7)

		unusedNums = [0,1,2,3,4,5]
		botPlacedShip = False

		while not botPlacedShip:
			temp = len(unusedNums) - 1
			randIdx = random.randint(0,temp)
			randNum = unusedNums[randIdx]
			unusedNums.pop(randIdx)

			if randNum == 0:
				# Center place left and right (Horizontally)
				if col + 1 <= 7 and col - 1 >= 0 and self.boardShoot[row][col] != 3 and self.boardShoot[row][col + 1] != 3 and self.boardShoot[row][col-1] != 3:
					self.boardShoot[row][col] = 3
					self.boardShoot[row][col + 1] = 3
					self.boardShoot[row][col - 1] = 3
					self.bots3SlottedShip.append(str(row) + str(col))
					self.bots3SlottedShip.append(str(row) + str(col+1))
					self.bots3SlottedShip.append(str(row) + str(col-1))
					
					botPlacedShip = True

			elif randNum == 1:
				# Center place up and down (Vertically)
				if row + 1 <= 7 and row - 1 >= 0 and self.boardShoot[row][col] != 3 and self.boardShoot[row+1][col] != 3 and self.boardShoot[row-1][col] != 3:
					self.boardShoot[row][col] = 3
					self.boardShoot[row + 1][col] = 3
					self.boardShoot[row - 1][col] = 3
					self.bots3SlottedShip.append(str(row) + str(col))
					self.bots3SlottedShip.append(str(row+1) + str(col))
					self.bots3SlottedShip.append(str(row-1) + str(col))
					
					botPlacedShip = True


			elif randNum == 2:
				# Edge/Corner place right and right (Horizontally)
				if col + 1 < 7 and col + 2 <= 7 and self.boardShoot[row][col] != 3 and self.boardShoot[row][col+1] != 3 and self.boardShoot[row][col+2] != 3:
					self.boardShoot[row][col] = 3
					self.boardShoot[row][col + 1] = 3
					self.boardShoot[row][col + 2] = 3
					self.bots3SlottedShip.append(str(row) + str(col))
					self.bots3SlottedShip.append(str(row) + str(col+1))
					self.bots3SlottedShip.append(str(row) + str(col+2))
					
					botPlacedShip = True

			elif randNum == 3:
				# Edge/Corner place left and left (Horizontally)
				if col - 1 > 0 and col - 2 >= 0 and self.boardShoot[row][col] != 3 and self.boardShoot[row][col-1] != 3 and self.boardShoot[row][col-2] != 3:
					self.boardShoot[row][col] = 3
					self.boardShoot[row][col - 1] = 3
					self.boardShoot[row][col - 2] = 3
					self.bots3SlottedShip.append(str(row) + str(col))
					self.bots3SlottedShip.append(str(row) + str(col-1))
					self.bots3SlottedShip.append(str(row) + str(col-2))
					
					botPlacedShip = True

			elif randNum == 4:
				# Edge/Corner place up and up (Vertically)
				if row + 1 < 7 and row + 2 <= 7 and self.boardShoot[row][col] != 3 and self.boardShoot[row+1][col] != 3 and self.boardShoot[row+2][col] != 3:
					self.boardShoot[row][col] = 3
					self.boardShoot[row + 1][col] = 3
					self.boardShoot[row + 2][col] = 3
					self.bots3SlottedShip.append(str(row) + str(col))
					self.bots3SlottedShip.append(str(row+1) + str(col))
					self.bots3SlottedShip.append(str(row+2) + str(col))
					
					botPlacedShip = True

			elif randNum == 5:
				# Edge/Corner place down and down (Vertically)
				if row - 1 > 0 and row - 2 >= 0 and self.boardShoot[row][col] != 3 and self.boardShoot[row-1][col] != 3 and self.boardShoot[row-2][col] != 3:
					self.boardShoot[row][col] = 3
					self.boardShoot[row - 1][col] = 3
					self.boardShoot[row - 2][col] = 3
					self.bots3SlottedShip.append(str(row) + str(col))
					self.bots3SlottedShip.append(str(row-1) + str(col))
					self.bots3SlottedShip.append(str(row-2) + str(col))
					
					botPlacedShip = True

			if len(unusedNums) == 0 and not botPlacedShip:
				unusedNums = [0,1,2,3,4,5]
				row = random.randint(0,7)
				col = random.randint(0,7)

 ############################################################################################


	def printBotsPlacedShips(self):

		for row in range(8):
			for col in range(8):
				if self.boardShoot[row][col] == 3:
					self.boardVisual[row + 1][col + 1] = " # "


		for row in range(10):
			for col in range(10):
				if col == 9:
					print(self.boardVisual[row][col])
				else:
					print(self.boardVisual[row][col]),

 ############################################################################################


	def isIncorrectShotInput(self , shotStr):
		
		shotStr = shotStr.upper()

		if shotStr[0] == "A":
			self.row = 0

		elif shotStr[0] == "B":
			self.row = 1

		elif shotStr[0] == "C":
			self.row = 2

		elif shotStr[0] == "D":
			self.row = 3

		elif shotStr[0] == "E":
			self.row = 4

		elif shotStr[0] == "F":
			self.row = 5

		elif shotStr[0] == "G":
			self.row = 6

		elif shotStr[0] == "H":
			self.row = 7

		else:
			print("Input Error: (A - H and 1 - 8)")
			return True



		if shotStr[1] == "1":
			self.col = 0

		elif shotStr[1] == "2":
			self.col = 1

		elif shotStr[1] == "3":
			self.col = 2

		elif shotStr[1] == "4":
			self.col = 3

		elif shotStr[1] == "5":
			self.col = 4

		elif shotStr[1] == "6":
			self.col = 5

		elif shotStr[1] == "7":
			self.col = 6

		elif shotStr[1] == "8":
			self.col = 7

		else:
			print("Input Error: (A - H and 1 - 8)")
			return True


		if playerBoardShoot.boardShoot[self.row][self.col] == 1 or self.boardShoot[self.row][self.col] == 2:
			print("Already Shot There")
			return True

		return False

			
 ############################################################################################


	def playerShoots(self):

		blink = "\033[05m{}"
		white = "\033[1;37;40m{}"
		red = "\033[1;91;40m{}"

		shotStr = raw_input("Shoot: ")

		while len(shotStr) > 2 or len(shotStr) < 2 or self.isIncorrectShotInput(shotStr):
				
				if len(shotStr) > 2 or len(shotStr) < 2:
					print("Input Error: (Input Ex: A5 or B2 ect.)")
				
				print("Try Again")
				shotStr = raw_input("Shoot: ")
		

		if self.boardShoot[self.row][self.col] == 0:
			print(gray.format("\n\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"))
			print(white.format("\nPlayer Miss!"))
			self.boardShoot[self.row][self.col] = 2
			self.boardVisual[self.row+1][self.col+1] = blink.format(white.format(" O "))


		elif self.boardShoot[self.row][self.col] == 3:
			print(gray.format("\n\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"))
			print(red.format("\nPlayer Hit!"))
			self.boardShoot[self.row][self.col] = 1
			self.boardVisual[self.row + 1][self.col + 1] = blink.format(red.format(" X ")) 

			for x in range(len(self.bots5SlottedShip)):
				if self.bots5SlottedShip[x] == (str(self.row) + str(self.col)):
					self.bots5SlottedShip.remove(str(self.row)+str(self.col))
					print(red.format("Player Hit Bot's 5 Slotted Ship!"))
					if len(self.bots5SlottedShip) == 0:
						print(red.format("Player Destoryed Bot's 5 Slotted Ship!"))
					break

			for x in range(len(self.bots4SlottedShip)):
				if self.bots4SlottedShip[x] == (str(self.row) + str(self.col)):
					self.bots4SlottedShip.remove(str(self.row) + str(self.col))
					print(red.format("Player Hit Bot's 4 Slotted Ship!"))
					if len(self.bots4SlottedShip) == 0:
						print(red.format("Player Destoryed Bot's 4 Slotted Ship!"))
					break

			for x in range(len(self.bots3SlottedShip)):
				if self.bots3SlottedShip[x] == (str(self.row) + str(self.col)):
					self.bots3SlottedShip.remove(str(self.row) + str(self.col))
					print(red.format("Player Hit Bot's 3 Slotted Ship!"))
					if len(self.bots3SlottedShip) == 0:
						print(red.format("Player Destoryed Bot's 3 Slotted Ship!"))
					break

 ############################################################################################

 	def botShoots(self):

 		blink = "\033[05m{}"
 		white = "\033[1;37;40m{}"
 		red = "\033[1;91;40m{}"

 		row = random.randint(0,7)
 		col = random.randint(0,7)


 		if self.isPlayers5SlottedShipHit:
 			temp = len(self.players5SlottedShip)
 			if temp != 0:
 				temp = temp - 1

 			tempIdx = random.randint(0,temp)
 			tempStr = self.players5SlottedShip[tempIdx]
 			row = int(tempStr[0])
 			col = int(tempStr[1])


 		elif self.isPlayers4SlottedShipHit:
 			temp = len(self.players4SlottedShip)
 			if temp != 0:
 				temp = temp - 1

 			tempIdx = random.randint(0,temp)
 			tempStr = self.players4SlottedShip[tempIdx]
 			row = int(tempStr[0])
 			col = int(tempStr[1])


 		elif self.isPlayers3SlottedShipHit:
 			temp = len(self.players3SlottedShip)
 			if temp != 0:
 				temp = temp - 1

 			tempIdx = random.randint(0,temp)
 			tempStr = self.players3SlottedShip[tempIdx]
 			row = int(tempStr[0])
 			col = int(tempStr[1])


 		if self.boardPlayer[row][col] == 1 or self.boardPlayer[row][col] == 2:
 			
 			while self.boardPlayer[row][col] == 1 or self.boardPlayer[row][col] == 2:
 				#print("Bot Already Shot There Bot Shooting Again!")
 				row = random.randint(0,7)
 				col = random.randint(0,7)


 		if self.boardPlayer[row][col] == 0:
 			print(gray.format("\n\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n"))
 			print(white.format("Bot Missed!"))
 			self.boardPlayer[row][col] = 2
 			self.boardVisual[row+1][col+1] = blink.format(white.format(" O "))

 		elif self.boardPlayer[row][col] == 3:
 			print(gray.format("\n\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n"))
 			print(red.format("Bot Hit!"))
 			self.boardPlayer[row][col] = 1
 			self.boardVisual[row + 1][col + 1] = blink.format(red.format(" X "))


 			if len(self.players5SlottedShip) != 0:
 				for x in range(len(self.players5SlottedShip)):
 					if self.players5SlottedShip[x] == (str(row) + str(col)):
 						print(red.format("Bot Hit Player's 5 Slotted Ship!"))
 						self.players5SlottedShip.pop(x)
 						self.isPlayers5SlottedShipHit = True

 						if len(self.players5SlottedShip) == 0:
 							print(red.format("Bot Destoryed Player's 5 Slotted Ship!"))
 							self.isPlayers5SlottedShipHit = False

 						break


 			if len(self.players4SlottedShip) != 0:
 				for x in range(len(self.players4SlottedShip)):
 					if self.players4SlottedShip[x] == (str(row) + str(col)):
 						print(red.format("Bot Hit Player's 4 Slotted Ship!"))
 						self.players4SlottedShip.pop(x)
 						self.isPlayers4SlottedShipHit = True

 						if len(self.players4SlottedShip) == 0:
 							print(red.format("Bot Destoryed Player's 4 Slotted Ship!"))
 							self.isPlayers4SlottedShipHit = False
 							 
 						break


 			if len(self.players3SlottedShip) != 0:
 				for x in range(len(self.players3SlottedShip)):
 					if self.players3SlottedShip[x] == (str(row) + str(col)):
 						print(red.format("Bot Hit Player's 3 Slotted Ship!"))
 						self.players3SlottedShip.pop(x)
 						self.isPlayers3SlottedShipHit = True
 							
 						if len(self.players3SlottedShip) == 0:
 							print(red.format("Bot Destoryed Player's 3 Slotted Ship!"))
 							self.isPlayers3SlottedShipHit = False

 						break


 ############################################################################################


# Empty = 0
# Hit = 1
# Miss = 2
# Ship = 3


# Main

import random
import time

gray = "\033[1;90;40m{}"
white = "\033[1;97;40m{}\033[90m"
green = "\033[1;92;40m{}"
yellow = "\033[1;93;40m{}"
magenta = "\033[1;95;40m{}\033[90m"

title = "\033[94m\033[4m\033[3m{}\033[00m\033[1;90;40m"

print(title.format("\n\tPython BattleShip\t\n"))

# The playerBoardShoot will also serve as the Bot's board
print("ShootBoard")
playerBoardShoot = Board()
playerBoardShoot.createBoard()
playerBoardShoot.printBoard()


print("\nPlayerBoard")
playerBoardVisual = Board()
playerBoardVisual.createBoard()
playerBoardVisual.printBoard()

time.sleep(5)
print("\n\n\n\n\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

print(white.format("\n\n\n\tShip Placement"))
print("Ship Types:")
print(green.format("5 Slot - Green Ship"))
print(yellow.format("4 Slot - Blue Ship"))
print(magenta.format("3 Slot - Magenta Ship \n"))

playerBoardShoot.placeBotsShips()

print("\nPlayerBoard")
playerBoardVisual.printBoard()
playerBoardVisual.placePlayerShips()
print("\n\nFinal PlayerBoard")
playerBoardVisual.printBoard()

print(white.format("\nCoin Flip!\n"))

time.sleep(5)

coinFlip = random.randint(0,1)

if coinFlip == 0:
	print("Bot Goes First!")

	print("\nShootBoard")
	playerBoardShoot.printBoard()

	print("\nPlayerBoard")
	playerBoardVisual.printBoard()

	time.sleep(3)
	print("\n\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")

	playerBoardVisual.botShoots() 	# Bot Shooting

	print(gray.format("\nShootBoard"))
	playerBoardShoot.printBoard()

	print(gray.format("\nPlayerBoard"))
	playerBoardVisual.printBoard()

	time.sleep(5)
	playerBoardVisual.stopBlinkingEverything()


elif coinFlip == 1:
	print("Player Goes First!")
	print("Enter Cordinates Ex: B2 or C5\n")



gameEnd = False
while not gameEnd:

	print(gray.format("\n\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n"))

	print(gray.format("\nShootBoard"))
	playerBoardShoot.printBoard()

	print(gray.format("\nPlayerBoard"))
	playerBoardVisual.printBoard()

	playerBoardShoot.playerShoots() 	# Player Shooting

	print(gray.format("\nShootBoard"))
	playerBoardShoot.printBoard()
	
	print(gray.format("\nPlayerBoard"))
	playerBoardVisual.printBoard()



	if len(playerBoardShoot.bots5SlottedShip) == 0 and len(playerBoardShoot.bots4SlottedShip) == 0 and len(playerBoardShoot.bots3SlottedShip) == 0:
		print(title.format("\n\n\nPlayer Destoryed All 3 Of The Bot's Ships!"))
		print(title.format("Player Wins!"))

		clearEverything = "\033[00m"
		print(clearEverything.format(" "))

		gameEnd = True
		break
	
	time.sleep(5)
	playerBoardShoot.stopBlinkingEverything()

	playerBoardVisual.botShoots() 	# Bot Shooting

	print(gray.format("\nShootBoard"))
	playerBoardShoot.printBoard()

	print(gray.format("\nPlayerBoard"))
	playerBoardVisual.printBoard()

	time.sleep(5)
	playerBoardVisual.stopBlinkingEverything()

	if len(playerBoardVisual.players5SlottedShip) == 0 and len(playerBoardVisual.players4SlottedShip) == 0 and len(playerBoardVisual.players3SlottedShip) == 0:
		
		print(gray.format("\n\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n"))

		print(gray.format("\nShootBoard"))
		playerBoardShoot.printBoard()
	
		print(gray.format("\nPlayerBoard"))
		playerBoardVisual.printBoard()

		print(title.format("\n\n\nBot Has Destoryed All 3 Of The Player's Ships!"))
		print(title.format("Bot Wins!"))

		clearEverything = "\033[00m"
		print(clearEverything.format(" "))
		gameEnd = True
		
		break









