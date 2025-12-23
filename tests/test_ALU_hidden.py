import os
from pathlib import Path

import cocotb
from cocotb.triggers import Timer
from cocotb_tools.runner import get_runner

async def generate_clock(dut):
    """Generate clock pulses."""
    for cycle in range(1000):
        dut.clk.value = 0
        await Timer(5, unit="ns")
        dut.clk.value = 1
        await Timer(5, unit="ns")

@cocotb.test()
async def test_ALU_1(dut):
    """ALU operation of ADD"""
    await cocotb.start(generate_clock(dut))
    print("ALU ADD operation")
    await Timer(5, unit="ns")  
    dut.rst.value = 0
    dut.A.value = 0x12
    dut.B.value = 0x10
    dut.op.value = 0
    await Timer(15, unit="ns")
    dut.rst.value = 1
    await Timer(150, unit="ns")  
    dut._log.info("rst = %d, A = %d, B = %d, op = %d, Y = %x",
                  dut.rst.value, dut.A.value, dut.B.value, dut.op.value, dut.Y.value)
    assert dut.Y.value == 0x22, "ADD operation is not correct"   


@cocotb.test()
async def test_ALU_2(dut):
    """ALU operation of SUB"""
    await cocotb.start(generate_clock(dut))
    print("ALU SUB operation")
    await Timer(5, unit="ns")  
    dut.rst.value = 0
    dut.A.value = 0x12
    dut.B.value = 0x10
    dut.op.value = 1
    await Timer(15, unit="ns")
    dut.rst.value = 1
    await Timer(150, unit="ns")  
    dut._log.info("rst = %d, A = %d, B = %d, op = %d, Y = %x",
                  dut.rst.value, dut.A.value, dut.B.value, dut.op.value, dut.Y.value)
    assert dut.Y.value == 0x2, "SUB operation is not correct"   

@cocotb.test()
async def test_ALU_3(dut):
    """ALU operation of AND"""
    await cocotb.start(generate_clock(dut))
    print("ALU AND operation")
    await Timer(5, unit="ns")  
    dut.rst.value = 0
    dut.A.value = 0x12
    dut.B.value = 0x10
    dut.op.value = 2
    await Timer(15, unit="ns")
    dut.rst.value = 1
    await Timer(150, unit="ns")  
    dut._log.info("rst = %d, A = %d, B = %d, op = %d, Y = %x",
                  dut.rst.value, dut.A.value, dut.B.value, dut.op.value, dut.Y.value)
    assert dut.Y.value == 0x10, "AND operation is not correct"   


@cocotb.test()
async def test_ALU_4(dut):
    """ALU operation of OR"""
    await cocotb.start(generate_clock(dut))
    print("ALU OR operation")
    await Timer(5, unit="ns")  
    dut.rst.value = 0
    dut.A.value = 0x12
    dut.B.value = 0x10
    dut.op.value = 3
    await Timer(15, unit="ns")
    dut.rst.value = 1
    await Timer(150, unit="ns")  
    dut._log.info("rst = %d, A = %d, B = %d, op = %d, Y = %x",
                  dut.rst.value, dut.A.value, dut.B.value, dut.op.value, dut.Y.value)
    assert dut.Y.value == 0x12, "or operation is not correct"   


@cocotb.test()
async def test_ALU_5(dut):
    """ALU operation of XOR"""
    await cocotb.start(generate_clock(dut))
    print("ALU XOR operation")
    await Timer(5, unit="ns")  
    dut.rst.value = 0
    dut.A.value = 0x12
    dut.B.value = 0x10
    dut.op.value = 4
    await Timer(15, unit="ns")
    dut.rst.value = 1
    await Timer(150, unit="ns")  
    dut._log.info("rst = %d, A = %d, B = %d, op = %d, Y = %x",
                  dut.rst.value, dut.A.value, dut.B.value, dut.op.value, dut.Y.value)
    assert dut.Y.value == 0x02, "xor operation is not correct"   


@cocotb.test()
async def test_ALU_6(dut):
    """ALU operation of compare"""
    await cocotb.start(generate_clock(dut))
    print("ALU compare operation")
    await Timer(5, unit="ns")  
    dut.rst.value = 0
    dut.A.value = 0x12
    dut.B.value = 0x10
    dut.op.value = 5
    await Timer(15, unit="ns")
    dut.rst.value = 1
    await Timer(150, unit="ns")  
    dut._log.info("rst = %d, A = %d, B = %d, op = %d, Y = %x",
                  dut.rst.value, dut.A.value, dut.B.value, dut.op.value, dut.Y.value)
    assert dut.Y.value == 0x00, "A>B operation is not correct"   

@cocotb.test()
async def test_ALU_7(dut):
    """ALU operation of compare"""
    await cocotb.start(generate_clock(dut))
    print("ALU compare operation")
    await Timer(5, unit="ns")  
    dut.rst.value = 0
    dut.A.value = 0x05
    dut.B.value = 0x10
    dut.op.value = 5
    await Timer(15, unit="ns")
    dut.rst.value = 1
    await Timer(150, unit="ns")  
    dut._log.info("rst = %d, A = %d, B = %d, op = %d, Y = %x",
                  dut.rst.value, dut.A.value, dut.B.value, dut.op.value, dut.Y.value)
    assert dut.Y.value == 0x01, "A<B operation is not correct"   

# CRITICAL: Pytest wrapper function
def test_ALU_hidden_runner():
    """Pytest wrapper to run cocotb tests"""
    sim = os.getenv("SIM", "icarus")
    proj_path = Path(__file__).resolve().parent.parent
    
    sources = [
        proj_path / "sources/ALU.v",
    ]
    
    runner = get_runner(sim)
    runner.build(
        sources=sources,
        hdl_toplevel="ALU",
        always=True,
    )
    
    runner.test(
        hdl_toplevel="ALU",
        test_module="test_ALU_hidden"
    )
