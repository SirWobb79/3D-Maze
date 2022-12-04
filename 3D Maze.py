import os

# Getting the assets ready
screen = [["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","■","□","□","□","□",],
		  ["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","■","□","□","□","□",],
		  ["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","■","□","□","□","□",],
		  ["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","■","□","□","□","□",],
		  ["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","■","□","□","□","□",],
		  ["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","■","□","□","□","□",],
		  ["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","■","□","□","□","□",],
		  ["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","■","□","□","□","□",],
		  ["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","■","□","□","□","□",],
		  ["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","■","□","□","□","□",],
		  ["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","■","□","□","□","□",],
		  ]

def player_pos(y,x):
	player = map[y][x]

map = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
	   [1,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1],
	   [1,0,1,1,0,1,1,0,1,0,1,1,1,0,1,1,0,1],
	   [1,0,0,1,0,1,0,0,1,0,0,0,1,0,0,1,0,1],
	   [1,1,1,1,0,1,1,1,1,0,1,0,1,1,1,1,0,1],
	   [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1],
	   [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,]]

rot = 0
px = 1
py = 3
player_pos(py, px)
count = 25

# The most important part of this
def pixel1(y,x):
	screen[y][x] = "■"
	
def pixel0(y,x):
	screen[y][x] = "□"

# Number system
num = 99
if num < 10:
	str_num = [str(num)[-1],"0"]
else:
	str_num = [str(num)[-1],str(num)[-2]]
	
# Over 500 lines of functions
def digit1():
	if str_num[0] == "0":
		pixel1(10,18)
		pixel1(9,19)
		pixel1(7,19)
		pixel1(6,18)
		pixel1(7,17)
		pixel1(9,17)
	elif str_num[0] == "1":
		pixel1(7,19)
		pixel1(9,19)
	elif str_num[0] == "2":
		pixel1(10,18)
		pixel1(9,17)
		pixel1(8,18)
		pixel1(7,19)
		pixel1(6,18)
	elif str_num[0] == "3":
		pixel1(10,18)
		pixel1(9,19)
		pixel1(7,19)
		pixel1(6,18)
		pixel1(8,18)
	elif str_num[0] == "4":
		pixel1(9,19)
		pixel1(7,19)
		pixel1(7,17)
		pixel1(8,18)
	elif str_num[0] == "5":
		pixel1(10,18)
		pixel1(9,19)
		pixel1(6,18)
		pixel1(7,17)
		pixel1(8,18)
	elif str_num[0] == "6":
		pixel1(10,18)
		pixel1(9,19)
		pixel1(6,18)
		pixel1(7,17)
		pixel1(9,17)
		pixel1(8,18)
	elif str_num[0] == "7":
		pixel1(9,19)
		pixel1(7,19)
		pixel1(6,18)
	elif str_num[0] == "8":
		pixel1(10,18)
		pixel1(9,19)
		pixel1(7,19)
		pixel1(6,18)
		pixel1(7,17)
		pixel1(9,17)
		pixel1(8,18)
	elif str_num[0] == "9":
		pixel1(10,18)
		pixel1(9,19)
		pixel1(7,19)
		pixel1(6,18)
		pixel1(7,17)
		pixel1(8,18)
		
def digit2():
	if str_num[1] == "0":
		pixel1(4,18)
		pixel1(3,19)
		pixel1(1,19)
		pixel1(0,18)
		pixel1(1,17)
		pixel1(3,17)
	elif str_num[1] == "1":
		pixel1(3,19)
		pixel1(1,19)
	elif str_num[1] == "2":
		pixel1(4,18)
		pixel1(3,17)
		pixel1(2,18)
		pixel1(1,19)
		pixel1(0,18)
	elif str_num[1] == "3":
		pixel1(4,18)
		pixel1(3,19)
		pixel1(1,19)
		pixel1(0,18)
		pixel1(2,18)
	elif str_num[1] == "4":
		pixel1(3,19)
		pixel1(1,19)
		pixel1(1,17)
		pixel1(2,18)
	elif str_num[1] == "5":
		pixel1(4,18)
		pixel1(3,19)
		pixel1(0,18)
		pixel1(1,17)
		pixel1(2,18)
	elif str_num[1] == "6":
		pixel1(4,18)
		pixel1(3,19)
		pixel1(0,18)
		pixel1(1,17)
		pixel1(3,17)
		pixel1(2,18)
	elif str_num[1] == "7":
		pixel1(3,19)
		pixel1(1,19)
		pixel1(0,18)
	elif str_num[1] == "8":
		pixel1(4,18)
		pixel1(3,19)
		pixel1(1,19)
		pixel1(0,18)
		pixel1(1,17)
		pixel1(3,17)
		pixel1(2,18)
	elif str_num[1] == "9":
		pixel1(4,18)
		pixel1(3,19)
		pixel1(1,19)
		pixel1(0,18)
		pixel1(1,17)
		pixel1(2,18)

