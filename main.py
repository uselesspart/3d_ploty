import plotly.graph_objects as go
import pandas as pd
import os
import glob
import numpy as np


if __name__ == "__main__":
    csv_files = glob.glob(os.path.join("./data", "*extention.tsv"))

    dfs = dict()
    for f  in csv_files:
        df = pd.read_csv(f, sep='\t', skiprows=[1])
        dfs[f] = df

    fig = go.Figure()
    for name in dfs.keys():
        data = dfs[name]
        zs = np.zeros(data.size)
        fig.add_trace(go.Scatter3d(
            x=data['lat[deg]'],
            y=data['long[deg]'],
            z=data['speed[kmph]'],
            mode='lines',
            line=dict(color="rgb(100, 100, 100)"),
            marker=dict(size=1)
        ))
        fig.add_trace(go.Scatter3d(
            x=data['lat[deg]'],
            y=data['long[deg]'],
            z=zs,
            mode='lines',
            line=dict(color="rgb(128, 64, 48)"),
            marker=dict(size=1)
        ))  
    fig.update_scenes(aspectratio=dict(x=2, y=2, z=1), xaxis_showgrid=True, xaxis_gridwidth=0.01, yaxis_showgrid=True, yaxis_gridwidth=0.01)
    fig.show()