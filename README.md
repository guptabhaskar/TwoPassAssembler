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
7. Symbol cannot be an opcode and vice-versa.
8. Label cannot be a symbol and vice-versa.
9. Symbol should only be defined once.
10. Number of instructions should not exceed 256 or else it will give an error.

### Opcode Table
![error: Opcode Table Added](./Assets/Opcode_Table.png)

### Assembly Test Code
![error: Assembly Code Added](./Assets/AssemblyCode.png)

### Symbol Table
![error: Symbol Table Added](./Assets/SymbolTable.png)

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
If we provide more than one symbol to a instruction, it will throw this error as shown.
![error: More than one Symbol provided](./Assets/Code3.png)
![error: More than one Symbol provided](./Assets/Error3.png)

#### 4. More than one Label provided
If we provide more than one label to a instruction, it will throw this error as shown.
![error: More than one Label provided](./Assets/Code4.png)
![error: More than one Label provided](./Assets/Error4.png)

#### 5. No Opcode found in a Instruction
Each instruction should have a opcode but if it does not have one than it will give this error.
![error: No Opcode found in a Instruction](./Assets/Code5.png)
![error: No Opcode found in a Instruction](./Assets/Error5.png)

#### 6. Insufficient Number of Arguments 
If a opcode requires a variable and you don't provide it with a variable than it will throw this error.
![error: No Opcode found in a Arguments](./Assets/Code6.png)
![error: No Opcode found in a Arguments](./Assets/Error6.png)

#### 7. Formatting Error(Opcode occur after arguments in a Instruction)
If variable is used before the opcode in a instruction than it will give the following error.
![error: Formatting Error](./Assets/Code7.png)
![error: Formatting Error](./Assets/Error7.png)

#### 8. Label Name cannot be a Opcode
If label name is a opcode than it will give the following output. 
![error: Label Name cannot be a Opcode](./Assets/Code8.png)
![error: Label Name cannot be a Opcode](./Assets/Error8.png)

### Pseudo Code
#### First Pass

#### Second Pass
