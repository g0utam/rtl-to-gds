# Automated RTL-to-GDS Design Flow

This repository contains a complete RTL-to-GDSII flow using **OpenROAD**, **Yosys**, and the **SkyWater 130nm (Sky130A) PDK**.  
The example design is a **4-bit ripple-carry adder**, synthesized, placed, routed, and exported to **GDSII**.

---

## 📂 Repository Structure

```
rtl2gds/
├── configs/             # YAML configs for flow
│   └── sky130_hd.yaml
├── scripts/             # Yosys and OpenROAD scripts
├── src/                 # Verilog source files (full_adder, four_bit_adder)
├── tb/                  # Testbenches
├── build/               # Build outputs (sim, pnr, etc.)
├── logs/                # Logs from Yosys, OpenROAD, Magic
├── flow.py              # Flow driver script
└── README.md
```

---

## 🛠️ Requirements

- Ubuntu 22.04+ (WSL2 tested)
- OpenROAD  
- Yosys  
- Icarus Verilog (`iverilog`)  
- Magic + Netgen  
- Sky130 PDK (`open-pdks-sky130`)  

---

## ⚡ Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/g0utam/rtl-to-gds.git
   cd rtl-to-gds
   ```

2. Install dependencies (OpenROAD, Yosys, etc.) and Sky130 PDK:
   ```bash
   sudo apt-get update
   sudo apt-get install -y open-pdks-sky130 yosys iverilog magic netgen klayout
   ```

3. Set environment variables in `~/.bashrc`:
   ```bash
   export PDK_ROOT=/usr/share/pdks
   export SKY130A=$PDK_ROOT/sky130A
   ```

4. Reload:
   ```bash
   source ~/.bashrc
   ```

---

## ▶️ Running the Flow

Run the flow with the provided config:

```bash
python3 flow.py configs/sky130_hd.yaml
```

Steps:
- ✅ RTL simulation (Icarus Verilog)  
- ✅ Logic synthesis (Yosys)  
- ✅ Place & Route (OpenROAD)  
- ✅ DRC & LVS (Magic, Netgen)  
- ✅ Final GDS export  

---

## 📊 Outputs

After a successful run, check:

- **Simulation VCD**: `build/sim/adder_4bit.vcd`  
- **Synthesized netlist**: `build/synth/four_bit_adder.v`  
- **Final GDSII**: `build/pnr/four_bit_adder.gds`  
- **Logs**: `logs/`  

You can open the GDS in [KLayout](https://www.klayout.de/):

```bash
klayout build/pnr/four_bit_adder.gds
```

---

## 📜 License

MIT License.  
This project is for **educational and research purposes** with the open-source SkyWater130 PDK.