def l_wall(y,x):
	if rot == 0:
		if map[y][x-1] == 1 and map[y-1][x] == 1:
			pixel1(0,0)
			pixel1(1,1)
			pixel1(2,2)
			pixel1(3,3)
			pixel1(4,3)
			pixel1(5,3)
			pixel1(6,3)
			pixel1(7,3)
			pixel1(8,2)
			pixel1(9,1)
			pixel1(10,0)
		elif map[y][x-1] == 1 and map[y-1][x] == 0:
			pixel1(0,0)
			pixel1(1,1)
			pixel1(2,2)
			pixel1(3,3)
			pixel1(7,3)
			pixel1(8,2)
			pixel1(9,1)
			pixel1(10,0)
		elif map[y][x-1] == 0 and map[y-1][x] == 1:
			pixel1(3,0)
			pixel1(3,1)
			pixel1(3,2)
			pixel1(3,3)
			pixel1(7,3)
			pixel1(7,2)
			pixel1(7,1)
			pixel1(7,0)
		elif map[y][x-1] == 0 and map[y-1][x] == 0:
			pixel1(3,0)
			pixel1(3,1)
			pixel1(3,2)
			pixel1(3,3)
			pixel1(7,3)
			pixel1(7,2)
			pixel1(7,1)
			pixel1(7,0)
	elif rot == 1:
		if map[y-1][x] == 1 and map[y][x+1] == 1:
			pixel1(0,0)
			pixel1(1,1)
			pixel1(2,2)
			pixel1(3,3)
			pixel1(4,3)
			pixel1(5,3)
			pixel1(6,3)
			pixel1(7,3)
			pixel1(8,2)
			pixel1(9,1)
			pixel1(10,0)
		elif map[y-1][x] == 1 and map[y][x+1] == 0:
			pixel1(0,0)
			pixel1(1,1)
			pixel1(2,2)
			pixel1(3,3)
			pixel1(7,3)
			pixel1(8,2)
			pixel1(9,1)
			pixel1(10,0)
		elif map[y-1][x] == 0 and map[y][x+1] == 1:
			pixel1(3,0)
			pixel1(3,1)
			pixel1(3,2)
			pixel1(3,3)
			pixel1(7,3)
			pixel1(7,2)
			pixel1(7,1)
			pixel1(7,0)
		elif map[y-1][x] == 0 and map[y][x+1] == 0:
			pixel1(3,0)
			pixel1(3,1)
			pixel1(3,2)
			pixel1(3,3)
			pixel1(7,3)
			pixel1(7,2)
			pixel1(7,1)
			pixel1(7,0)
	elif rot == 2:
		if map[y][x+1] == 1 and map[y+1][x] == 1:
			pixel1(0,0)
			pixel1(1,1)
			pixel1(2,2)
			pixel1(3,3)
			pixel1(4,3)
			pixel1(5,3)
			pixel1(6,3)
			pixel1(7,3)
			pixel1(8,2)
			pixel1(9,1)
			pixel1(10,0)
		elif map[y][x+1] == 1 and map[y+1][x] == 0:
			pixel1(0,0)
			pixel1(1,1)
			pixel1(2,2)
			pixel1(3,3)
			pixel1(7,3)
			pixel1(8,2)
			pixel1(9,1)
			pixel1(10,0)
		elif map[y][x+1] == 0 and map[y+1][x] == 1:
			pixel1(3,0)
			pixel1(3,1)
			pixel1(3,2)
			pixel1(3,3)
			pixel1(7,3)
			pixel1(7,2)
			pixel1(7,1)
			pixel1(7,0)
		elif map[y][x+1] == 0 and map[y+1][x] == 0:
			pixel1(3,0)
			pixel1(3,1)
			pixel1(3,2)
			pixel1(3,3)
			pixel1(7,3)
			pixel1(7,2)
			pixel1(7,1)
			pixel1(7,0)
	elif rot == 3:
		if map[y+1][x] == 1 and map[y][x-1] == 1:
			pixel1(0,0)
			pixel1(1,1)
			pixel1(2,2)
			pixel1(3,3)
			pixel1(4,3)
			pixel1(5,3)
			pixel1(6,3)
			pixel1(7,3)
			pixel1(8,2)
			pixel1(9,1)
			pixel1(10,0)
		elif map[y+1][x] == 1 and map[y][x-1] == 0:
			pixel1(0,0)
			pixel1(1,1)
			pixel1(2,2)
			pixel1(3,3)
			pixel1(7,3)
			pixel1(8,2)
			pixel1(9,1)
			pixel1(10,0)
		elif map[y+1][x] == 0 and map[y][x-1] == 1:
			pixel1(3,0)
			pixel1(3,1)
			pixel1(3,2)
			pixel1(3,3)
			pixel1(7,3)
			pixel1(7,2)
			pixel1(7,1)
			pixel1(7,0)
		elif map[y+1][x] == 0 and map[y][x-1] == 0:
			pixel1(3,0)
			pixel1(3,1)
			pixel1(3,2)
			pixel1(3,3)
			pixel1(7,3)
			pixel1(7,2)
			pixel1(7,1)
			pixel1(7,0)

