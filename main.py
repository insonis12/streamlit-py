import streamlit as st
import pandas as pd

# Dane budynków
budynki = [
]

# Funkcja do obliczania zapotrzebowania na materiały
def oblicz_zapotrzebowanie(budynek, poziom):
    zapotrzebowanie = {}
    zapotrzebowanie["Drewno"] = budynek["Drewno"] * (budynek["CzynnikDrewna"] ** poziom)
    zapotrzebowanie["Glina"] = budynek["Glina"] * (budynek["CzynnikGliny"] ** poziom)
    zapotrzebowanie["Zelazo"] = budynek["Zelazo"] * (budynek["CzynnikZelaza"] ** poziom)
    zapotrzebowanie["Populacja"] = budynek["Populacja"] * (budynek["CzynnikPopulacji"] ** poziom)
    return zapotrzebowanie

# Interfejs Streamlit
st.title("Symulator zapotrzebowania na materiały budowlane")

# Wybór budynku
budynek_wybrany = st.selectbox("Wybierz budynek:", [b["Nazwa"] for b in budynki])

# Wyszukiwanie wybranego budynku
budynek = next(b for b in budynki if b["Nazwa"] == budynek_wybrany)

# Wybór poziomu budynku
poziom = st.slider(f"Wybierz poziom dla {budynek_wybrany}", budynek["MinPoziom"], budynek["MaxPoziom"], 1)

# Obliczanie zapotrzebowania na materiały
zapotrzebowanie = oblicz_zapotrzebowanie(budynek, poziom)

# Wyświetlanie wyników
st.subheader(f"Zapotrzebowanie na materiały dla {budynek_wybrany} na poziomie {poziom}")
st.write(f"Drewno: {zapotrzebowanie['Drewno']:.2f}")
st.write(f"Glina: {zapotrzebowanie['Glina']:.2f}")
st.write(f"Żelazo: {zapotrzebowanie['Zelazo']:.2f}")
st.write(f"Populacja: {zapotrzebowanie['Populacja']:.2f}")

# Dodanie tabeli dla zapotrzebowania na materiały dla różnych poziomów
tabela_wynikow = []
for p in range(budynek["MinPoziom"], budynek["MaxPoziom"] + 1):
    zapotrzebowanie = oblicz_zapotrzebowanie(budynek, p)
    tabela_wynikow.append({
        "Poziom": p,
        "Drewno": zapotrzebowanie["Drewno"],
        "Glina": zapotrzebowanie["Glina"],
        "Zelazo": zapotrzebowanie["Zelazo"],
        "Populacja": zapotrzebowanie["Populacja"]
    })

df = pd.DataFrame(tabela_wynikow)

# Wyświetlanie tabeli
st.subheader(f"Tabela zapotrzebowania dla {budynek_wybrany}")
st.dataframe(df)
