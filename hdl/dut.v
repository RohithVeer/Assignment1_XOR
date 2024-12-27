module dut (
    input wire a,
    input wire b,
    output wire y
);

    assign y = a ^ b;  // XOR operation

`ifdef ICARUS_SIM
    initial begin
        $dumpfile("xor_result.vcd");  // Specify the VCD file
        $dumpvars(0, dut);      // Dump all variables in the DUT
    end
`endif

endmodule