def r_wall(y,x):
	if rot == 0:
		if map[y][x+1] == 1 and map[y-1][x] == 1:
			pixel1(0,14)
			pixel1(1,13)
			pixel1(2,12)
			pixel1(3,11)
			pixel1(4,11)
			pixel1(5,11)
			pixel1(6,11)
			pixel1(7,11)
			pixel1(8,12)
			pixel1(9,13)
			pixel1(10,14)
		elif map[y][x+1] == 1 and map[y-1][x] == 0:
			pixel1(0,14)
			pixel1(1,13)
			pixel1(2,12)
			pixel1(3,11)
			pixel1(7,11)
			pixel1(8,12)
			pixel1(9,13)
			pixel1(10,14)
		elif map[y][x+1] == 0 and map[y-1][x] == 1:
			pixel1(3,14)
			pixel1(3,13)
			pixel1(3,12)
			pixel1(3,11)
			pixel1(7,11)
			pixel1(7,12)
			pixel1(7,13)
			pixel1(7,14)
		elif map[y][x+1] == 0 and map[y-1][x] == 0:
			pixel1(3,14)
			pixel1(3,13)
			pixel1(3,12)
			pixel1(3,11)
			pixel1(7,11)
			pixel1(7,12)
			pixel1(7,13)
			pixel1(7,14)
	elif rot == 1:
		if map[y+1][x] == 1 and map[y][x+1] == 1:
			pixel1(0,14)
			pixel1(1,13)
			pixel1(2,12)
			pixel1(3,11)
			pixel1(4,11)
			pixel1(5,11)
			pixel1(6,11)
			pixel1(7,11)
			pixel1(8,12)
			pixel1(9,13)
			pixel1(10,14)
		elif map[y+1][x] == 1 and map[y][x+1] == 0:
			pixel1(0,14)
			pixel1(1,13)
			pixel1(2,12)
			pixel1(3,11)
			pixel1(7,11)
			pixel1(8,12)
			pixel1(9,13)
			pixel1(10,14)
		elif map[y+1][x] == 0 and map[y][x+1] == 1:
			pixel1(3,14)
			pixel1(3,13)
			pixel1(3,12)
			pixel1(3,11)
			pixel1(7,11)
			pixel1(7,12)
			pixel1(7,13)
			pixel1(7,14)
		elif map[y+1][x] == 0 and map[y][x+1] == 0:
			pixel1(3,14)
			pixel1(3,13)
			pixel1(3,12)
			pixel1(3,11)
			pixel1(7,11)
			pixel1(7,12)
			pixel1(7,13)
			pixel1(7,14)
	elif rot == 2:
		if map[y][x-1] == 1 and map[y+1][x] == 1:
			pixel1(0,14)
			pixel1(1,13)
			pixel1(2,12)
			pixel1(3,11)
			pixel1(4,11)
			pixel1(5,11)
			pixel1(6,11)
			pixel1(7,11)
			pixel1(8,12)
			pixel1(9,13)
			pixel1(10,14)
		elif map[y][x-1] == 1 and map[y+1][x] == 0:
			pixel1(0,14)
			pixel1(1,13)
			pixel1(2,12)
			pixel1(3,11)
			pixel1(7,11)
			pixel1(8,12)
			pixel1(9,13)
			pixel1(10,14)
		elif map[y][x-1] == 0 and map[y+1][x] == 1:
			pixel1(3,14)
			pixel1(3,13)
			pixel1(3,12)
			pixel1(3,11)
			pixel1(7,11)
			pixel1(7,12)
			pixel1(7,13)
			pixel1(7,14)
		elif map[y][x-1] == 0 and map[y+1][x] == 0:
			pixel1(3,14)
			pixel1(3,13)
			pixel1(3,12)
			pixel1(3,11)
			pixel1(7,11)
			pixel1(7,12)
			pixel1(7,13)
			pixel1(7,14)
	elif rot == 3:
		if map[y-1][x] == 1 and map[y][x-1] == 1:
			pixel1(0,14)
			pixel1(1,13)
			pixel1(2,12)
			pixel1(3,11)
			pixel1(4,11)
			pixel1(5,11)
			pixel1(6,11)
			pixel1(7,11)
			pixel1(8,12)
			pixel1(9,13)
			pixel1(10,14)
		elif map[y-1][x] == 1 and map[y][x-1] == 0:
			pixel1(0,14)
			pixel1(1,13)
			pixel1(2,12)
			pixel1(3,11)
			pixel1(7,11)
			pixel1(8,12)
			pixel1(9,13)
			pixel1(10,14)
		elif map[y-1][x] == 0 and map[y][x-1] == 1:
			pixel1(3,14)
			pixel1(3,13)
			pixel1(3,12)
			pixel1(3,11)
			pixel1(7,11)
			pixel1(7,12)
			pixel1(7,13)
			pixel1(7,14)
		elif map[y-1][x] == 0 and map[y][x-1] == 0:
			pixel1(3,14)
			pixel1(3,13)
			pixel1(3,12)
			pixel1(3,11)
			pixel1(7,11)
			pixel1(7,12)
			pixel1(7,13)
			pixel1(7,14)
			
