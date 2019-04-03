import discord
from discord import client
from discord.ext import commands
import sys
import os
import time
import json

# Code Written by Fire: @InValidFire
prefix='.'
description = '''A moderation bot built by Fire'''
#initializes the global time variables
a1 = 0
a2 = 0
a3 = 0
a4 = 0
a5 = 0
a6 = 0
a7 = 0
a8 = 0
a9 = 0
a10 = 0
a11 = 0
a12 = 0
a13 = 0
a14 = 0
a15 = 0
a16 = 0
a17 = 0
a18 = 0
a19 = 0
a20 = 0
a21 = 0
a22 = 0
a23 = 0
a24 = 0
a25 = 0
a26 = 0
a27 = 0
a28 = 0
a29 = 0
a30 = 0
a31 = 0
a32 = 0
a33 = 0
a34 = 0
a35 = 0
a36 = 0
a37 = 0
a38 = 0
a39 = 0
a40 = 0
a41 = 0
a42 = 0
a43 = 0
a44 = 0
a45 = 0
a46 = 0
a47 = 0
a48 = 0
print("Global time vars initialized")
#initializes the server time variables
b1 = 0
b2 = 0
b3 = 0
b4 = 0
b5 = 0
b6 = 0
b7 = 0
b8 = 0
b9 = 0
b10 = 0
b11 = 0
b12 = 0
b13 = 0
b14 = 0
b15 = 0
b16 = 0
b17 = 0
b18 = 0
b19 = 0
b20 = 0
b21 = 0
b22 = 0
b23 = 0
b24 = 0
b25 = 0
b26 = 0
b27 = 0
b28 = 0
b29 = 0
b30 = 0
b31 = 0
b32 = 0
b33 = 0
b34 = 0
b35 = 0
b36 = 0
b37 = 0
b38 = 0
b39 = 0
b40 = 0
b41 = 0
b42 = 0
b43 = 0
b44 = 0
b45 = 0
b46 = 0
b47 = 0
b48 = 0
print("Server time variables initialized")
# initializes player time variables
c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
c6 = 0
c7 = 0
c8 = 0
c9 = 0
c10 = 0
c11 = 0
c12 = 0
c13 = 0
c14 = 0
c15 = 0
c16 = 0
c17 = 0
c18 = 0
c19 = 0
c20 = 0
c21 = 0
c22 = 0
c23 = 0
c24 = 0
c25 = 0
c26 = 0
c27 = 0
c28 = 0
c29 = 0
c30 = 0
c31 = 0
c32 = 0
c33 = 0
c34 = 0
c35 = 0
c36 = 0
c37 = 0
c38 = 0
c39 = 0
c40 = 0
c41 = 0
c42 = 0
c43 = 0
c44 = 0
c45 = 0
c46 = 0
c47 = 0
c48 = 0
print("Player time variables initialized")
activeserver = "null"
sysdate = "null" # used to handle loading of global data, and keeping track of
serverdate = "null" # used to handle loading of server data
systime = "null" #use this variable to make a clock for the bot to keep time with

def setup(method):
	global sysdate
	global activeserver
	newtimevars = {}
	newtimevars['times'] = []
	newtimevars['times'].append({
	'sysdate': sysdate,
	'00:00': 0,
	'00:30': 0,
	'01:00': 0,
	'01:30': 0,
	'02:00': 0,
	'02:30': 0,
	'03:00': 0,
	'03:30': 0,
	'04:00': 0,
	'04:30': 0,
	'05:00': 0,
	'05:30': 0,
	'06:00': 0,
	'06:30': 0,
	'07:00': 0,
	'07:30': 0,
	'08:00': 0,
	'08:30': 0,
	'09:00': 0,
	'09:30': 0,
	'10:00': 0,
	'10:30': 0,
	'11:00': 0,
	'11:30': 0,
	'12:00': 0,
	'12:30': 0,
	'13:00': 0,
	'13:30': 0,
	'14:00': 0,
	'14:30': 0,
	'15:00': 0,
	'15:30': 0,
	'16:00': 0,
	'16:30': 0,
	'17:00': 0,
	'17:30': 0,
	'18:00': 0,
	'18:30': 0,
	'19:00': 0,
	'19:30': 0,
	'20:00': 0,
	'20:30': 0,
	'21:00': 0,
	'21:30': 0,
	'22:00': 0,
	'22:30': 0,
	'23:00': 0,
	'23:30': 0
	})
	home = os.getcwd()
	if method == "server":
		os.makedirs(os.getcwd()+"/Data/Servers/"+activeserver+"/Temp")
		os.makedirs(os.getcwd()+"/Data/Servers/"+activeserver+"/"+sysdate)
		os.chdir(os.getcwd()+"/Data/Servers/"+activeserver+"/Data/Global")
	if method == "global":
		os.makedirs(os.getcwd()+"/Temp")
		os.makedirs(os.getcwd()+"/Globals")
		os.chdir(os.getcwd()+"/Temp")
	with open("timevars.json","w+") as file:
		json.dump(newtimevars,file)
	os.chdir(home)
