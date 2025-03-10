import dash
from dash import dcc, html
# import dash_bootstrap_components as dbc

# Initialisation de l'application Dash
app = dash.Dash(__name__)

# Définition de la mise en page
app.layout = html.Div([
    html.H1("Hello World !", style={'textAlign': 'center'})
])

# Exécution du serveur
if __name__ == '__main__':
    app.run_server(debug=True)