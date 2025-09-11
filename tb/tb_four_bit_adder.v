`timescale 1ns/1ps
module tb_four_bit_adder;
  reg [3:0] a, b;
  reg cin;
  wire [3:0] sum;
  wire cout;

  four_bit_adder uut(.a(a), .b(b), .cin(cin), .sum(sum), .cout(cout));

  initial begin
    $dumpfile("adder_4bit.vcd");
    $dumpvars(0, tb_four_bit_adder);

    a=4'b0001; b=4'b0010; cin=0; #10;
    a=4'b0101; b=4'b0110; cin=1; #10;
    a=4'b1111; b=4'b0001; cin=0; #10;

    $display("Simulation Finished");
    $finish;
  end
endmodule
