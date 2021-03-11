import pandas as pd
import csv
import plotly.graph_objects as go

df = pd.read_csv('height-weight.csv')
print(df.groupby('Height')['Weight'].mean())

fig= go.Figure(go.Bar(
        x='Height',
        y='Weight',
        orientation='h'
)
)

fig.show()