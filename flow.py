import os
import sys
import subprocess
import yaml

def run_cmd(cmd, log_file=None):
    print(f">> {cmd}")
    if log_file:
        with open(log_file, "w") as f:
            subprocess.run(cmd, shell=True, check=True, stdout=f, stderr=subprocess.STDOUT)
    else:
        subprocess.run(cmd, shell=True, check=True)

def main(cfg_path):
    # Load YAML config
    with open(cfg_path) as f:
        cfg = yaml.safe_load(f)

    design = cfg["design"]
    top = cfg["top"]
    src_files = " ".join(cfg["src_files"])
    tb_files = " ".join(cfg["tb_files"])

    os.makedirs("build/sim", exist_ok=True)
    os.makedirs("logs", exist_ok=True)
    os.makedirs("build/pnr", exist_ok=True)

    # 1. Run simulation
    run_cmd(f"iverilog -o build/sim/sim.out {tb_files} {src_files}")
    run_cmd("vvp build/sim/sim.out")

    # 2. Run synthesis with Yosys
    yosys_cmd = f"yosys -p 'read_verilog {src_files}; synth -top {top}; write_json build/{design}.json'"
    run_cmd(yosys_cmd, log_file="logs/yosys.log")

    # 3. Run OpenROAD (PnR)
    openroad_cmd = f"openroad -exit scripts/pnr.tcl"
    run_cmd(openroad_cmd, log_file="logs/openroad.log")

    # 4. Run DRC with Magic
    magic_cmd = f"magic -dnull -noconsole -T $SKY130A/tech/magic/sky130A.tech scripts/drc.tcl"
    run_cmd(magic_cmd, log_file="logs/magic_drc.log")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 flow.py <config.yaml>")
        sys.exit(1)
    main(sys.argv[1])
