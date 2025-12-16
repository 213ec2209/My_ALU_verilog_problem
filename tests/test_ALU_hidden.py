import cocotb
from cocotb.triggers import Timer
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge

@cocotb.test()
async def test_alu_add(dut):
    """Test ALU ADD"""
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())

    await RisingEdge(dut.clk)   # ✅ correctly indented
    dut.A.value = 0x12
    dut.B.value = 0x10
    dut.op.value = 0  

    await RisingEdge(dut.clk)

    dut._log.info(f"A={dut.A.value} B={dut.B.value} Y={dut.Y.value}")
    assert dut.Y.value == 0x22

@cocotb.test()
async def test_alu_sub(dut):
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())

    await RisingEdge(dut.clk)   # ✅ correctly indented

   await RisingEdge(dut.clk)
    dut.A.value = 0x12
    dut.B.value = 0x10
    dut.op.value = 1  

    await RisingEdge(dut.clk)
    assert dut.Y.value == 0x02


@cocotb.test()
async def test_alu_and(dut):
    """Test ALU AND"""
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())
 
    await RisingEdge(dut.clk)   # ✅ correctly indented
    dut.A.value = 0x12
    dut.B.value = 0x10
    dut.op.value = 2  
    await RisingEdge(dut.clk)
    assert dut.Y.value == 0x10


@cocotb.test()
async def test_alu_or(dut):
    """Test ALU OR"""
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())
  
    await RisingEdge(dut.clk)   # ✅ correctly indented
    dut.A.value = 0x12
    dut.B.value = 0x10
    dut.op.value = 3  
    
    await RisingEdge(dut.clk)
    assert dut.Y.value == 0x12


@cocotb.test()
async def test_alu_xor(dut):
    """Test ALU XOR"""
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())
 
    await RisingEdge(dut.clk)   # ✅ correctly indented
    dut.A.value = 0x12
    dut.B.value = 0x10
    dut.op.value = 4  

    await RisingEdge(dut.clk)
    assert dut.Y.value == 0x02


@cocotb.test()
async def test_alu_slt_unsigned(dut):
    """Test ALU SLT (unsigned)"""
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())

    await RisingEdge(dut.clk)   # ✅ correctly indented
    dut.A.value = 0x12
    dut.B.value = 0x10
    dut.op.value = 5  

    await RisingEdge(dut.clk)
    assert dut.Y.value == 0x00

def test_ALU_hidden_runner():
    import os
    from pathlib import Path
    from cocotb_tools.runner import get_runner
    
    sim = os.getenv("SIM", "icarus")
    proj_path = Path(__file__).resolve().parent.parent
    
    sources = [
        proj_path / "sources/ALU.sv",
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

