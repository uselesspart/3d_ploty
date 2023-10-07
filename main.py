import plotly.graph_objects as go
import pandas as pd
import os
import glob
import numpy as np
import sys

def main():

    path = os.getcwd()
    csv_files = glob.glob(os.path.join(path, "*.tsv"))
    dfs = []

    for f  in csv_files:
        df = pd.read_csv(f, sep='\t')
        dfs.append(df)

    fig = go.Figure()
    color = 0

    for i in dfs:

        size = i.size
        zs = np.zeros(size)
        color = np.random.randint(int(0xFFFFFF))
    
        fig.add_trace(go.Scatter3d(
            x = i['lat[deg]'],
            y = i['long[deg]'],
            z = i['path_meter_pos[m]'], 
            line=dict(color=str('#%06x' % (color))),
            marker=dict(size=1)
        ))
        fig.add_trace(go.Scatter3d(
            x = i['path_meter_pos[m]'],
            y = i['speed[kmph]'],
            z = zs, 
            line=dict(color=str('#%06x' % (color))),
            marker=dict(size=1)
        ))

    fig.show()
    
if __name__ == "__main__":
    main()