#func responsible for reseting the time vars, may use multiple places
def globaltimereset():
	global a1
	global a2
	global a3
	global a4
	global a5
	global a6
	global a7
	global a8
	global a9
	global a10
	global a11
	global a12
	global a13
	global a14
	global a15
	global a16
	global a17
	global a18
	global a19
	global a20
	global a21
	global a22
	global a23
	global a24
	global a25
	global a26
	global a27
	global a28
	global a29
	global a30
	global a31
	global a32
	global a33
	global a34
	global a35
	global a36
	global a37
	global a38
	global a39
	global a40
	global a41
	global a42
	global a43
	global a44
	global a45
	global a46
	global a47
	global a48
	a1 = 0
	a2 = 0
	a3 = 0
	a4 = 0
	a5 = 0
	a6 = 0
	a7 = 0
	a8 = 0
	a9 = 0
	a10 = 0
	a11 = 0
	a12 = 0
	a13 = 0
	a14 = 0
	a15 = 0
	a16 = 0
	a17 = 0
	a18 = 0
	a19 = 0
	a20 = 0
	a21 = 0
	a22 = 0
	a23 = 0
	a24 = 0
	a25 = 0
	a26 = 0
	a27 = 0
	a28 = 0
	a29 = 0
	a30 = 0
	a31 = 0
	a32 = 0
	a33 = 0
	a34 = 0
	a35 = 0
	a36 = 0
	a37 = 0
	a38 = 0
	a39 = 0
	a40 = 0
	a41 = 0
	a42 = 0
	a43 = 0
	a44 = 0
	a45 = 0
	a46 = 0
	a47 = 0
	a48 = 0
	print("Global time vars reset")
def servertimereset():
	global b1
	global b2
	global b3
	global b4
	global b5
	global b6
	global b7
	global b8
	global b9
	global b10
	global b11
	global b12
	global b13
	global b14
	global b15
	global b16
	global b17
	global b18
	global b19
	global b20
	global b21
	global b22
	global b23
	global b24
	global b25
	global b26
	global b27
	global b28
	global b29
	global b30
	global b31
	global b32
	global b33
	global b34
	global b35
	global b36
	global b37
	global b38
	global b39
	global b40
	global b41
	global b42
	global b43
	global b44
	global b45
	global b46
	global b47
	global b48
	b1 = 0
	b2 = 0
	b3 = 0
	b4 = 0
	b5 = 0
	b6 = 0
	b7 = 0
	b8 = 0
	b9 = 0
	b10 = 0
	b11 = 0
	b12 = 0
	b13 = 0
	b14 = 0
	b15 = 0
	b16 = 0
	b17 = 0
	b18 = 0
	b19 = 0
	b20 = 0
	b21 = 0
	b22 = 0
	b23 = 0
	b24 = 0
	b25 = 0
	b26 = 0
	b27 = 0
	b28 = 0
	b29 = 0
	b30 = 0
	b31 = 0
	b32 = 0
	b33 = 0
	b34 = 0
	b35 = 0
	b36 = 0
	b37 = 0
	b38 = 0
	b39 = 0
	b40 = 0
	b41 = 0
	b42 = 0
	b43 = 0
	b44 = 0
	b45 = 0
	b46 = 0
	b47 = 0
	b48 = 0
	print("Server time vars reset")
# Nessessary bot stuff
bot = commands.Bot(command_prefix='.', description=description)
token = os.environ.get('DISCORDBOTTOKEN') #grabs the Discord Bot Token from a set environmental variable to keep it safe. c:

#Loads data if the date of previous data matches today
with open(os.getcwd()+"/Data/Temp/timevars.json") as globalvarload:
	globaltimes = json.load(globalvarload)
	for i in globaltimes['times']:
		try:
			sysdate = i['sysdate']
			print("Date loaded successfully")
		except:
			print("Couldn't load date successfully")

