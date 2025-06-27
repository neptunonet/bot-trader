from datetime import datetime, timedelta
from data.polygon_client import get_ohlc
from analysis.signal_engine import calcular_indicadores, evaluar_entrada_salida

def analizar_ticker(ticker):
    try:
        # Definimos rango: últimos 10 días
        to_date = datetime.now().date()
        from_date = to_date - timedelta(days=10)

        df = get_ohlc(
            ticker=ticker,
            multiplier=1,
            timespan="day",
            from_date=str(from_date),
            to_date=str(to_date)
        )

        if df is None or df.empty:
            raise ValueError("No se pudo obtener datos del ticker")

        df = calcular_indicadores(df)
        resultado = evaluar_entrada_salida(df)

        if not isinstance(resultado, dict) or "entrada" not in resultado or "salida" not in resultado:
            raise ValueError("evaluar_entrada_salida no devolvió un diccionario válido")

        print(f"{ticker} → Entrada: {resultado['entrada']} | Salida: {resultado['salida']}")
        return resultado

    except Exception as e:
        print(f"❌ Error al analizar {ticker}: {e}")
        return {"entrada": False, "salida": False}

if __name__ == "__main__":
    with open("watchlist.txt") as f:
        tickers = [line.strip() for line in f if line.strip()]
    for t in tickers:
        analizar_ticker(t)