def infront(y,x):
	if rot == 0:
		if map[y-1][x] == 0:
			pixel1(4,4)
			pixel1(6,4)
			pixel1(4,10)
			pixel1(6,10)
			pixel1(5,5)
			pixel1(5,6)
			pixel1(5,7)
			pixel1(5,8)
			pixel1(5,9)
		elif map[y-1][x] == 1:
			pixel1(3,4)
			pixel1(3,5)
			pixel1(3,6)
			pixel1(3,7)
			pixel1(3,8)
			pixel1(3,9)
			pixel1(3,10)
			pixel1(7,4)
			pixel1(7,5)
			pixel1(7,6)
			pixel1(7,7)
			pixel1(7,8)
			pixel1(7,9)
			pixel1(7,10)
	elif rot == 1:
		if map[y][x+1] == 0:
			pixel1(4,4)
			pixel1(6,4)
			pixel1(4,10)
			pixel1(6,10)
			pixel1(5,5)
			pixel1(5,6)
			pixel1(5,7)
			pixel1(5,8)
			pixel1(5,9)
		elif map[y][x+1] == 1:
			pixel1(3,4)
			pixel1(3,5)
			pixel1(3,6)
			pixel1(3,7)
			pixel1(3,8)
			pixel1(3,9)
			pixel1(3,10)
			pixel1(7,4)
			pixel1(7,5)
			pixel1(7,6)
			pixel1(7,7)
			pixel1(7,8)
			pixel1(7,9)
			pixel1(7,10)
	elif rot == 2:
		if map[y+1][x] == 0:
			pixel1(4,4)
			pixel1(6,4)
			pixel1(4,10)
			pixel1(6,10)
			pixel1(5,5)
			pixel1(5,6)
			pixel1(5,7)
			pixel1(5,8)
			pixel1(5,9)
		elif map[y+1][x] == 1:
			pixel1(3,4)
			pixel1(3,5)
			pixel1(3,6)
			pixel1(3,7)
			pixel1(3,8)
			pixel1(3,9)
			pixel1(3,10)
			pixel1(7,4)
			pixel1(7,5)
			pixel1(7,6)
			pixel1(7,7)
			pixel1(7,8)
			pixel1(7,9)
			pixel1(7,10)
	elif rot == 3:
		if map[y][x-1] == 0:
			pixel1(4,4)
			pixel1(6,4)
			pixel1(4,10)
			pixel1(6,10)
			pixel1(5,5)
			pixel1(5,6)
			pixel1(5,7)
			pixel1(5,8)
			pixel1(5,9)
		elif map[y][x-1] == 1:
			pixel1(3,4)
			pixel1(3,5)
			pixel1(3,6)
			pixel1(3,7)
			pixel1(3,8)
			pixel1(3,9)
			pixel1(3,10)
			pixel1(7,4)
			pixel1(7,5)
			pixel1(7,6)
			pixel1(7,7)
			pixel1(7,8)
			pixel1(7,9)
			pixel1(7,10)