if sysdate == time.strftime("%m-%d-%Y"):
	for i in globaltimes['times']:
		a1 = int(i['00:00'])
		a2 = int(i['00:30'])
		a3 = int(i['01:00'])
		a4 = int(i['01:30'])
		a5 = int(i['02:00'])
		a6 = int(i['02:30'])
		a7 = int(i['03:00'])
		a8 = int(i['03:30'])
		a9 = int(i['04:00'])
		a10 = int(i['04:30'])
		a11 = int(i['05:00'])
		a12 = int(i['05:30'])
		a13 = int(i['06:00'])
		a14 = int(i['06:30'])
		a15 = int(i['07:00'])
		a16 = int(i['07:30'])
		a17 = int(i['08:00'])
		a18 = int(i['08:30'])
		a19 = int(i['09:00'])
		a20 = int(i['09:30'])
		a21 = int(i['10:00'])
		a22 = int(i['10:30'])
		a23 = int(i['11:00'])
		a24 = int(i['11:30'])
		a25 = int(i['12:00'])
		a26 = int(i['12:30'])
		a27 = int(i['13:00'])
		a28 = int(i['13:30'])
		a29 = int(i['14:00'])
		a30 = int(i['14:30'])
		a31 = int(i['15:00'])
		a32 = int(i['15:30'])
		a33 = int(i['16:00'])
		a35 = int(i['17:00'])
		a34 = int(i['16:30'])
		a36 = int(i['17:30'])
		a37 = int(i['18:00'])
		a38 = int(i['18:30'])
		a39 = int(i['19:00'])
		a40 = int(i['19:30'])
		a41 = int(i['20:00'])
		a42 = int(i['20:30'])
		a43 = int(i['21:00'])
		a44 = int(i['21:30'])
		a45 = int(i['22:00'])
		a46 = int(i['22:30'])
		a47 = int(i['23:00'])
		a48 = int(i['23:30'])
		print("Dates matched, loaded data successfully")

if sysdate != time.strftime("%m-%d-%Y"):
	sysdate = time.strftime("%m-%d-%Y")
	print("Dates did not match, did not load data, updated date variable")

# Initializes the bot, signifying ready
@bot.event
async def on_ready():
	print("----------")
	print("Bot Ready")
	print("Prefix: "+prefix)
	print("Name: "+str(bot.user))
	print("Connected Servers:")
	for server in bot.servers:
		print("\t"+server.name+"-"+server.id)
	print("-----Debug-----")
	print("Current time: "+time.strftime("%m/%d/%Y-%H:%M")) #current system time
	print("Directory: "+os.getcwd()) #current working directory
	print("----------")

