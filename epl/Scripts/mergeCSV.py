import pandas as pd
combined_csv = pd.concat( [ pd.read_csv(f) for f in filenames ] )
combined_csv.to_csv( "combined_csv.csv", index=False )
