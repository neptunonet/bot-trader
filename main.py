from data.polygon_client import get_ohlc
from analysis.signal_engine import calcular_indicadores, evaluar_entrada_salida

def analizar_ticker(ticker):
    df = get_ohlc(ticker, multiplier=1, timespan="day", from_date="2024-01-01", to_date="2025-06-26")
    df = calcular_indicadores(df)
    entrada, salida = evaluar_entrada_salida(df)
    print(f"{ticker} → Entrada: {entrada} | Salida: {salida}")

if __name__ == "__main__":
    with open("watchlist.txt") as f:
        tickers = [line.strip() for line in f if line.strip()]
    for t in tickers:
        analizar_ticker(t)
