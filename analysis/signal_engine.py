import pandas_ta as ta

def calcular_indicadores(df):
    df["rsi"] = ta.rsi(df["close"], length=14)
    macd = ta.macd(df["close"])
    df["macd_hist"] = macd["MACDh_12_26_9"]
    df["sma_20"] = ta.sma(df["close"], length=20)
    return df

def evaluar_entrada_salida(df):
    ult = df.iloc[-1]
    entrada = ult["rsi"] < 30 and ult["macd_hist"] > 0 and ult["close"] > ult["sma_20"]
    salida = ult["rsi"] > 70 or ult["macd_hist"] < 0 or ult["close"] < ult["sma_20"]
    return entrada, salida
