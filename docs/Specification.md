ALU Documentation
Overview

An Arithmetic Logic Unit (ALU) is a fundamental digital circuit used to perform arithmetic and logical operations on binary data. The ALU forms a core component of processors, controllers, and digital hardware systems. It operates on two input operands and produces a result based on a selected operation.

The ALU described in this document is an 8-bit synchronous ALU that performs arithmetic and logical operations on two 8-bit input operands. The ALU operates under the control of a clock signal and a reset signal. The output is registered and updated on the rising edge of the clock. When the reset signal is low, the output Y is cleared to zero. To understand the ALU functionality, the following parameters are required:

Clock signal (clk)
Reset signal (rst)
First operand (A)
Second operand (B)
Operation select (op)
ALU result (Y)

ALU Operation Description

The ALU performs different arithmetic and logical operations based on the value of the operation select signal op. All operations are executed synchronously on the rising edge of the clock.

The ALU operation is defined as follows:
On every positive edge of clk or negative edge of rst, the ALU samples inputs A, B, and op
Based on the value of op, the corresponding arithmetic or logical operation is performed
The computed result is stored in the output register Y
When rst is high, the output Y is reset to zero regardless of the operation

Operation Encoding
op	Operation	Description
000	ADD	Addition of A and B
001	SUB	Subtraction of B from A
010	AND	Bitwise AND
011	OR	Bitwise OR
100	XOR	Bitwise XOR
101	SLT	Set Less Than (unsigned comparison)
Others	DEFAULT	Output forced to zero
Functionality

The ALU module accepts two 8-bit input operands (A and B) and a 3-bit operation selector (op). On the rising edge of the clock, the ALU computes the selected arithmetic or logical operation and produces an 8-bit output (Y). The output remains stable between clock edges.

Inputs
A : 8-bit input operand
B : 8-bit input operand
op : 3-bit operation selector
clk : Clock signal
rst : Active-high reset signal

Outputs
Y : 8-bit registered result of the selected operation


Arithmetic Operations

Addition (ADD) and Subtraction (SUB) are performed using standard 8-bit unsigned arithmetic.

Overflow and underflow are ignored and truncated to 8 bits.

Logical Operations

Bitwise logical operations include AND, OR, and XOR.
Each logical operation is performed independently on the corresponding bits of operands A and B.
Set-on-Less-Than (SLT)
The SLT operation compares operands A and B.
If A is less than B, the output is set to 8'd1.
Otherwise, the output is set to 8'd0.
The comparison is performed as an unsigned comparison.
Default Case Handling
For undefined or unsupported operation codes, the output Y is forced to zero.

ALU Operation Algorithm

Step 1 — Input Sampling
The operands A and B, along with the operation code op, are sampled on the rising edge of the clock and falling edge of rst.

Step 2 — Operation Decode
The operation code op determines which arithmetic or logical function is executed.

Step 3 — Result Computation

The ALU operations can be expressed as:

ADD
Y = A + B
SUB
Y = A − B
AND
Y = A ∧ B
OR
Y = A ∨ B
XOR
Y = A ⊕ B
SLT
Y = 1 if A < B else 0 (unsigned comparison)
Step 4 — Default Handling
If op does not match a valid operation, the output is set to zero:
Y = 0

Algorithm Representation
if rst=1
Y=0;
elseif op == 000:
    Y = A + B
elif op == 001:
    Y = A - B
elif op == 010:
    Y = A & B
elif op == 011:
    Y = A | B
elif op == 100:
    Y = A ^ B
elif op == 101:
    if A < B:
        Y = 1
    else:
        Y = 0
else:
    Y = 0


Here,< : Unsigned comparison; + : 8-bit addition; - : 8-bit subtraction; & : Bitwise AND;|: Bitwise OR; ^ : Bitwise XOR; A : 8-bit input operand; B : 8-bit input operand; op: 3-bit operand selection; rst : 1-bit reset operand;

At the beginning of the ALU operation, the two 8-bit input operands are assumed as A and B, and the 3-bit operation select signal op determines the function to be executed, and the output is set to zero when the rst signal is high. Every ALU operation is carried out synchronously on the rising edge of the clock and falling edge of rst, and each computation cycle produces a single registered result. The output of the ALU is stored in register Y, which retains its value until the next clock edge.

Each ALU operation is executed sequentially in time, such that the result of one clock cycle is available only after the rising edge of the clock. The computation does not depend on previous ALU results, but the sequential nature ensures deterministic timing behavior suitable for synchronous digital systems.

The ALU supports multiple arithmetic and logical operations, including addition, subtraction, bitwise logical functions, and comparison operations. Although the ALU architecture can be extended to support wider data widths, the current implementation operates on 8-bit unsigned operands, making it suitable for compact processing units and educational RTL designs.

The operation selection is controlled by the op signal, which defines the function to be performed in a given clock cycle. For unsupported or invalid operation codes, the ALU output is forced to zero to maintain deterministic behavior.

The reset signal controls the initialization of the ALU output. When the reset signal is asserted low, the output register Y is cleared to zero, regardless of the input operands or operation code. This ensures proper initialization of the ALU before normal operation begins.

FSM-Controlled Process

The ALU operates as a single-state synchronous process
There is no multi-state FSM
Each rising edge of the clock triggers exactly one ALU operation
The output Y is updated once per clock cycle

ALU Operation Example
Let us consider the following parameters:

A  = 8'h12
B  = 8'h10
op = 3'b000

Solution:
Y = A + B
  = 8'h12 + 8'h10
  = 8'h22
Final Output:

Y = 8'h22
