import pandas as pd

def find_context(df: pd.DataFrame, pergunta: str):
    pergunta_lower = pergunta.lower()
    for _, row in df.iterrows():
        if row['tema'] in pergunta_lower:
            return row
    return df.iloc[0]