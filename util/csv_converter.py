import pandas as pd
import pathlib

path = pathlib.Path("../gaia_data/original_data")

for file in path.iterdir():
    if file.is_file():
        if file.suffix == '.csv':
            originalDataframe = pd.read_csv(file.absolute(), header=0, sep=r'\s*,\s*',
                                            engine='python', comment='#')
            filteredDataframe = originalDataframe[["teff_gspphot", "lum_flame"]]
            filteredDataframe.dropna(axis=0, how="any", inplace=True)
            filteredDataframe.to_csv("../gaia_data/filtered_data/" + file.stem + " filtered.csv", index=False)

