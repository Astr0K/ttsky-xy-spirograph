# XY Spirograph

A Tiny Tapeout SKY130 micro-tile project that draws four selectable patterns on an oscilloscope in XY mode. The Verilog design generates two 4-bit coordinates that drive external R-2R DACs.

## Patterns

| `ui_in[1:0]` | Pattern |
| --- | --- |
| `00` | Diamond |
| `01` | Bow tie |
| `10` | Crisscross |
| `11` | Four-point star |

## Hardware

Connect `uo_out[3:0]` to the X DAC and `uo_out[7:4]` to the Y DAC. At a 64 kHz clock, the pattern repeats 1,000 times per second.

See the [project datasheet](docs/info.md) for wiring and test instructions.

## Simulation

The cocotb test in `test/test.py` checks reset and the first five coordinate samples of the diamond pattern.
