import plotly.graph_objects as go
import pandas as pd

def main():
    pd.options.plotting.backend = "plotly"
    df1 = pd.read_csv('line1.csv')
    df2 = pd.read_csv('line2.csv')
    df3 = pd.read_csv('line3.csv')
    dfs = {'df1' : df1, 'df2' : df2, 'df3' : df3}

    fig = go.Figure()

    for i in dfs:
        fig.add_trace(go.Scatter3d(
            x = dfs[i]['x'],
            y = dfs[i]['y'],
            z = dfs[i]['z']
        ))
    
    fig.show()
    
if __name__ == "__main__":
    main()