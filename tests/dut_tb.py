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

