import cocotb
from cocotb.triggers import Timer
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge

@cocotb.test()
async def test_alu_add(dut):
    """Test ALU ADD"""
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())

    dut.A.value = 0x12
    dut.B.value = 0x10
    dut.op.value = 0  # ADD

    await RisingEdge(dut.clk)

    dut._log.info(f"A={dut.A.value} B={dut.B.value} Y={dut.Y.value}")
    assert dut.Y.value == 0x22


@cocotb.test()
async def test_alu_sub(dut):
    """Test ALU SUB"""
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())

    dut.A.value = 0x12
    dut.B.value = 0x10
    dut.op.value = 1  # SUB

    await RisingEdge(dut.clk)
    assert dut.Y.value == 0x02


@cocotb.test()
async def test_alu_and(dut):
    """Test ALU AND"""
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())

    dut.A.value = 0x12
    dut.B.value = 0x10
    dut.op.value = 2  # AND

    await RisingEdge(dut.clk)
    assert dut.Y.value == 0x10


@cocotb.test()
async def test_alu_or(dut):
    """Test ALU OR"""
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())

    dut.A.value = 0x12
    dut.B.value = 0x10
    dut.op.value = 3  # OR

    await RisingEdge(dut.clk)
    assert dut.Y.value == 0x12


@cocotb.test()
async def test_alu_xor(dut):
    """Test ALU XOR"""
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())

    dut.A.value = 0x12
    dut.B.value = 0x10
    dut.op.value = 4  # XOR

    await RisingEdge(dut.clk)
    assert dut.Y.value == 0x02


@cocotb.test()
async def test_alu_slt_unsigned(dut):
    """Test ALU SLT (unsigned)"""
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())

    dut.A.value = 0x12
    dut.B.value = 0x10
    dut.op.value = 5  # SLT

    await RisingEdge(dut.clk)
    assert dut.Y.value == 0x00
