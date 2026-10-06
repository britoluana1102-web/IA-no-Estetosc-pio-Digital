"""
CardioIA - Fase 2 - Parte 1
Lê as frases de sintomas, identifica expressões do mapa de conhecimento
e sugere um possível diagnóstico (apoio à decisão, NÃO substitui um médico).
"""
import csv
import re
import unicodedata
from collections import defaultdict
from pathlib import Path

BASE = Path(__file__).parent
ARQ_FRASES = BASE / "frases_sintomas.txt"
ARQ_MAPA = BASE / "mapa_conhecimento.csv"


def normalizar(texto: str) -> str:
    """minúsculas, sem acentos e sem pontuação, para comparar textos."""
    texto = unicodedata.normalize("NFD", texto.lower())
    texto = "".join(c for c in texto if unicodedata.category(c) != "Mn")
    texto = re.sub(r"[^a-z0-9\s]", " ", texto)
    return re.sub(r"\s+", " ", texto).strip()


def carregar_frases(caminho):
    with open(caminho, encoding="utf-8") as f:
        return [linha.strip() for linha in f if linha.strip()]


def carregar_mapa(caminho):
    """Retorna {doença: set(expressões normalizadas)}."""
    mapa = defaultdict(set)
    with open(caminho, encoding="utf-8", newline="") as f:
        for linha in csv.DictReader(f):
            doenca = linha["Doença Associada"].strip()
            for col in ("Sintoma 1", "Sintoma 2"):
                if linha[col].strip():
                    mapa[doenca].add(normalizar(linha[col]))
    return mapa


def diagnosticar(frase, mapa):
    """Conta quantas expressões de cada doença aparecem na frase."""
    frase_norm = normalizar(frase)
    resultado = {}
    for doenca, expressoes in mapa.items():
        achadas = sorted(e for e in expressoes if e in frase_norm)
        if achadas:
            resultado[doenca] = achadas
    return resultado


def main():
    frases = carregar_frases(ARQ_FRASES)
    mapa = carregar_mapa(ARQ_MAPA)

    for i, frase in enumerate(frases, start=1):
        resultado = diagnosticar(frase, mapa)
        print(f"\nPaciente {i}: {frase}")
        if not resultado:
            print("  -> Nenhum sintoma reconhecido. Encaminhar para avaliação médica.")
            continue

        melhor = max(len(v) for v in resultado.values())
        sugeridas = [d for d, v in resultado.items() if len(v) == melhor]

        sintomas = sorted({s for v in resultado.values() for s in v})
        print(f"  Sintomas identificados: {', '.join(sintomas)}")
        print("  Pontuação por doença: " +
              "; ".join(f"{d} ({len(v)})" for d, v in
                        sorted(resultado.items(), key=lambda x: -len(x[1]))))
        print(f"  -> Diagnóstico sugerido: {' / '.join(sugeridas)}")


if __name__ == "__main__":
    main()
