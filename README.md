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

#### 1. More than one opcode in instruction.

**INP and DSP** both are opcodes. 
![error: More than One Opcode Error](./Assets/Code1.png)
![error: More than One Opcode Code](./Assets/Error1.png)

#### 2. 

### Pseudo Code
#### First Pass

#### Second Pass
