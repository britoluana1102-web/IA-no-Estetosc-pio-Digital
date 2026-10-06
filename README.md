# IA-no-Estetoscópio-Digital
# CardioIA – Fase 2: Diagnóstico Automatizado (IA no Estetoscópio Digital)

Projeto acadêmico da FIAP – curso de Inteligência Artificial.

## Integrantes
| Nome completo | RM |
|---|---|
| _Luana Brito da Silva_ | _566632_ |

## Vídeo de demonstração
Link (YouTube, não listado): _colar aqui o link_

## Sobre o projeto
Nesta fase simulamos um sistema simples de apoio ao diagnóstico, em duas partes:

1. **Parte 1:** um programa em Python lê relatos de pacientes, identifica os sintomas e sugere um possível diagnóstico.
2. **Parte 2:** um modelo de Machine Learning classifica frases de sintomas em **alto risco** ou **baixo risco**.

> Projeto de estudo com dados simulados. Não substitui avaliação médica.

## Estrutura do repositório
```
cardioia-fase2/
├── README.md
├── dados_fase1/
│   ├── dados_pacientes_cardiacos.csv   # dataset da Fase 1 (150 pacientes)
│   └── gerar_dataset.py
├── parte1/
│   ├── frases_sintomas.txt             # 10 frases de pacientes
│   ├── mapa_conhecimento.csv           # sintomas -> doenças
│   └── extracao_diagnostico.py         # código da Parte 1
└── parte2/
    ├── gerar_base_risco.py             # cria as frases a partir do dataset da Fase 1
    ├── base_risco.csv                  # frases com rótulo de risco
    └── classificador_risco.ipynb       # código da Parte 2
```

## Parte 1 – Sintomas e diagnóstico sugerido
- `frases_sintomas.txt`: 10 frases simulando relatos (o que o paciente sente, desde quando e como atrapalha a rotina).
- `mapa_conhecimento.csv`: tabela com as colunas *Sintoma 1 | Sintoma 2 | Doença Associada*. Cobre Infarto, Angina, Insuficiência Cardíaca, Arritmia, Hipertensão, Doença Arterial Periférica e Pericardite.
- `extracao_diagnostico.py`: lê as frases, procura no mapa as expressões de sintomas e sugere a doença com mais sintomas encontrados.

Para executar:
```bash
cd parte1
python extracao_diagnostico.py
```

## Parte 2 – Classificador de risco
- `base_risco.csv`: 69 frases no formato `frase,situacao`, criadas a partir do dataset da Fase 1 (pacientes de risco "Moderado" ficaram de fora). São 51 de baixo risco e 18 de alto risco.
- `classificador_risco.ipynb`: transforma as frases em números com **TF-IDF**, treina uma **Regressão Logística** (Scikit-learn) e avalia o resultado com acurácia, relatório de classificação e matriz de confusão.

Para executar:
```bash
pip install pandas numpy matplotlib scikit-learn jupyter
cd parte2
jupyter notebook classificador_risco.ipynb
```

### Resultados
- Acurácia de cerca de **89%** no teste (18 frases).
- O modelo acertou todos os casos de alto risco do teste.

### Limitações observadas
- A base é pequena e tem mais frases de baixo risco do que de alto risco.
- Os rótulos vêm de uma regra simples criada na Fase 1, não de um médico.
- O modelo associou a palavra "mulher" a baixo risco por acaso, o que é um possível viés.
- A frase "Sou mulher e sinto dor no peito e falta de ar" foi classificada como baixo risco, o que seria um erro grave em uma triagem real.

A análise completa está no final do notebook.

## Tecnologias
Python, pandas, numpy, matplotlib, scikit-learn e Jupyter Notebook.
