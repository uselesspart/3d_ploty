import plotly.graph_objects as go
import pandas as pd
import os
import glob
import numpy as np
import sys
    

if __name__ == "__main__":
    csv_files = glob.glob(os.path.join("./data", "*.tsv"))

    dfs = dict()
    for f  in csv_files:
        df = pd.read_csv(f, sep='\t',skiprows=[1])
        dfs[f] = df

    fig = go.Figure()
    color = 125
    for name in dfs.keys():
        data = dfs[name]
        zs = np.zeros(data.size)
        fig.add_trace(go.Scatter3d(
            x = data['lat[deg]'],
            y = data['long[deg]'],
            z = data['speed[kmph]'], 
            line=dict(color=str('#%06x' % (color))),
            marker=dict(size=1)
        ))
        fig.add_trace(go.Scatter3d(
            x = data['lat[deg]'],
            y = data['long[deg]'],
            z = zs, 
            line=dict(color=str('#%06x' % (color))),
            marker=dict(size=1)
        ))
    
    fig.update_scenes(aspectratio=dict(x=2, y=2, z=1))
    
    fig.show()