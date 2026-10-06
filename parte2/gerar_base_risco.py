"""
CardioIA - Fase 2 - Parte 2
Transforma o dataset da Fase 1 (tabela de pacientes) em frases em linguagem natural
rotuladas como "alto risco" ou "baixo risco".
Pacientes de risco "Moderado" ficam de fora, pois a atividade usa só duas classes.
"""
import random
from pathlib import Path

import pandas as pd

BASE = Path(__file__).parent
random.seed(42)

df = pd.read_csv(BASE.parent / "dados_fase1" / "dados_pacientes_cardiacos.csv")
df = df[df["risco_cardiaco"].isin(["Alto", "Baixo"])]


def montar_frase(p):
    sexo = "homem" if p["sexo"] == "M" else "mulher"

    fatores = []
    if p["idade"] > 55:
        fatores.append("tenho mais de 55 anos")
    if p["pressao_sistolica"] > 140:
        fatores.append("tenho pressão alta")
    if p["colesterol_total"] > 240:
        fatores.append("tenho colesterol alto")
    if p["tabagismo"] == "Sim":
        fatores.append("fumo")
    if p["diabetes"] == "Sim":
        fatores.append("tenho diabetes")
    if p["historico_familiar_cardiaco"] == "Sim":
        fatores.append("tenho histórico de doença do coração na família")

    sintomas = []
    if p["dor_no_peito"] == "Sim":
        sintomas.append("dor no peito")
    if p["falta_de_ar"] == "Sim":
        sintomas.append("falta de ar")
    if p["palpitacoes"] == "Sim":
        sintomas.append("palpitações")
    if p["fadiga"] == "Sim":
        sintomas.append("cansaço")

    random.shuffle(fatores)
    partes = [f"sou {sexo}"] + fatores
    frase = ", ".join(partes)
    if sintomas:
        frase += " e sinto " + " e ".join(sintomas)
    elif not fatores:
        frase += " e não tenho sintomas nem fatores de risco"
    return frase[0].upper() + frase[1:] + "."


saida = pd.DataFrame({
    "frase": df.apply(montar_frase, axis=1),
    "situacao": df["risco_cardiaco"].map({"Alto": "alto risco", "Baixo": "baixo risco"}),
})
saida = saida.sample(frac=1, random_state=42).reset_index(drop=True)
saida.to_csv(BASE / "base_risco.csv", index=False, encoding="utf-8")
print(saida["situacao"].value_counts())
print(saida.head(8).to_string())
