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

### Error Handling

#### 1. More than one opcode in Instruction

**INP and DSP** both are opcodes. 
![error: More than One Opcode Error](./Assets/Code1.png)
![error: More than One Opcode Code](./Assets/Error1.png)

#### 2. Label Name cannot be a Symbol Name
![error: Label Name cannot be a Symbol Name](./Assets/Code2.png)
![error: Label Name cannot be a Symbol Name](./Assets/Error2.png)

#### 3. More than one Symbol provided
![error: More than one Symbol provided](./Assets/Code3.png)
![error: More than one Symbol provided](./Assets/Error3.png)

#### 4. More than one Label provided
![error: More than one Label provided](./Assets/Code4.png)
![error: More than one Label provided](./Assets/Error4.png)

#### 5. No Opcode found in a Instruction
![error: No Opcode found in a Instruction](./Assets/Code5.png)
![error: No Opcode found in a Instruction](./Assets/Error5.png)

#### 6. Insufficient Number of Arguments 
![error: No Opcode found in a Arguments](./Assets/Code6.png)
![error: No Opcode found in a Arguments](./Assets/Error6.png)

#### 7. Formatting Error(Opcode occur after arguments in a Instruction)
![error: Formatting Error](./Assets/Code7.png)
![error: Formatting Error](./Assets/Error7.png)

### Pseudo Code
#### First Pass

#### Second Pass
