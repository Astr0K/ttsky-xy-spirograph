import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer


@cocotb.test()
async def test_reset_and_diamond(dut):
    dut.ui_in.value = 0
    dut.rst_n.value = 0
    cocotb.start_soon(Clock(dut.clk, 200, unit="ns").start())

    await RisingEdge(dut.clk)
    await Timer(50, unit="ns")
    assert int(dut.uo_out.value) == 0x88

    dut.rst_n.value = 1
    for expected in (0x80, 0x80, 0x91, 0x91, 0xA2):
        await RisingEdge(dut.clk)
        await Timer(50, unit="ns")
        assert int(dut.uo_out.value) == expected
