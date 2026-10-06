"""
CardioIA - Fase 1: Geração de dataset simulado de pacientes cardíacos.
"""

import numpy as np
import pandas as pd

np.random.seed(42)
N = 150  # número de pacientes simulados

# --- Variáveis demográficas ---
idade = np.random.randint(29, 80, size=N)
sexo = np.random.choice(["M", "F"], size=N)

# --- Variáveis clínicas ---
pressao_sistolica = np.random.normal(130, 18, size=N).round(0).clip(90, 200).astype(int)
pressao_diastolica = np.random.normal(82, 12, size=N).round(0).clip(55, 130).astype(int)
colesterol_total = np.random.normal(210, 40, size=N).round(0).clip(120, 350).astype(int)
frequencia_cardiaca = np.random.normal(75, 12, size=N).round(0).clip(45, 130).astype(int)
glicemia_jejum = np.random.normal(100, 25, size=N).round(0).clip(65, 250).astype(int)
imc = np.random.normal(27, 4.5, size=N).round(1).clip(16, 45)

# --- Histórico / hábitos ---
historico_familiar = np.random.choice(["Sim", "Não"], size=N, p=[0.35, 0.65])
tabagismo = np.random.choice(["Sim", "Não"], size=N, p=[0.28, 0.72])
diabetes = np.random.choice(["Sim", "Não"], size=N, p=[0.22, 0.78])
sedentarismo = np.random.choice(["Sim", "Não"], size=N, p=[0.45, 0.55])

# --- Sintomas relatados ---
dor_no_peito = np.random.choice(["Sim", "Não"], size=N, p=[0.30, 0.70])
falta_de_ar = np.random.choice(["Sim", "Não"], size=N, p=[0.25, 0.75])
palpitacoes = np.random.choice(["Sim", "Não"], size=N, p=[0.20, 0.80])
fadiga = np.random.choice(["Sim", "Não"], size=N, p=[0.33, 0.67])

# --- Classificação de risco (variável alvo simplificada, baseada em regras) ---
score = (
    (idade > 55).astype(int)
    + (pressao_sistolica > 140).astype(int)
    + (colesterol_total > 240).astype(int)
    + (tabagismo == "Sim").astype(int)
    + (diabetes == "Sim").astype(int)
    + (dor_no_peito == "Sim").astype(int)
    + (historico_familiar == "Sim").astype(int)
)
risco_cardiaco = np.where(score >= 4, "Alto", np.where(score >= 2, "Moderado", "Baixo"))

df = pd.DataFrame({
    "id_paciente": [f"P{str(i+1).zfill(4)}" for i in range(N)],
    "idade": idade,
    "sexo": sexo,
    "pressao_sistolica": pressao_sistolica,
    "pressao_diastolica": pressao_diastolica,
    "colesterol_total": colesterol_total,
    "frequencia_cardiaca": frequencia_cardiaca,
    "glicemia_jejum": glicemia_jejum,
    "imc": imc,
    "historico_familiar_cardiaco": historico_familiar,
    "tabagismo": tabagismo,
    "diabetes": diabetes,
    "sedentarismo": sedentarismo,
    "dor_no_peito": dor_no_peito,
    "falta_de_ar": falta_de_ar,
    "palpitacoes": palpitacoes,
    "fadiga": fadiga,
    "risco_cardiaco": risco_cardiaco,
})

df.to_csv("dados_pacientes_cardiacos.csv", index=False, encoding="utf-8")
print(f"Dataset gerado com {len(df)} linhas e {len(df.columns)} colunas.")
print(df.head())