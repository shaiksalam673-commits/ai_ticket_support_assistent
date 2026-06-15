import pandas as pd

def load_data():
    df = pd.read_excel("data/support_tickets.xlsx")
    return df