"""
Computer Organization Project-1

In this project, we have to create a two-pass assembler for the 
12 bit accumulator architecture. I have chosen python as my 
language for doinng this project. Initially, Assembly code 
will be stored in assemblycode.txt. After the execution of the 
program machine code will be stored in machinecode.txt. It also produces
a VariableTable.txt and LabelTable.txt which contains all the variables and labels used in the assembly code respectively.

"""

''' 
Parameter Type: Opcode Dictionary, Line/Word to check
Return Type: String 
That is the opcode of the assembly opcode in that line.
'''
def opcodereturner(opcode,line):
	s=line.split(" ",1)
	if(s[0] in opcode.keys()):
		return opcode[s[0]]

'''
Parameter Type: Line, Opcode Dictionary
Return Type: Int
This function gives no. of opcodes in a line.
'''
def no_of_opcodes(line,opcode):
	l=line.split()
	count=0
	opcodekeyslist=opcode.keys()
	for i in l:
		if(i in opcodekeyslist):
			count+=1
	return count

'''
Parameter Type: Opcode Dictionary, Word(Maybe Opcode)
Return Type: Boolean 
Checks if the string is whether a instruction or not by 
checking in the opcode dictionary keys.
'''	
def checkifinstruction(opcode,op):
	if(op in opcode.keys()):
		return True
	else:
		return False

'''
Parameter Type: Error(bool), Opcode Dictionary, Symbols Dictionary
Return Type: Boolean,Dictionary,No of lines
This will read the assemblycode.txt file and will check if there is a
error. If there is a error than it will change error to True and 
Second Pass will not run. It also adds symbols to our dictionary called 
symbols and return that dictionary. And also returns a boolean value 
that will be True if it encountered a error.
'''
def pass1(error,opcode,symbols):
	file=open("assemblycode.txt","r")   		#Open the file
	file1=open("assemblycode.txt","r")			#Open the file for no. of lines
	lines=list(file1.readlines())
	length=len(lines)
	lc=0
	lineno=0
	while(True):
		flag=True
		line=file.readline()
		if not line:
			break;
		else:
			eof=line.find('/n')
			if(eof!=-1 and flag):
				line=line[:-1]
			lineno+=1
			comment=line.find('//')
			if(comment!=-1 and flag):
				line=line[:comment]				#Remove commented part
			if(line!='' and flag):
				brz=line.find('BRZ')
				brp=line.find('BRP')
				brn=line.find('BRN')
				inp=line.find('INP')
				sac=line.find('SAC')
				stp=line.find('STP')
				if(line.strip()=='STP' and flag):
					lc+=1
					break;
				if(no_of_opcodes(line,opcode)==0 and flag):
					error=True
					flag=False
					print(line)
					print("Error found on line number "+str(lineno)+": No Opcode found.")
				if(no_of_opcodes(line,opcode)>1 and flag):
					error=True
					flag=False
					print("Error found on line number "+str(lineno)+": More than one Opcode found.")
				l=line.split()
				if(len(l)==1 and l[0]!='CLA' and l[0]!='STP' and flag):
					error=True
					flag=False
					print("Error found on line number "+str(lineno)+": Insufficient no. of arguments.")
				if(len(l)==2 and checkifinstruction(opcode,l[0])==False and checkifinstruction(opcode,l[1])==True and l[1]!='CLA' and l[1]!='STP' and flag):
					error=True
					flag=False
					print("Error found on line number "+str(lineno)+": Formatting Error")
				for k in range(len(l)):
					q=False
					if(l[k] in opcode.keys()):
						q=True
					if(q==True):
						if(len(l)-k-1>=2):
							print("ERROR on Line "+str(lineno)+": More than one variable/label provided.")	#If more than required variables are provided
							error=True	
							flag=False
				if(len(l)>=3 and checkifinstruction(opcode,l[0])==False and checkifinstruction(opcode,l[1])==False and flag):
					error=True
					flag=False
					print("Error found on line number "+str(lineno)+": Formatting Error")
				colon=line.find(':')
				if(colon!=-1 and flag):
					head=line[:colon]
					head=head.strip()
					if(checkifinstruction(opcode,head)):
						error=True
						flag=False
						print("Error found on line number "+str(lineno)+": Label cannot be a opcode.")
					if(head in symbols and symbols[head]==-1 and flag):
						error=True
						flag=False
						print("Error found on line number "+str(lineno)+": Same symbol defined more than one time.")
					if(stp!=-1):
						symbols[head]=lc
						lc+=1
						continue
					symbols[head]=lc
				elif(brz!=-1 or brp!=-1 or brn!=-1 and flag):
					head=l[1]
					head=head.strip()
					if(checkifinstruction(opcode,head)):
						error=True
						flag=False
						print("Error found on line number "+str(lineno)+": Symbol cannot be a opcode.")
					if(head in symbols and flag):
						if(symbols[head]==-1):
							error=True
							flag=False
							print("Error found on line number "+str(lineno)+":"+head+" is a label type symbol.")
						else:
							lc+=1
							continue
					else:
						symbols[head]=-2
				elif(sac!=-1 or inp!=-1 and flag):
					head=l[1]
					head=head.strip()
					if(checkifinstruction(opcode,head)):
						error=True
						flag=False
						print("Error found on line number "+str(lineno)+": Symbol cannot be a opcode.")
					if(head in symbols and flag):
						if(symbols[head]==-1):
							error=True
							flag=False
							print("Error found on line number "+str(lineno)+":"+head+" is a label type symbol.")
					symbols[head]=-1
				lc+=1
	symbolkeys=symbols.keys()
	nvar=0
	for i in range(len(symbols)):
		if(symbols[symbolkeys[i]]==-2):
			print("Error: Label not defined "+symbolkeys[i])
			error=True
		elif(symbols[symbolkeys[i]]==-1):
			nvar+=1
			symbols[symbolkeys[i]]=lc
			lc+=1
	nlines=lc-nvar
	if(nlines+nvar>256):
		print("Error: Number of instructions has been exceeded than the limit-(0-255).")
	file.close()    
	file1.close()
	return error,symbols,nlines	

