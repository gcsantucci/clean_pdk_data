# Data Cleaning for PDK and atm nu MC events in Super-Kamiokande

(reason for creating this repo is for reference only)

Read the pickle files created by ROOTtoPandas.

These are DataFrames containing info from original file plus features created by 
the macro NewVars.C

Cleaning creates the necessary likelihood ratios, drop unecessary columns, adjust variable types
and writes to dataframe to pickle file. But only for selected events.
For now, these are: FCFV + 1-ring mu-like + 1 decay-e.

## Original Numbers from PDK MC:

Each file originally had 100,000 events. After running detector simulation (SKDETSIM) and FC reduction (fccomb) each file has:

- File 0:

Total number of events: 96363. FC reduction of 3.6%.
Number of events inside True FCFV: 80147.
Total number of MuGamma events: 28410.
Number of MuGamma events inside True FCFV: 23583.
Efficiency loss of 17.0%.

- File 1:

Total number of events: 96404. FC reduction of 3.6%.
Number of events inside True FCFV: 80161.
Total number of MuGamma events: 28615.
Number of MuGamma events inside True FCFV: 23715.
Efficiency loss of 17.0%.

- File 2:

Total number of events: 96301. FC reduction of 3.7%.
Number of events inside True FCFV: 79991.
Total number of MuGamma events: 28764.
Number of MuGamma events inside True FCFV: 23870.
Efficiency loss of 17.0%.

- File 3:

Total number of events: 96335. FC reduction of 3.7%.
Number of events inside True FCFV: 79960.
Total number of MuGamma events: 28802.
Number of MuGamma events inside True FCFV: 23919.
Efficiency loss of 17.0%.

- File 4:

Total number of events: 96273. FC reduction of 3.7%.
Number of events inside True FCFV: 79878.
Total number of MuGamma events: 28347.
Number of MuGamma events inside True FCFV: 23435.
Efficiency loss of 17.0%.

- File 5:

Total number of events: 96366. FC reduction of 3.6%.
Number of events inside True FCFV: 79989.
Total number of MuGamma events: 28545.
Number of MuGamma events inside True FCFV: 23696.
Efficiency loss of 17.0%.
