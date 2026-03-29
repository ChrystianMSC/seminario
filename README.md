# 🐾 Felimons - Pytest & Plugins Demo

Este projeto demonstra o poder do ecossistema `pytest` através de um Trading Card Game (TCG) de gatos mágicos. 

## 🛠️ Setup do Ambiente
Execute no terminal do PyCharm para garantir que todas as ferramentas estão presentes:

```powershell
pip install pytest pytest-sugar pytest-cov pytest-mock pytest-clarity requests pytest-xdist
```

---

## 🚀 Script de Comandos para o Seminário
```powershell
# Roda desativando os plugins visuais (Sugar e Clarity)
pytest -p no:sugar -p no:clarity test_felimons.py
```

```powershell
# O Sugar ativa automaticamente, mas aqui garantimos o foco nele
pytest test_felimons.py
```

```powershell
# Se um assert de texto falhar, o Clarity detalha a diferença
pytest -p no:sugar -vv test_felimons.py
```

```powershell
# Roda apenas os testes que simulam a API de nomes mágicos
pytest test_felimons.py -k "magical_name" -v
```

```powershell
# Relatório resumido com linhas faltando
pytest --cov=main --cov-report=term-missing test_felimons.py

# Gerar relatório visual (HTML)
pytest --cov=main --cov-report=html test_felimons.py
```

---

## 📚 Tabela de Referência de Plugins

| Plugin | O que ele resolve? |
| :--- | :--- |
| **pytest-sugar** | **Estética:** Troca o console estático por uma interface fluida. |
| **pytest-clarity** | **Legibilidade:** Diff de erros de comparação muito mais amigável. |
| **pytest-mock** | **Isolamento:** Remove dependências externas (APIs, DBs). |
| **pytest-cov** | **Métricas:** Mede o quanto do seu código está realmente testado. |
---
