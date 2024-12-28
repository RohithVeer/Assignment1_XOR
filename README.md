# assignment-xor

*Estimated Completion Time* 10 min

This assignment is not complex. It follows the same concepts as discussed in https://youtu.be/AcLHSpvPaRQ 

This project demonstrates how to use Cocotb (Coroutine-based Co-simulation Testbench) to verify a Verilog module implementing an XOR operation.

Prerequisites

Cocotb,Icarus Verilog:- https://www.youtube.com/watch?v=WIKXy5tYCp4


Verilog Module: dut_xor.v

This module performs a 2-input XOR operation:

module dut (
    input wire a,
    input wire b,
    output wire y
);
    assign y = a ^ b;
endmodule

Cocotb Testbench: dut_tb.py

The Python testbench verifies the XOR operation for all input combinations:

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def xor_gate_test(dut):
    """
    Testbench for XOR gate.
    Drives inputs and checks the output against the expected result.
    """
    # Define test cases: (a, b, expected_output)
    test_vectors = [
        (0, 0, 0),  # A=0, B=0, Y=0
        (0, 1, 1),  # A=0, B=1, Y=1
        (1, 0, 1),  # A=1, B=0, Y=1
        (1, 1, 0)   # A=1, B=1, Y=0
    ]

    for a, b, expected_y in test_vectors:
        # Apply inputs
        dut.a.value = a
        dut.b.value = b

        # Wait for some time to simulate propagation delay
        await Timer(2, units="ns")

        # Check the output
        assert dut.y.value == expected_y, f"Failed for A={a}, B={b}: Y={dut.y.value}, expected={expected_y}"

    # Optional: Mark the test as complete with a success message
    dut._log.info("All test cases passed!")


Makefile

The Makefile automates the simulation process:

SIM ?= icarus
TOPLEVEL_LANG ?= verilog
VERILOG_SOURCES += $(PWD)/../hdl/dut.v
xor:
	rm -rf sim_build
	$(MAKE) sim MODULE=dut_tb TOPLEVEL=dut
include $(shell cocotb-config --makefiles)/Makefile.sim

How to Run the Simulation!

Navigate to the project directory:

cd project-directory

Run the testbench using make:

make xor

Check the simulation results in the terminal or under the results/ directory if configured.

Expected Output

The testbench will verify the XOR logic for all input combinations. A successful run will output something like:

# Simlation Results
![WhatsApp Image 2024-12-27 at 11 35 56 PM](https://github.com/user-attachments/assets/39d4bc1d-c77c-4824-aad4-8db552c5020d)
![WhatsApp Image 2024-12-27 at 11 38 09 PM](https://github.com/user-attachments/assets/5a4bb0e3-8c8d-45cc-833c-982507ff5ba0)


The Simulation Graphs ould be observed by running the cmd "gtkwave xor_result.vcd"(cmd in the "")
This project is open-source and licensed under the MIT License. Feel free to use and modify it as needed.


