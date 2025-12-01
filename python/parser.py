# parser.py - Extract neutron dose from MCNP output file
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

def parse_mcnp_output(filename="bunker_maino"):
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    dose_values = []
    start_parsing = False
    
    for line in lines:
        if "fmesh4:n" in line.lower():
            start_parsing = True
            continue
        if start_parsing and line.strip() and len(line.split()) > 3:
            
            values = [float(x) for x in line.split()[1::2]]
            dose_values.extend(values)
    
    # reshape  fmesh (z, y, x)
    dose = np.array(dose_values).reshape(45, 140, 180)
    return dose


# dose = parse_mcnp_output("bunker_maino")
# plt.imshow(dose[22,:,:].T, norm=LogNorm(), cmap='viridis')
# plt.colorbar(label='Neutron dose (pSv/primary)')
# plt.title('15 MV Linac - Neutron Dose Map')
# plt.savefig('results/dose_map_neutron.png', dpi=300)
# plt.show()
