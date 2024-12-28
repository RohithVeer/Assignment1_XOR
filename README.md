# assignment-xor

*Estimated Completion Time* 10 min

This assignment is not complex. It follows the same concepts as discussed in https://youtu.be/AcLHSpvPaRQ 

This project demonstrates how to use Cocotb (Coroutine-based Co-simulation Testbench) to verify a Verilog module implementing an XOR operation.

# Prerequisites

Cocotb,Icarus Verilog:- https://www.youtube.com/watch?v=WIKXy5tYCp4
# dut.v

This module performs a 2-input XOR operation:

module dut (
    input wire a,
    input wire b,
    output wire y
);
    assign y = a ^ b;
endmodule

Expected Output

The testbench will verify the XOR logic for all input combinations. A successful run will output something like:

# Simlation Results
![WhatsApp Image 2024-12-27 at 11 35 56 PM](https://github.com/user-attachments/assets/39d4bc1d-c77c-4824-aad4-8db552c5020d)
![WhatsApp Image 2024-12-27 at 11 38 09 PM](https://github.com/user-attachments/assets/5a4bb0e3-8c8d-45cc-833c-982507ff5ba0)




