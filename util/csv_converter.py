import pandas as pd

originalDataframe = pd.read_csv('gaia-1.csv', header=0, sep=r'\s*,\s*', engine='python', comment='#')
filteredDataframe = originalDataframe[["teff_gspphot", "lum_flame"]]
filteredDataframe.dropna(axis=0, how="any",inplace=True)
filteredDataframe.to_csv("gaia-1 filtered.csv", index=False)