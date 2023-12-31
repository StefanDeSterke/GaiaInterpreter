""" gaia.py:  Retrieve certain Gaia-parameters and plot these parameters in an HRD.
"""

from util import gaia_retriever
from astroquery.gaia import Gaia

# Read the CSV files as a Pandas DataFrame:
# df = gaia_retriever.local_retrieve_astrophysical_parameters()

Gaia.ROW_LIMIT = -1
Gaia.login(user=config.user, password=config.password)

df = gaia_retriever.async_retrieve_astrophysical_parameters()

# Plot:

import matplotlib
matplotlib.rcParams.update({'font.size': 16})  # Set font size for all text: combine screen visibility with report readability - default: 12 10?
import matplotlib.pyplot as plt         # Get matplotlib.pyplot

# plt.style.use('dark_background')        # Invert colours

fig = plt.figure(figsize=(19.2,10.8))       # Set png size to 1920x1080; savefig has default dpi 100;  default: 6.4,4.8
ax1 = fig.add_subplot(111)                  # Create an axes object for the current figure

# Plot a HRD from the data:
ax1.plot(df.teff_gspphot, df.lum_flame, '.', markersize=2)  # '.': plot dots instead of a line
ax1.legend()

# Plot the inverse of the x-axis
ax1.invert_xaxis()

plt.xlabel(r'$T_\mathrm{eff}/K$')                    # Label the horizontal axis
plt.ylabel(r'$L/L_\odot$')                    # Label the horizontal axis

# Use a logarithmic scale for both axes

plt.xscale('log')
plt.yscale('log')

# Set the bound for both axes

ax1.set_xbound(lower=2512,upper=39810)
ax1.set_ybound(lower=0.001,upper=100000)

# Set the tick interval for the x-axis

ax1.set_xticks([3000, 10000, 30000])
ax1.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())

ax1.grid(True)                            # Plot a grid
fig.tight_layout()                        # Use narrow margins

plt.show()                                # Show the plot to screen
fig.savefig('gaia random sql-1.png')                 # Save the plot as png (use pdf for better quality)
plt.close()                               # Close the plot in order to start a new one later

