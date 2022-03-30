# code for converting in csv
# importing panda library
# import pandas as pd
# readinag given csv file
# and creating dataframe
# dataframe1 = pd.read_csv("GeeksforGeeks.txt")
# storing this dataframe in a csv file
# dataframe1.to_csv('GeeksforGeeks.csv',
# 				index = None)

def _dec(method):
	def decs(ref):
		print("\n")
		print("="*60)
		method(ref)
		print("="*60)
		print("\n")
	return decs
	

"""%%%%%%%%%%%%%%%%%%%"""


def _opn(method):
	def op(ref):
		global f
		with open(new.name,"r") as f:
			method(ref)
	return op
	

"""%%%%%%%%%%%%%%%%%%%"""

	
def srch(self,new,ty):
		with open(self,"r") as r :
			l=r.read().split("\n")
		with open(self,"r+") as r :
			cont=0
			for line in l :
				line=line.replace("\'","").split(", ")
				if line[0]=="":
					continue
				if ty=="last name":
					if new==line[1]:
						cont+=1
				if ty =="roll":
					if new==line[2]:
						cont+=1
				if ty=="phone":
					if new==line[3]:
						cont+=1					
		return cont
	

"""%%%%%%%%%%%%%%%%%%%"""


def gen(l,name):
	for line in l :
		lin=line.replace("\'","").split(", ")
		if lin[0]=="":
			continue
		elif lin[0]==name :
			yield lin

