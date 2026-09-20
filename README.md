# 💧 Consumo de Água – Classificador de Perfil de Consumo

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/Licença-MIT-blue?style=for-the-badge)
![Saneamento](https://img.shields.io/badge/Tema-Sustentabilidade%20🌱-2E8B57?style=for-the-badge)

## 🎯 Objetivo

Programa desenvolvido para uma campanha de **conscientização ambiental** promovida pela companhia de saneamento local. O sistema solicita o tipo de imóvel e o consumo mensal de água e, com base em regras de negócio pré-definidas, classifica o perfil de consumo e exibe um **alerta educativo** ao morador, incentivando o uso consciente da água. 🌎💧

## 📏 Regras de negócio

| Tipo de imóvel | Condição de consumo | Mensagem exibida |
|---|---|---|
| Comercial | Qualquer valor | 🏢 Tarifa comercial aplicada – consulte o plano corporativo. |
| Apartamento | Menor que 10 m³ | 🌱 Consumo econômico – excelente controle de água! |
| Apartamento | 10 m³ ou mais | 💧 Consumo moderado – dentro do padrão residencial. |
| Casa | Até 25 m³ | 💧 Consumo moderado – dentro do padrão residencial. |
| Casa | Acima de 25 m³ | 🚨 Consumo excessivo – adote medidas de economia e verifique vazamentos. |

## 🐍 Tecnologias e conceitos utilizados

- **Python 3** (nenhuma biblioteca externa é necessária).
- Conceitos aplicados: `input()`, conversão de tipos com `float()`, estrutura condicional `if / elif / else` e `print()`.
- Código comentado no modelo **"Ato por Ato"**, explicando o programa na ordem real em que ele é executado (do Ato 0 ao Ato 4), e não apenas na ordem das linhas do arquivo.

## ▶️ Como executar o programa

1. Clone este repositório:
   ```bash
   git clone https://github.com/SEU-USUARIO/consumo-agua.git
   ```
2. Acesse a pasta do projeto:
   ```bash
   cd consumo-agua
   ```
3. Execute o script com Python 3:
   ```bash
   python3 app.py
   ```
4. Informe o tipo de imóvel e o consumo mensal quando solicitado, e veja o resultado da classificação. ✅

## 📁 Estrutura do projeto

```
consumo-agua/
├── app.py        # Script principal com a lógica de classificação
└── README.md     # Documentação do projeto
```

## 🚀 Melhorias futuras

- Validar a entrada do consumo para evitar erro caso o usuário digite um texto no lugar de um número.
- Permitir a classificação de vários imóveis em sequência, sem precisar reiniciar o programa.
- Registrar o histórico de consultas em um arquivo para acompanhamento posterior.

## 👨‍💻 Autor

Projeto desenvolvido como atividade prática de lógica de programação em Python, com foco em conscientização ambiental. 💙

---

⭐ Se este projeto foi útil, deixe uma estrela no repositório!
