[![MCNP6](https://img.shields.io/badge/MCNP-6.3-blue)](#)[![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python)](#)[![NCRP 151](https://img.shields.io/badge/NCRP-151%20Compliant-green)](#)[![Stars](https://img.shields.io/github/stars/Tamaris-coder/Linac-15MV-Neutron-Shielding?style=social)](#)

# 15 MV Linac Bunker – Full MCNP6 Neutron + Gamma Shielding

 
Real 15 MV medical linac vault Monte Carlo simulation using MCNP6.3  
NCRP Report 151 compliant | Real Iranian hospital geometry

## Key Results
| Parameter                     | Value                    | Limit (NCRP 151) |
|-----------------------------|--------------------------|-------------------------|
| Max neutron dose outside     | **0.018 mSv/week**       | 0.02 mSv/week           |
| Max gamma dose               | 0.009 mSv/week           | 0.02 mSv/week           |
| Maze attenuation (neutrons)  | >10⁴                     | —                       |
| Door design                  | 12 cm 5% borated PE + 18 cm heavy concrete | — |
| **Total door weight**        | **9.8 tons**             | Feasible                |

## Tech Stack
- **MCNP6.3** – Full 3D Monte Carlo (5×10⁷ histories)
- **Python** – Automatic dose extraction & visualization
- **Materials** – Borated polyethylene, heavy concrete (3.8 g/cm³), Cole™ polymer

## Project Structure
- **Materials** – Borated polyethylene, heavy concrete (3.8 g/cm³), Cole™ polymer

## Project Structure
