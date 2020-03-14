## Course: CSE112 Computer Organization at IIITD

### Project Members:

1. Bhaskar Gupta
2. Rishav Kumar

### Assumptions:

1. Clear Accumulator(CLR) clears the accumulator. No address and value is present after clearing the accumulator.
2. Comments could be added using **"//"**. They are removed by the assembler for conversion to machine code.
3. No macros and procedures are to be assembled.
4. No literals are to be handled.
5. Only the opcodes given should be used. All these opcodes are pre-added as a dictionary in the program and are not read from a separate file.
6. Label cannot be an opcode and vice-versa.
7. Variable cannot be an opcode and vice-versa.
8. Label cannot be a variable and vice-versa.
9. Variable should only be defined once.
10. Number of instructions should not exceed 256 or else it will give an error.

### Opcode Table
![error: Opcode Table Added](./Assets/Opcode_Table.png)

### Assembly Test Code
![error: Assembly Code Added](./Assets/AssemblyCode.png)

### Variable Table
![error: Variable Table Added](./Assets/VariableTable.png)

### Label Table
![error: Label Table Added](./Assets/LabelTable.png)

### Machine Code
![error: Machine Code Added](./Assets/MachineCode.png)

### Error Handling

#### 1. More than one opcode in Instruction

**INP and DSP** both are opcodes. But, a instruction cannot have more than one opcode so it will throw an error. 
![error: More than One Opcode Error](./Assets/Code1.png)
![error: More than One Opcode Code](./Assets/Error1.png)

#### 2. Label Name cannot be a Symbol Name
If we use a symbol name as a label name, it will throw an error as shown.

![error: Label Name cannot be a Symbol Name](./Assets/Code2.png)
![error: Label Name cannot be a Symbol Name](./Assets/Error2.png)

#### 3. More than one Symbol provided
If we provide more than one symbol to an instruction, it will throw this error as shown.
![error: More than one Symbol provided](./Assets/Code3.png)
![error: More than one Symbol provided](./Assets/Error3.png)

#### 4. More than one Label provided
If we provide more than one label to an instruction, it will throw this error as shown.
![error: More than one Label provided](./Assets/Code4.png)
![error: More than one Label provided](./Assets/Error4.png)

#### 5. No Opcode found in a Instruction
Each instruction should have an opcode but if it does not have one then it will give this error.
![error: No Opcode found in a Instruction](./Assets/Code5.png)
![error: No Opcode found in a Instruction](./Assets/Error5.png)

#### 6. Insufficient Number of Arguments 
If an opcode requires a variable and you don't provide it with a variable then it will throw this error.
![error: No Opcode found in a Arguments](./Assets/Code6.png)
![error: No Opcode found in a Arguments](./Assets/Error6.png)

#### 7. Formatting Error(Opcode occur after arguments in a Instruction)
If variable is used before the opcode in an instruction then it will give the following error.
![error: Formatting Error](./Assets/Code7.png)
![error: Formatting Error](./Assets/Error7.png)

#### 8. Label Name cannot be a Opcode
If label name is an opcode than it will give the following output. 
![error: Label Name cannot be a Opcode](./Assets/Code8.png)
![error: Label Name cannot be a Opcode](./Assets/Error8.png)
#### 9. Memory Limit Exceeded
Overload triggered by more commands and variables processed than the maximum limit. Our assembler limit is 256 (0–255).

### Pseudo Code

#### First Pass


If the first pass ends successfully, then only the second pass is executed.


**1.** Open input file to read the file line by line.


**2.** Check and remove the commented part in the line if any. 


**3.** Check the presence of opcode in a line by using the function

	def opcodereturner(opcode,line):

	''' 

	Parameter Type: Opcode Dictionary, Line/Word to check

	Return Type: String 

	That is the opcode of the assembly opcode in that line.

	'''


**4.** Check if its a instruction or not by using the function

	def checkifinstruction(opcode,op):

	'''		

	Parameter Type: Opcode Dictionary, Word(Maybe Opcode)

	Return Type: Boolean 

	Checks if the string is whether a instruction or not by 

	checking in the opcode dictionary keys.

	'''	


**5.** Count the no. of opcodes in an instruction using the function

	def no_of_opcodes(line,opcode):

	'''

	Parameter Type: Line, Opcode Dictionary

	Return Type: Int

	This function gives no. of opcodes in a line.

	'''


**6.** We have defined a boolean type variable **“error”** which is **False** in the beginning and turns **True** if an error 

occurs during the first pass. This stops the execution of the second pass from executing if **“error“** is equal to **True**. 


#### Second Pass


**1.** This is only executed if “error” is equal to False.


**2.** All the Instructions are read again in the second pass. 


**3.** Label Table and Variable Table are made in the second pass.


**4.** Whole assembly code is converted into machine code line by line and added into the file machinecode.txt.