"""%%%%%%%%%%%%%%%%%%%"""

	
class CrtNewFile():
	def __init__(self,name):
		self.name=name	
		with open(self.name,"a+"):
			print("================")
			print("File is opened")
			print("================")
		
		
	"""======================"""
	
	
	@_dec
	def addlist(self):
		print("Type close in any field to exit the adding function.\nElse the add function will go on forever.")
		while True :
			while True :
				try :
					name=input("Enter name :- ")
					if name == "close":
						return					
					if not name.isalpha():
						raise TypeError
					if name.isalpha():
						break
				except :
					print("Please enter a name not a number.")
			while True :
				try :
					last_name=input("Enter last name :- ")
					if last_name=="close":
						return
					if not last_name.isalpha():
						raise TypeError
					if last_name.isalpha():
						break
				except :
					print("Please enter a last name not a number.")
			while True:
				try:
					roll=int(input("Enter roll no. :- "))
					if roll == "close":
						return
					break
				except :
					print("Please enter a valid roll no.")
			while True :
				try :
					ph=input("Enter phn no. :-  ")
					if ph == "close":
						return
					try :
						m=int(ph)
					except :
						print("No. should be digits")
						break
					if len(ph)<10 or len(ph)>=11:
						raise TypeError
					elif len(ph)== 10:
						break
				except :
					print("Please enter a valid phone number.")
			lis=[name,last_name,roll,ph]
			list=str(lis)
			list=list.replace("[","").replace("]","").replace("\"","")
			print(list)
			with open(self.name,"a") as f:
				f.write(list+"\n")
			print("Record added..")
					
	
	"""======================"""
	
	
	@_dec
	def clearfile(self):
		with open(self.name,"r") as f :
			l=f.read()
			if len(l)==0:
				print("File is already empty.")
			else :
				In=input("Do you want to clear the file. \"Y\" for yes and \"N\" for no :-")
				if In =="Y":
					with open(self.name,"w") as f:
						f.write("")
					print("file is emptied")
				else :
					print("Clearing cancelled...")
					return
	

	"""======================"""
	
	
	@_dec
	@_opn
	def show(self):
		data=f.read()
		if len(data)==0:
			print("The file doesn't contain anything")
		else:
			print("The content of file is")
			print("----------------")
			print(data)
	
	
	"""======================"""
	
	
	@_dec
	@_opn
	def search(self):
		while 1:
			try:
				print('''From which criteria do you want to find
(1):-name
(2):-roll
(3):-last
(4):-phone
(5):-close''')
				type = input('=>')
				if type == 'close':
					return
				elif type.isnumeric():
					raise TypeError
				elif not type.isalpha():
					raise TypeError
				elif type in ['name','roll', 'phone' , 'last']:
					name=input(f"please enter the {type} of the student:-")
					break
			except:
				print('please enter the correct option') 
		count=0
		l=f.read().split("\n")
		count=0
		for line in l:
			line=line.replace("\'","").split(", ")
			if name in line:
				count+=1
				print(line)
		if count==0:
				print("No results found")
		else :
				print(f"There are {count} matching results")
				
						
	"""======================"""		
	
	@_dec
	@_opn
	def output(self):
		while True :
			name=input("Enter the name of the student:- ")
			l=f.read().split("\n")
			for line in l:
				line=line.replace("\'","").split(", ")
				if name==line[0]:
					print("Selected Record is added to the variable n")
					return line
				else :
					print("No record foumd for this name.")
					
					
	"""======================"""
	
	
	@_dec
	def edit(self):
		name=input("Enter the name :-").lower()
		while True :
			type=input("Enter the type of information you want to change.\n\"name\" for name \n\"last name\" for last name \n\"roll\" for roll no. and \n\"phone\" for phone no. :-").lower()
			types=["name","last name","roll","phone"]
			if type not in types :
				print("There is no type of field with this name.")
			else :
				break
		change=input("Enter new information :-").lower()
		with open(self.name,"r") as r :
			l=r.read().split("\n")
		with open(self.name,"r+") as r :
			count=0
			for line in l :
				line=line.replace("\'","").split(", ")
				if name==line[0]:
						count+=1
			if count==0:
				print("\n")
				print("="*60)
				print("No record found for this name")
				print("="*60)
				print("\n")
			else :
				for line in l :
					if count==1:
						line=line.replace("\'","").split(", ")
						if name==line[0]:
							if type.lower()=="name":
								line[0]=change
							elif type.lower()=="last name":
								line[1]=change
							elif type.lower()=="roll":
								line[2]=change
							elif type.lower()=="phone no":
								line[3]=change
							line=str(line)
							line=line.replace("[","").replace("]","").replace("\"","")
							print(line)
							r.write(line+"\n")
							print("\n")
							print("="*60)
							print(line)
							print("="*60)
							print ("\n")
						elif line[0]=="":
							r.write("")
						else:
							line=str(line)
							line=line.replace("[","").replace("]","").replace("\"","")
							r.write(line+"\n")
					elif count >1:
							print ("\n")
							print("="*60)
							print("There are more then one record with this name. \n What do you want to do now. \n \n ( i ):- Give more information of record. \n ( ii ):- Select from the record founded.")
							print("="*60)
							print("\n")
							inp=input("i for 1st option / ii for 2nd option :-")
							def cng(line,type,change):
								lis = ["name","last name","roll","phone"]
								for a in range(len(lis)):
									if type not in lis :
										return "There is no type of information in the record"
									if type==lis[a]:
										line[a]=change
										line=str(line)
										line=line.replace("[","").replace("]","").replace("\"","")
										print("\n")
										print("="*60)
										print(line)
										print("="*60)
										print("\n")
										r.write(line+"\n")
							if inp == "i":
								ty=input("Enter the type of new information :-")
								new=input("Enter the new information :-")
								cnt=srch(self.name,new,ty)
								if cnt == 0:
									print ("\n")
									print("="*60)
									print("No record found for this information.")
									print("="*60)
									print ("\n")
								elif cnt > 1:
									print ("\n")
									print("="*60)
									print("More then one record found agian,  terminated.")
									print("="*60)
									print ('\n')			
								elif cnt==1 :
									for line in l :
										line=line.replace("\'","").split(", ")
										if line[0]=="":
											continue
										if ty == "name":
											print ('\n')
											print("="*60)
											print("Can't search the records on the basis of name.")
											print("="*60)
											print ('\n')
										if ty == "last name":
											if line[1]==new :
												line=cng(line,type,change)
											elif line[0]=="":
												r.write("")
											else:
												line=str(line).replace("[","").replace("]","").replace("\"","")
												r.write(line+"\n")
										elif ty=="roll":
											if line[2]==new:
												line=cng(line,type,change)
											elif line[0]=="":
												r.write("")
											else:
												line=str(line)
												line=line.replace("[","").replace("]","").replace("\"","")
												r.write(line+"\n")
	
										elif ty == "phone":
											if line[3]==new :
												line=cng(line,type,change)
											elif line[0]=="":
												r.write("")
											else:
												line=str(line)
												line=line.replace("[","").replace("]","").replace("\"","")
												r.write(line+"\n")
							if inp=="ii":	
								gene=gen(l,name)
								n=1
								for a in gene :
									print(f"({n}):- {a}")
									n+=1
								inpt=int(input("Enter the record no."))
								m=1
								gene=gen(l,name)
								for b in gene :
									if m == inpt:
										#print(b)
										for line in l :
											line=line.replace("\'","").split(", ")
											if line == b :
												out=cng(b,type,change)
											elif line[0]=="":
												r.write("")
											else :
												line=str(line)
												line=line.replace("[","").replace("]","").replace("\"","")
												r.write(line+"\n")
										break
									m+=1
							break

					
	"""======================"""


	@_dec
	def dele(self):
		name=input("Enter the name:-")
		with open(self.name,"r") as f:
			lines=f.read().split("\n")
		with open(self.name,"w") as f :
			count=0
			for line in lines :
				line=line.replace("\'","").split(", ")
				if line[0]==name :
					count+=1
			if count==1:
				for line in lines :
					line=line.replace("\'","").split(", ")
					if line[0]==name :
						f.write("")
					elif line[0]=="":
						f.write("")
					else :
						line=str(line)
						line=line.replace("[","").replace("]","").replace("\"","")
						f.write(line +"\n")
				print("Record deleted.")
			elif count==0:
						print("No record found for this name")
			elif count >1:
					print("There are more then one records with this name.")
					inpt=input("Type (i) for deleting all records found with this name.\nType (ii) for selecting from the records for deleting :-")
					if inpt=="i":
						for line in lines :
							line=line.replace("\'","").split(", ")
							if line[0]==name :
								f.write("")
							elif line[0]=="":
								f.write("")
							else :
								line=str(line)
								line=line.replace("[","").replace("]","").replace("\"","")
								f.write(line)
						print("Records deleted.")
					elif inpt=="ii":
						gene=gen(lines,name)
						n=1
						for a in gene :
							print(f"({n}):-{a}")
							n+=1
						inp=int(input("Enter the record no you want to delete :- "))
						m=1
						gene=gen(lines,name)
						for b in gene :
							if m == inp:
								for line in lines :
									line=line.replace("\'","").split(", ")
									if line == b :
										f.write("")
									elif line[0]=="":
										f.write("")
									else :
										line=str(line)
										line=line.replace("[","").replace("]","").replace("\"","")
										f.write(line+"\n")
							m+=1
						print("Record deleted.")
					else :
						print ("Please enter \"i\" or \"ii\" only.")		
						

	"""======================"""
	
	
	@_dec
	@_opn				
	def count(self):
		line=f.readlines()
		count=0
		for lines in line :
			count+=1
		print(f"There are {count} records.")
			
			
	"""======================"""

	@_dec
	@_opn
	def srt(self):
		print("On which basis do you want to sort the file")
		with open(self.name,"r") as f:
			lines=f.read().split("\n")
			new_lines = []
			for line in lines :
				line=line.replace("\'","").split(", ")
				new_lines.append(line)
			new_lines=new_lines[:-1]
		while 1:
			try:
				type = int(input("(1):-According to roll no.\n(2):-According to name\n(3):-For exiting this command\n=>"))
				if type != 1 and type != 2 and type != 3:
					raise TypeError
				elif type == 3:
					break
				elif type == 1:
					with open(self.name,"w") as f:
						f.write('')
					rolls = [a[2] for a in new_lines]
					rolls.sort()
					res = [a for i in rolls for a in new_lines if a[2]==i]
					for a in res :
						list=str(a)
						list=list.replace("[","").replace("]","").replace("\"","")
						print(list)
						with open(self.name,"a") as f:
							f.write(list+"\n")
					print("Records Sorted...")
					break
				elif type == 2:
					with open(self.name,"w") as f:
						f.write('')
					names = [a[0] for a in new_lines]
					names.sort()
					print(names)
					res = [a for i in names for a in new_lines if a[0]==i]
					print(res)
					for a in res:
						list=str(a)
						list=list.replace("[","").replace("]","").replace("\"","")
						print(list)
						with open(self.name,"a") as f:
							f.write(list+"\n")
							
					print("Records Sorted...")
					break
			except:
				print("Please select from the given options")
			


		

	"""======================"""


