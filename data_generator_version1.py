import sys
import random
import os
import csv_writer_module
import json_writer_module

def main():
	#read files
	female_done = open('female.txt', 'r')
	male_done = open('male.txt', 'r')
	phone = open('phone.txt', 'r')
	street = open('address.txt', 'r')

	#write files
	data = open('data.txt', 'w')

	#class for user input exceptions
	class Error(Exception):
		"""Base class for other exceptions"""
		pass

	class ValueTooSmall(Error):
		"""Raised when the input value is too small"""
		pass

	class ValueTooLarge(Error):
		"""Raise when input value is too large"""
		pass

	#check if using arguments
	if len(sys.argv) == 2:
		num = int(sys.argv[1])

	#no arguments ask for number of data
	else:
		while True:
			try:
				answer = True
				num = input("Please enter a number between 1-1000: ")
				num = int(num)
				if(num > 1000):
					raise ValueTooLarge
			
				elif(num < 1):
					raise ValueTooSmall

				break
			except ValueError:
				print("Please enter a valid interger! Please try again...")
			except ValueTooSmall:
				print("Your number is too small, must be greater than 0! Please try again...")
			except ValueTooLarge:
				print("Your number is too large, must be less than 1001! Please try again...")

	#pull in data from files into separate lists
	female_list = []
	for x in female_done: #pull in data from files into separate lists
		female_list.append(x)

	male_list = [] #pull in data from files into separate lists
	for x in male_done:
		male_list.append(x)

	phone_list = [] #pull in data from files into separate lists
	for x in phone:
		phone_list.append(x)

	street_list = [] #pull in data from files into separate lists
	for x in street:
		street_list.append(x)

	male_first_names = []
	male_last_names = []
	female_first_names = []	
	female_last_names = []

	for x in male_list: #split the names into first and last
		ma = x.split(",")
		male_first_names.append(ma[1])
		male_last_names.append(ma[0])

	for x in female_list: #split the names into first and last
		ma = x.split(",")
		female_first_names.append(ma[1])
		female_last_names.append(ma[0])



	def checkName(first_name, last_name): #check if name is already in data.txt
		global name #make name global
		name = [] #reset name
		name.append(random.choice(first_name)) #randomize first name
		name.append(random.choice(last_name))#randomize last name
		fp = open('data.txt', 'r') #open data.txt
		data = fp.readlines() #read data.txt
		if data != '': #check if data.txt is empty
		#if os.path.getsize('data.txt') != 0: #check if data.txt is empty
			for x in data: #check if name is already in data.txt
				y = x.split(',')
				if(y[0].strip() == name[1].strip() and y[1].strip() == name[0].strip()):
					name = []
					checkName(first_name, last_name) #if name is already in data.txt, call function again
				else: #if name is not in data.txt,
					return
		else: #if data.txt is empty,
			return

	ext = ['@hotmail.com', '@gmail.com', '@yahoo.com', '@whatever.com'] #email extensions

	for x in range(0, num):
		rand_gender = random.randint(0,1) #this is for randomizing between male/females
		if rand_gender == 1:
			checkName(female_first_names, female_last_names)
			email = name[0].strip() + '.' + name[1].strip() + ext[random.randint(0,3)].strip()
			address = street_list[x].strip()
			ph_num = phone_list[x].strip()
			data.write(name[1].strip() + ',' + name[0].strip() + ',' + email + ',' + address + ',' + ph_num + '\n')
		elif rand_gender == 0:
			checkName(male_first_names, male_last_names)
			fullname = name[1] + ',' + name[0]
			email = name[0].strip() + '.' + name[1].strip() + ext[random.randint(0,3)].strip()
			address = street_list[x].strip()
			ph_num = phone_list[x].strip()
			data.write(name[1].strip() + ',' + name[0].strip() + ',' + email + ',' + address + ',' + ph_num + '\n')

	female_done.close()
	male_done.close()
	phone.close()
	street.close()
	data.close()
	print('Data collection finished!')
	#choose to print out in csv or json
	def printData():
		answer = input('Please choose 1 for csv or 2 for json output file: ')
		if(answer == '1'):
			csv_writer_module.csv_run()
			print('Please find your data in "data.csv" in the cwd!!!')
					
		elif(answer == '2'):
			json_writer_module.json_run()
			print('Please find your data in "data.json" in the cwd!!!')
		else:
			printData()

	printData()

	print("printing all finished!!!")

if __name__== "__main__":
	main()





