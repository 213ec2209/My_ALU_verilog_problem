`timescale 1ns/1ps
module ALU (
    input  wire        clk,   // clock
    input  wire        rst,   // reset
    input  wire [7:0]  A,     // first operand
    input  wire [7:0]  B,     // second operand
    input  wire [2:0]  op,    // operation select
    output reg  [7:0]  Y      // ALU output
);
<<<<<<< HEAD:sources/ALU.v
always @(posedge clk or posedge rst) begin
    if (!rst) begin
        Y <= 8'd0;
=======

always @(posedge clk) begin
    if (rst) begin
        Y <= 8'd0;  // Active HIGH reset - when rst=1, reset to zero
>>>>>>> a8939d7bc04d23a2b6b37b7b0df4b9a821595a1f:sources/ALU.sv
    end else begin
        case (op)
            3'b000: Y <= A + B;                 // ADD
            3'b001: Y <= A - B;                 // SUB
            3'b010: Y <= A & B;                 // AND
            3'b011: Y <= A | B;                 // OR
            3'b100: Y <= A ^ B;                 // XOR
            3'b101: Y <= (A < B) ? 8'd1 : 8'd0; // SLT
            default: Y <= 8'd0;
        endcase
    end
end
endmodule