def run():
	while True:
		print("""(1):-Enter the name of the file in which you want to work.
(2):-The file should be of txt format.
(3):-If the file is in diffrent folder.Then give the full
     path of file.""")
		name=input("File Name :- ")
		if name.count(".")==1:
			x=name.split(".")
			if x[1]=="txt":
				global new
				new=CrtNewFile(name)
				break
			else :
				print("\n")
				print("="*60)
				print("Enter the correct extension")
				print("="*60)
				print("\n")
		else:
			print("\n")
			print("="*60)
			print("Please enter the correct file name")
			print("="*60)
			print("\n")
run()
while True:
	print("""(1):-To add a list type \"add"
(2):-To view the content of the file typr \"view"
(3):-To clear the content of the file type \"clear"
(4):-For checking a record in the file type \"search"
(5):-For sorting the document \"sort\"
(6):-For taking a record in a variable type \"output"
(7):-For editing a record in the file type \"edit\"
(8):-For deleting a specific record from the file type \"del\"
(9):-For viewing no. of total records type \"count"
(10):-For opening another file type \"open"
(11):-For closing the program type \"close" """)
	function=input("Enter the command :- ")
	if function == "close":
		print("="*60)
		print("="*60)
		print("Program is closed. Thank you for using.")
		print("="*60)
		print("="*60)
		break
	elif function == "add":
		new.addlist()
	elif function == "view":
		new.show()
	elif function == "clear":
		new.clearfile()
	elif function == "search":
		new.search()
	elif function == "sort":
		new.srt()
	elif function == "output":
		n=new.output()
	elif function == "edit":
		new.edit()
	elif function == "del":
		new.dele()
	elif function == "count":
		new.count()
	elif function == "open":
		print("="*60)
		run()
	else :
		print("\n")
		print("="*60)
		print("There is no function defined for this keyword")
		print("="*60)
		print("\n")
	print("#~"*30)