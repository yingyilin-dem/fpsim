# python -m tests.test_stockout_unit

import numpy as np
import matplotlib.pyplot as plt
from fpsim import Sim
from fpsim.stockout import StockoutIntervention

# Stockout: 100% for method 1 and 3 in 2025–2030
stockout_years = list(range(2025, 2031))
stockout_probs = {year: {1: 1.0, 3: 1.0} for year in stockout_years}

# Create stockout intervention
stockout_interv = StockoutIntervention(
    stockout_probs=stockout_probs,
    seed=123
)

# Simulation with stockout
sim_with = Sim(
    location="kenya", 
    start_year=2020, 
    end_year=2030, 
    n_agents=1000,
    interventions=[stockout_interv],
    label='With stockout'
)
sim_with.run()

# Baseline simulation without stockout
sim_base = Sim(
    location="kenya", 
    start_year=2020, 
    end_year=2030, 
    n_agents=1000,
    label='No stockout'
)
sim_base.run()

# Plot CPR over time
plt.figure(figsize=(10, 5))
plt.plot(sim_base.results['t'], sim_base.results['cpr'], label='No stockout')
plt.plot(sim_with.results['t'], sim_with.results['cpr'], label='With 100% stockout (method 1 & 3, 2025–2030)', linestyle='--')
plt.axvspan(2025, 2030, color='gray', alpha=0.2, label='Stockout period')

plt.xlabel('Year')
plt.ylabel('CPR')
plt.title('Impact of Method 1 & 3 Stockout on Contraceptive Prevalence Rate')
plt.legend()
plt.tight_layout()
plt.grid(True)
plt.show()