'''
Parameter Type: Opcode Dictionary, Symbols Dictionary, List , No of lines 
Return type: Void
This will run if their is no error in the assembly code. This will
add corresponding machine code to machinecode.txt, all the variables to VariableTable.txt and all the labels to to LabelTable.txt.
'''
def pass2(opcode,symbols,l1,l2,nlines):
	for symbol in symbols.keys():
		value=symbols[symbol]
		binaryvalue=format(value,'08b')
		symbols[symbol]=binaryvalue
	mcode=open("machinecode.txt",'w')
	acode=open("assemblycode.txt","r")
	while(True):
		line=acode.readline()
		if not line:
			break;
		else:
			eof=line.find('/n')
			if(eof!=-1):
				line=line[:-1]
			comment=line.find('//')
			if(comment!=-1):
				line=line[:comment]				#Remove commented part
			if(line!=''):
				colon=line.find(':')
				if(colon!=-1):
					line=line[colon+1:]
				l=line.split()    
				if(len(l)==1):
					mcode.write(opcodereturner(opcode,l[0])+" 00000000"+'\n')
				else:
					mcode.write(opcodereturner(opcode,l[0])+" "+str(symbols[l[1]])+'\n')
	vtable=open("VariableTable.txt",'w')
	vtable.write("VARIABLE\tADDRESS"+'\n')
	ltable=open("LabelTable.txt",'w')
	ltable.write("LABEL\t\tADDRESS"+'\n')
	symbolskeys=symbols.keys()
	for i in symbolskeys:
		if(int(symbols[i],2)<nlines):
			ltable.write(i+'\t\t\t'+symbols[i]+'\n')
		else:
			vtable.write(i+'\t\t\t'+symbols[i]+'\n')
	ltable.close()
	mcode.close()
	acode.close()
	vtable.close()

'''Initialization'''
opcode={"CLA":"0000","LAC":"0001","SAC":"0010","ADD":"0011","SUB":"0100","BRZ":"0101","BRN":"0110","BRP":"0111","INP":"1000","DSP":"1001","MUL":"1010","DIV":"1011","STP":"1100"}
symbols={}
error=False
l1=[]
l2=[]
error,symbols,nlines=pass1(error,opcode,symbols)
if(error==False):
	pass2(opcode,symbols,l1,l2,nlines)
else:
	exit()