def camera(y,x):
	l_wall(y,x)
	r_wall(y,x)
	infront(y,x)
	
def hud(y,x):
	if map[y][x] == 0:
		return "□"
	elif map[y][x] == 1:
		return "■"

# Main loop
use = True
while use:
	os.system("cls" if os.name == "nt" else "clear")
	
	player_pos(py,px)
	camera(py,px)
	
	digit1()
	digit2()
		
	for i in screen:
		print("".join(i))
	
	screen = [["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","■","□","□","□","□",],
		  	["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","■","□","□","□","□",],
		 	 ["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","■","□","□","□","□",],
		 	 ["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","■","□","□","□","□",],
			  ["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","■","□","□","□","□",],
		 	 ["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","■","□","□","□","□",],
		 	 ["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","■","□","□","□","□",],
		 	 ["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","■","□","□","□","□",],
		 	 ["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","■","□","□","□","□",],
			  ["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","■","□","□","□","□",],
			  ["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","■","□","□","□","□",],
		 	 ]
	
	# Compass (Rotation goes clockwise from 0 to 3)
	if rot == 0:
		print("Facing: N")
	elif rot == 1:
		print("Facing: E")
	elif rot == 2:
		print("Facing: S")
	elif rot == 3:
		print("Facing: W")
	
	# Movement
	move = input("Use WASD to move\n>")
	if move == "w":
		if rot == 0:
			if map[py-1][px] == 0:
				py -= 1
		elif rot == 1:
			if map[py][px+1] == 0:
				px += 1
		elif rot == 2:
			if map[py+1][px] == 0:
				py += 1
		elif rot == 3:
			if map[py][px-1] == 0:
				px -= 1
	elif move == "s":
		if rot == 0:
			if map[py+1][px] == 0:
				py += 1
		elif rot == 1:
			if map[py][px-1] == 0:
				px -= 1
		elif rot == 2:
			if map[py-1][px] == 0:
				py -= 1
		elif rot == 3:
			if map[py][px+1] == 0:
				px += 1
	elif move == "a":
		rot -= 1
		if rot < 0:
			rot = 3
	elif move == "d":
		rot += 1
		if rot > 3:
			rot = 0
			
	count -= 1
	if count < 1:
		count = 25
		num -= 1
	
	if num < 10:
		str_num = [str(num)[-1],"0"]
	else:
		str_num = [str(num)[-1],str(num)[-2]]
	
	# For not escaping in time
	if num == 0:
		os.system("cls" if os.name == "nt" else "clear")
		print("You failed to escape in time, you now must suffer the consenquences that await you...")
		break