@bot.event
async def on_message(message):
	# Pulls the needed global variables
	global sysdate
	global serverdate
	global activeserver
	global a1
	global a2
	global a3
	global a4
	global a5
	global a6
	global a7
	global a8
	global a9
	global a10
	global a11
	global a12
	global a13
	global a14
	global a15
	global a16
	global a17
	global a18
	global a19
	global a20
	global a21
	global a22
	global a23
	global a24
	global a25
	global a26
	global a27
	global a28
	global a29
	global a30
	global a31
	global a32
	global a33
	global a34
	global a35
	global a36
	global a37
	global a38
	global a39
	global a40
	global a41
	global a42
	global a43
	global a44
	global a45
	global a46
	global a47
	global a48
	global b1
	global b2
	global b3
	global b4
	global b5
	global b6
	global b7
	global b8
	global b9
	global b10
	global b11
	global b12
	global b13
	global b14
	global b15
	global b16
	global b17
	global b18
	global b19
	global b20
	global b21
	global b22
	global b23
	global b24
	global b25
	global b26
	global b27
	global b28
	global b29
	global b30
	global b31
	global b32
	global b33
	global b34
	global b35
	global b36
	global b37
	global b38
	global b39
	global b40
	global b41
	global b42
	global b43
	global b44
	global b45
	global b46
	global b47
	global b48

	activeserver = str(message.server.id)

	# if errors occur in loading data, run the setup for the server to generate nessessary files
	try:
		with open(os.getcwd()+"/Data/Servers/"+activeserver+"/Temp/timevars.json") as servervarload:
			servertimes = json.load(servervarload)
			for i in servertimes['times']:
				try:
					serverdate = i['sysdate']
					print("Server date loaded successfully")
				except:
					print("Couldn't load server date successfully")
	except:
		setup("server")
		with open(os.getcwd()+"/Data/Servers/"+activeserver+"/Temp/timevars.json") as servervarload:
			servertimes = json.load(servervarload)
			for i in servertimes['times']:
				try:
					serverdate = i['sysdate']
					print("Server date loaded successfully")
				except:
					print("Couldn't load server date")

	# loads data if serverdate (loaded above) matches current date
	if serverdate == time.strftime("%m-%d-%Y"):
		for i in servertimes['times']:
			b1 = int(i['00:00'])
			b2 = int(i['00:30'])
			b3 = int(i['01:00'])
			b4 = int(i['01:30'])
			b5 = int(i['02:00'])
			b6 = int(i['02:30'])
			b7 = int(i['03:00'])
			b8 = int(i['03:30'])
			b9 = int(i['04:00'])
			b10 = int(i['04:30'])
			b11 = int(i['05:00'])
			b12 = int(i['05:30'])
			b13 = int(i['06:00'])
			b14 = int(i['06:30'])
			b15 = int(i['07:00'])
			b16 = int(i['07:30'])
			b17 = int(i['08:00'])
			b18 = int(i['08:30'])
			b19 = int(i['09:00'])
			b20 = int(i['09:30'])
			b21 = int(i['10:00'])
			b22 = int(i['10:30'])
			b23 = int(i['11:00'])
			b24 = int(i['11:30'])
			b25 = int(i['12:00'])
			b26 = int(i['12:30'])
			b27 = int(i['13:00'])
			b28 = int(i['13:30'])
			b29 = int(i['14:00'])
			b30 = int(i['14:30'])
			b31 = int(i['15:00'])
			b32 = int(i['15:30'])
			b33 = int(i['16:00'])
			b34 = int(i['16:30'])
			b35 = int(i['17:00'])
			b36 = int(i['17:30'])
			b37 = int(i['18:00'])
			b38 = int(i['18:30'])
			b39 = int(i['19:00'])
			b40 = int(i['19:30'])
			b41 = int(i['20:00'])
			b42 = int(i['20:30'])
			b43 = int(i['21:00'])
			b44 = int(i['21:30'])
			b45 = int(i['22:00'])
			b46 = int(i['22:30'])
			b47 = int(i['23:00'])
			b48 = int(i['23:30'])
			print("Server dates matched, loaded server data successfully")

	if serverdate != time.strftime("%m-%d-%Y"):
		print("Server dates did not match, did not load data")

	# Here's where I need to input the player data loader. If a new server gets a message, it needs to first
	# set up the server directory before the player directory should be built - NOTE



	# Resets time variables if the saved timestamp does not match current date.
	# Allows it to pass midnight and keep variables accurate.
	# Also creates the required file structure for organizing data storage
	if sysdate != time.strftime("%m-%d-%Y"):
		globaltimereset()
		servertimereset()
		sysdate = time.strftime("%m-%d-%Y")
		os.makedirs(os.getcwd()+"/Data/Global/"+sysdate)
		os.makedirs(os.getcwd()+"/Data/Servers/"+activeserver+"/"+sysdate)
	if message.author == bot.user:
		return

	# Creates the time-block system, goes thirty minutes from the stated time
	# If a message is at 3:02, it will set atime to 3:00, as it was inside the 3:00 block
	if int(time.strftime("%M")) <= 29:
		atime = time.strftime("%H") + ":00"
	if int(time.strftime("%M")) >= 30:
		atime = time.strftime("%H") + ":30"

	# Controls changing and setting the global time variables depending on the atime variable (see above)
	if atime == "00:00":
		a1= a1+1
		print("Activity in block: " + atime + "[" + str(a1) + "] on server '"+message.server.name+"'")
	if atime == "00:30":
		a2 = a2+1
		print("Activity in block: " + atime + "[" + str(a2) + "] on server '"+message.server.name+"'")
	if atime == "01:00":
		a3 = a3+1
		print("Activity in block: " + atime + "[" + str(a3) + "] on server '"+message.server.name+"'")
	if atime == "01:30":
		a4 = a4+1
		print("Activity in block: " + atime + "[" + str(a4) + "] on server '"+message.server.name+"'")
	if atime == "02:00":
		a5 = a5+1
		print("Activity in block: " + atime + "[" + str(a5) + "] on server '"+message.server.name+"'")
	if atime == "02:30":
		a6 = a6+1
		print("Activity in block: " + atime + "[" + str(a6) + "] on server '"+message.server.name+"'")
	if atime == "03:00":
		a7 = a7+1
		print("Activity in block: " + atime + "[" + str(a7) + "] on server '"+message.server.name+"'")
	if atime == "03:30":
		a8 = a8+1
		print("Activity in block: " + atime + "[" + str(a8) + "] on server '"+message.server.name+"'")
	if atime == "04:00":
		a9 = a9+1
		print("Activity in block: " + atime + "[" + str(a9) + "] on server '"+message.server.name+"'")
	if atime == "04:30":
		a10 = a10+1
		print("Activity in block: " + atime + "[" + str(a10) + "] on server '"+message.server.name+"'")
	if atime == "05:00":
		a11 = a11+1
		print("Activity in block: " + atime + "[" + str(a11) + "] on server '"+message.server.name+"'")
	if atime == "05:30":
		a12 = a12+1
		print("Activity in block: " + atime + "[" + str(a12) + "] on server '"+message.server.name+"'")
	if atime == "06:00":
		a13 = a13+1
		print("Activity in block: " + atime + "[" + str(a13) + "] on server '"+message.server.name+"'")
	if atime == "06:30":
		a14 = a14+1
		print("Activity in block: " + atime + "[" + str(a14) + "] on server '"+message.server.name+"'")
	if atime == "07:00":
		a15 = a15+1
		print("Activity in block: " + atime + "[" + str(a15) + "] on server '"+message.server.name+"'")
	if atime == "07:30":
		a16 = a16+1
		print("Activity in block: " + atime + "[" + str(a16) + "] on server '"+message.server.name+"'")
	if atime == "08:00":
		a17 = a17+1
		print("Activity in block: " + atime + "[" + str(a17) + "] on server '"+message.server.name+"'")
	if atime == "08:30":
		a18 = a18+1
		print("Activity in block: " + atime + "[" + str(a18) + "] on server '"+message.server.name+"'")
	if atime == "09:00":
		a19 = a19+1
		print("Activity in block: " + atime + "[" + str(a19) + "] on server '"+message.server.name+"'")
	if atime == "09:30":
		a20 = a20+1
		print("Activity in block: " + atime + "[" + str(a20) + "] on server '"+message.server.name+"'")
	if atime == "10:00":
		a21 = a21+1
		print("Activity in block: " + atime + "[" + str(a21) + "] on server '"+message.server.name+"'")
	if atime == "10:30":
		a22 = a22+1
		print("Activity in block: " + atime + "[" + str(a22) + "] on server '"+message.server.name+"'")
	if atime == "11:00":
		a23 = a23+1
		print("Activity in block: " + atime + "[" + str(a23) + "] on server '"+message.server.name+"'")
	if atime == "11:30":
		a24 = a24+1
		print("Activity in block: " + atime + "[" + str(a24) + "] on server '"+message.server.name+"'")
	if atime == "12:00":
		a25 = a25+1
		print("Activity in block: " + atime + "[" + str(a25) + "] on server '"+message.server.name+"'")
	if atime == "12:30":
		a26 = a26+1
		print("Activity in block: " + atime + "[" + str(a26) + "] on server '"+message.server.name+"'")
	if atime == "13:00":
		a27 = a27+1
		print("Activity in block: " + atime + "[" + str(a27) + "] on server '"+message.server.name+"'")
	if atime == "13:30":
		a28 = a28+1
		print("Activity in block: " + atime + "[" + str(a28) + "] on server '"+message.server.name+"'")
	if atime == "14:00":
		a29 = a29+1
		print("Activity in block: " + atime + "[" + str(a29) + "] on server '"+message.server.name+"'")
	if atime == "14:30":
		a30 = a30+1
		print("Activity in block: " + atime + "[" + str(a30) + "] on server '"+message.server.name+"'")
	if atime == "15:00":
		a31 = a31+1
		print("Activity in block: " + atime + "[" + str(a31) + "] on server '"+message.server.name+"'")
	if atime == "15:30":
		a32 = a32+1
		print("Activity in block: " + atime + "[" + str(a32) + "] on server '"+message.server.name+"'")
	if atime == "16:00":
		a33 = a33+1
		print("Activity in block: " + atime + "[" + str(a33) + "] on server '"+message.server.name+"'")
	if atime == "16:30":
		a34 = a34+1
		print("Activity in block: " + atime + "[" + str(a34) + "] on server '"+message.server.name+"'")
	if atime == "17:00":
		a35 = a35+1
		print("Activity in block: " + atime + "[" + str(a35) + "] on server '"+message.server.name+"'")
	if atime == "17:30":
		a36 = a36+1
		print("Activity in block: " + atime + "[" + str(a36) + "] on server '"+message.server.name+"'")
	if atime == "18:00":
		a37 = a37+1
		print("Activity in block: " + atime + "[" + str(a37) + "] on server '"+message.server.name+"'")
	if atime == "18:30":
		a38 = a38+1
		print("Activity in block: " + atime + "[" + str(a38) + "] on server '"+message.server.name+"'")
	if atime == "19:00":
		a39 = a39+1
		print("Activity in block: " + atime + "[" + str(a39) + "] on server '"+message.server.name+"'")
	if atime == "19:30":
		a40 = a40+1
		print("Activity in block: " + atime + "[" + str(a40) + "] on server '"+message.server.name+"'")
	if atime == "20:00":
		a41 = a41+1
		print("Activity in block: " + atime + "[" + str(a41) + "] on server '"+message.server.name+"'")
	if atime == "20:30":
		a42 = a42+1
		print("Activity in block: " + atime + "[" + str(a42) + "] on server '"+message.server.name+"'")
	if atime == "21:00":
		a43 = a43+1
		print("Activity in block: " + atime + "[" + str(a43) + "] on server '"+message.server.name+"'")
	if atime == "21:30":
		a44 = a44+1
		print("Activity in block: " + atime + "[" + str(a44) + "] on server '"+message.server.name+"'")
	if atime == "22:00":
		a45 = a45+1
		print("Activity in block: " + atime + "[" + str(a45) + "] on server '"+message.server.name+"'")
	if atime == "22:30":
		a46 = a46+1
		print("Activity in block: " + atime + "[" + str(a46) + "] on server '"+message.server.name+"'")
	if atime == "23:00":
		a47 = a47+1
		print("Activity in block: " + atime + "[" + str(a47) + "] on server '"+message.server.name+"'")
	if atime == "23:30":
		a48 = a48+1
		print("Activity in block: " + atime + "[" + str(a48) + "] on server '"+message.server.name+"'")

	# Controls changing and setting the server time variables depending on the atime variable (see above)
	if atime == "00:00":
		b1= b1+1
		print("Activity in block: " + atime + "[" + str(b1) + "] on server '"+message.server.name+"'")
	if atime == "00:30":
		b2 = b2+1
		print("Activity in block: " + atime + "[" + str(b2) + "] on server '"+message.server.name+"'")
	if atime == "01:00":
		b3 = b3+1
		print("Activity in block: " + atime + "[" + str(b3) + "] on server '"+message.server.name+"'")
	if atime == "01:30":
		b4 = b4+1
		print("Activity in block: " + atime + "[" + str(b4) + "] on server '"+message.server.name+"'")
	if atime == "02:00":
		b5 = b5+1
		print("Activity in block: " + atime + "[" + str(b5) + "] on server '"+message.server.name+"'")
	if atime == "02:30":
		b6 = b6+1
		print("Activity in block: " + atime + "[" + str(b6) + "] on server '"+message.server.name+"'")
	if atime == "03:00":
		b7 = b7+1
		print("Activity in block: " + atime + "[" + str(b7) + "] on server '"+message.server.name+"'")
	if atime == "03:30":
		b8 = b8+1
		print("Activity in block: " + atime + "[" + str(b8) + "] on server '"+message.server.name+"'")
	if atime == "04:00":
		b9 = b9+1
		print("Activity in block: " + atime + "[" + str(b9) + "] on server '"+message.server.name+"'")
	if atime == "04:30":
		b10 = b10+1
		print("Activity in block: " + atime + "[" + str(b10) + "] on server '"+message.server.name+"'")
	if atime == "05:00":
		b11 = b11+1
		print("Activity in block: " + atime + "[" + str(b11) + "] on server '"+message.server.name+"'")
	if atime == "05:30":
		b12 = b12+1
		print("Activity in block: " + atime + "[" + str(b12) + "] on server '"+message.server.name+"'")
	if atime == "06:00":
		b13 = b13+1
		print("Activity in block: " + atime + "[" + str(b13) + "] on server '"+message.server.name+"'")
	if atime == "06:30":
		b14 = b14+1
		print("Activity in block: " + atime + "[" + str(b14) + "] on server '"+message.server.name+"'")
	if atime == "07:00":
		b15 = b15+1
		print("Activity in block: " + atime + "[" + str(b15) + "] on server '"+message.server.name+"'")
	if atime == "07:30":
		b16 = b16+1
		print("Activity in block: " + atime + "[" + str(b16) + "] on server '"+message.server.name+"'")
	if atime == "08:00":
		b17 = b17+1
		print("Activity in block: " + atime + "[" + str(b17) + "] on server '"+message.server.name+"'")
	if atime == "08:30":
		b18 = b18+1
		print("Activity in block: " + atime + "[" + str(b18) + "] on server '"+message.server.name+"'")
	if atime == "09:00":
		b19 = b19+1
		print("Activity in block: " + atime + "[" + str(b19) + "] on server '"+message.server.name+"'")
	if atime == "09:30":
		b20 = b20+1
		print("Activity in block: " + atime + "[" + str(b20) + "] on server '"+message.server.name+"'")
	if atime == "10:00":
		b21 = b21+1
		print("Activity in block: " + atime + "[" + str(b21) + "] on server '"+message.server.name+"'")
	if atime == "10:30":
		b22 = b22+1
		print("Activity in block: " + atime + "[" + str(b22) + "] on server '"+message.server.name+"'")
	if atime == "11:00":
		b23 = b23+1
		print("Activity in block: " + atime + "[" + str(b23) + "] on server '"+message.server.name+"'")
	if atime == "11:30":
		b24 = b24+1
		print("Activity in block: " + atime + "[" + str(b24) + "] on server '"+message.server.name+"'")
	if atime == "12:00":
		b25 = b25+1
		print("Activity in block: " + atime + "[" + str(b25) + "] on server '"+message.server.name+"'")
	if atime == "12:30":
		b26 = b26+1
		print("Activity in block: " + atime + "[" + str(b26) + "] on server '"+message.server.name+"'")
	if atime == "13:00":
		b27 = b27+1
		print("Activity in block: " + atime + "[" + str(b27) + "] on server '"+message.server.name+"'")
	if atime == "13:30":
		b28 = b28+1
		print("Activity in block: " + atime + "[" + str(b28) + "] on server '"+message.server.name+"'")
	if atime == "14:00":
		b29 = b29+1
		print("Activity in block: " + atime + "[" + str(b29) + "] on server '"+message.server.name+"'")
	if atime == "14:30":
		b30 = b30+1
		print("Activity in block: " + atime + "[" + str(b30) + "] on server '"+message.server.name+"'")
	if atime == "15:00":
		b31 = b31+1
		print("Activity in block: " + atime + "[" + str(b31) + "] on server '"+message.server.name+"'")
	if atime == "15:30":
		b32 = b32+1
		print("Activity in block: " + btime + "[" + str(b32) + "] on server '"+message.server.name+"'")
	if atime == "16:00":
		b33 = b33+1
		print("Activity in block: " + btime + "[" + str(b33) + "] on server '"+message.server.name+"'")
	if atime == "16:30":
		b34 = b34+1
		print("Activity in block: " + atime + "[" + str(b34) + "] on server '"+message.server.name+"'")
	if atime == "17:00":
		b35 = b35+1
		print("Activity in block: " + atime + "[" + str(b35) + "] on server '"+message.server.name+"'")
	if atime == "17:30":
		b36 = b36+1
		print("Activity in block: " + atime + "[" + str(b36) + "] on server '"+message.server.name+"'")
	if atime == "18:00":
		b37 = b37+1
		print("Activity in block: " + atime + "[" + str(b37) + "] on server '"+message.server.name+"'")
	if atime == "18:30":
		b38 = b38+1
		print("Activity in block: " + atime + "[" + str(b38) + "] on server '"+message.server.name+"'")
	if atime == "19:00":
		b39 = b39+1
		print("Activity in block: " + atime + "[" + str(b39) + "] on server '"+message.server.name+"'")
	if atime == "19:30":
		b40 = b40+1
		print("Activity in block: " + atime + "[" + str(b40) + "] on server '"+message.server.name+"'")
	if atime == "20:00":
		b41 = b41+1
		print("Activity in block: " + atime + "[" + str(b41) + "] on server '"+message.server.name+"'")
	if atime == "20:30":
		b42 = b42+1
		print("Activity in block: " + atime + "[" + str(b42) + "] on server '"+message.server.name+"'")
	if atime == "21:00":
		b43 = b43+1
		print("Activity in block: " + atime + "[" + str(b43) + "] on server '"+message.server.name+"'")
	if atime == "21:30":
		b44 = b44+1
		print("Activity in block: " + atime + "[" + str(b44) + "] on server '"+message.server.name+"'")
	if atime == "22:00":
		b45 = b45+1
		print("Activity in block: " + atime + "[" + str(b45) + "] on server '"+message.server.name+"'")
	if atime == "22:30":
		b46 = a46+1
		print("Activity in block: " + atime + "[" + str(b46) + "] on server '"+message.server.name+"'")
	if atime == "23:00":
		b47 = b47+1
		print("Activity in block: " + atime + "[" + str(b47) + "] on server '"+message.server.name+"'")
	if atime == "23:30":
		b48 = b48+1
		print("Activity in block: " + atime + "[" + str(b48) + "] on server '"+message.server.name+"'")

	#saves server time variables as JSON
	servertimes = {}
	servertimes['times'] = []
	servertimes['times'].append({
	'sysdate': sysdate,
	'00:00': str(b1),
	'00:30': str(b2),
	'01:00': str(b3),
	'01:30': str(b4),
	'02:00': str(b5),
	'02:30': str(b6),
	'03:00': str(b7),
	'03:30': str(b8),
	'04:00': str(b9),
	'04:30': str(b10),
	'05:00': str(b11),
	'05:30': str(b12),
	'06:00': str(b13),
	'06:30': str(b14),
	'07:00': str(b15),
	'07:30': str(b16),
	'08:00': str(b17),
	'08:30': str(b18),
	'09:00': str(b19),
	'09:30': str(b20),
	'10:00': str(b21),
	'10:30': str(b22),
	'11:00': str(b23),
	'11:30': str(b24),
	'12:00': str(b25),
	'12:30': str(b26),
	'13:00': str(b27),
	'13:30': str(b28),
	'14:00': str(b29),
	'14:30': str(b30),
	'15:00': str(b31),
	'15:30': str(b32),
	'16:00': str(b33),
	'16:30': str(b34),
	'17:00': str(b35),
	'17:30': str(b36),
	'18:00': str(b37),
	'18:30': str(b38),
	'19:00': str(b39),
	'19:30': str(b40),
	'20:00': str(b41),
	'20:30': str(b42),
	'21:00': str(b43),
	'21:30': str(b44),
	'22:00': str(b45),
	'22:30': str(b46),
	'23:00': str(b47),
	'23:30': str(b48)
	})

	#Saves server time variables to a temporary file loaded at message send
	with open(os.getcwd()+"/Data/Servers/"+activeserver+"/Temp/timevars.json","w+") as servervarfile:
		json.dump(servertimes, servervarfile, indent = "\t")
		print("Server Time vars saved as JSON")

	#Saves server time variables permanently to a timestamped file
	with open(os.getcwd()+"/Data/Servers/"+activeserver+"/"+sysdate+"/"+sysdate+"-"+str(message.server.name)+".json","w+") as servertimefile:
		json.dump(servertimes, servertimefile, indent = "\t")
		print("Server Daily log updated")

	#saves global time variables as JSON via a dictionary creation (i know it's weird)
	globaltimes = {} # this is the dictionary definition
	globaltimes['times'] = [] # these are creating 'words in the dictionary'
	globaltimes['times'].append({
	'sysdate': sysdate,
	'00:00': str(a1), # writes to the word, giving it a definition
	'00:30': str(a2),
	'01:00': str(a3),
	'01:30': str(a4),
	'02:00': str(a5),
	'02:30': str(a6),
	'03:00': str(a7),
	'03:30': str(a8),
	'04:00': str(a9),
	'04:30': str(a10),
	'05:00': str(a11),
	'05:30': str(a12),
	'06:00': str(a13),
	'06:30': str(a14),
	'07:00': str(a15),
	'07:30': str(a16),
	'08:00': str(a17),
	'08:30': str(a18),
	'09:00': str(a19),
	'09:30': str(a20),
	'10:00': str(a21),
	'10:30': str(a22),
	'11:00': str(a23),
	'11:30': str(a24),
	'12:00': str(a25),
	'12:30': str(a26),
	'13:00': str(a27),
	'13:30': str(a28),
	'14:00': str(a29),
	'14:30': str(a30),
	'15:00': str(a31),
	'15:30': str(a32),
	'16:00': str(a33),
	'16:30': str(a34),
	'17:00': str(a35),
	'17:30': str(a36),
	'18:00': str(a37),
	'18:30': str(a38),
	'19:00': str(a39),
	'19:30': str(a40),
	'20:00': str(a41),
	'20:30': str(a42),
	'21:00': str(a43),
	'21:30': str(a44),
	'22:00': str(a45),
	'22:30': str(a46),
	'23:00': str(a47),
	'23:30': str(a48)
	})

	#Saves global time variables to a temporary file loaded at boot
	with open(os.getcwd()+"/Data/Temp/timevars.json","w+") as globalvarfile:
		json.dump(globaltimes, globalvarfile, indent = "\t")
		print("Global Time vars saved as JSON")

	#Saves global time variables permanently to a timestamped file
	with open(os.getcwd()+"/Data/Global/"+sysdate+"/"+sysdate+"-global.json","w+") as globaltimefile:
		json.dump(globaltimes, globaltimefile, indent = "\t")
		print("Global Daily log updated")

# Runs the bot with our token key.
bot.run(token)
