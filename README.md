XY Spirograph
A four-pattern vector display for the Tiny Tapeout micro interface. The RTL in
src/project.v is synthesizable Verilog. Copy it into the Verilog micro-tile
template and set these fields under project in info.yaml:
```yaml
tiles: "micro"
top\_module: "tt\_um\_xy\_spirograph"
source\_files:
  - "project.v"
```
Drive clk at 64 kHz for 1000 repetitions per second. Hold rst_n low across a
rising edge to reset both axes to code 8. Select the pattern with ui_in[1:0].
The remaining six inputs are unused. The two-stage input synchronizer allows
live switching. Changing two switches separately can briefly select another
pattern.
Selector	X	Y
00	Triangle at base frequency	Triangle, quarter-cycle lead
01	Triangle at base frequency	Triangle at twice base frequency, quarter-cycle lead on Y
10	Triangle at twice base frequency	Triangle at three times base frequency
11	Four-point star, 16 coordinate pairs	Same table shifted by four entries
Connect uo_out[3:0] to a 4-bit R-2R ladder for X (bit 3 is MSB).
Connect uo_out[7:4] to a second ladder for Y (bit 7 is MSB).
For each ladder use four nodes from MSB to LSB, an R between adjacent nodes,
a 2R from each node to its digital pin, and a 2R from the LSB node to ground.
Read the analog output at the MSB node. Example: R = 10 kOhm, 2R = 20 kOhm.
Connect X to CH1, Y to CH2, and share board ground with the scope. Use
high-impedance DC-coupled inputs, XY mode, and equal volts/div on both axes.
The DACs output discrete points. Persistence helps reveal them; the appearance
of connecting segments depends on acquisition, analog settling and display mode.
Simulation
From this directory, using Verilator with timing support:
```sh
verilator --binary --timing -Wno-TIMESCALEMOD --top-module tb src/project.v test/tb.sv
./obj\_dir/Vtb
```
The self-checking test compares three complete 64-clock sweeps per mode to
reference coordinates, including selector pipeline latency and resets.
Physical fit and timing require hardening
