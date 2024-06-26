import dash
from dash import html

# Initialize the Dash app
app = dash.Dash(__name__,
                requests_pathname_prefix="/webapp-DIE3/",
                routes_pathname_prefix="/webapp-DIE3/")


# Define the layout of the appd
app.layout = html.Div([
    # Form 1 - Query database
    html.H1('Hello World!')
], style={'width': '50%', 'margin': 'auto', 'font-family': 'Arial, sans-serif'})

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=80)
