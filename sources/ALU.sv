`timescale 1ns/1ps
module ALU (
    input  logic        clk,   // present but unused
    input  logic [7:0]  A,
    input  logic [7:0]  B,
    input  logic [2:0]  op,
    output logic [7:0]  Y
);

always_comb begin
    case (op)
        3'b000: Y = A + B;                                      // ADD
        3'b001: Y = A - B;                                      // SUB
        3'b010: Y = A & B;                                      // AND
        3'b011: Y = A | B;                                      // OR
        3'b100: Y = A ^ B;                                      // XOR
        3'b101: Y = ($unsigned(A) < $unsigned(B)) ? 8'd1 : 8'd0; // SLT (unsigned)
        default: Y = 8'd0;
    endcase
end

endmodule
