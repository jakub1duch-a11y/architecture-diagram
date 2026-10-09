# 🤖 Mermaid Diagram AI Agent

Inteligentný AI agent postavený na [CrewAI](https://crewai.io/) framework, ktorý generuje, upravuje a vylepšuje Mermaid diagramy automaticky.

## 🎯 Funkčnosti

- **📋 Návrh diagramu** - Inteligentnी návrh štruktúry diagramu na základe popisu
- **🔧 Generovanie kódu** - Automatické generovanie syntakticky správneho Mermaid kódu
- **👁️ Recenzia diagramu** - Analýza a vylepšovanie existujúcich diagramov
- **✏️ Úprava diagramu** - Modifikácia diagramov podľa špecifických požiadaviek
- **🔄 Kompletný workflow** - Automatizovaný proces: návrh → generovanie → recenzia

## 🏗️ Architektura Agentov

Agent pozostáva z 4 špecializovaných agentov:

### 1. **Architecture Diagram Architect** 👨‍🏛️
- Navrhuje štruktúru diagramu
- Rozhoduje o type diagramu (flowchart, sequence, class, atď.)
- Identifikuje komponenty a vzťahy

### 2. **Mermaid Syntax Expert** 🔤
- Generuje syntakticky správny Mermaid kód
- Aplikuje styling a best practices
- Zabezpečuje okamžitú renderovateľnosť

### 3. **Diagram Quality Reviewer** ✅
- Overuje korektnosť a jasnosť
- Navrhuje vylepšenia
- Kontroluje dodržiavanie best practices

### 4. **Diagram Editor** ✏️
- Upravuje existujúce diagramy
- Pridáva/odstraňuje/modifikuje prvky
- Zachováva integritu diagramu

## 📋 Inštalácia

### Požiadavky
- Python 3.8+
- OpenAI API kľúč

### Krokmi

1. **Klonujte repozitár**
```bash
git clone https://github.com/jakub1duch-a11y/architecture-diagram.git
cd architecture-diagram
```

2. **Vytvorte virtuálne prostredie**
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# alebo
venv\Scripts\activate  # Windows
```

3. **Inštalujte závislosťi**
```bash
pip install -r requirements.txt
```

4. **Nastavte API kľúč**
```bash
cp .env.example .env
# Otvorte .env a upravte OPENAI_API_KEY
```

## 🚀 Použitie

### Rýchly start

```python
from mermaid_agent import MermaidDiagramAgent

agent = MermaidDiagramAgent()

# Generovať diagram
diagram = agent.generate_diagram(
    "Microservices architecture s API Gateway, Auth Service, Order Service"
)

print(diagram)
```

### Komplexný príklad

```python
from mermaid_agent import MermaidDiagramAgent

agent = MermaidDiagramAgent()

description = """
E-commerce platform s:
- API Gateway
- Auth Service
- Product Service
- Order Service
- Payment Service
- Database per service
- Message queue
"""

# Celý workflow: návrh -> generovanie -> recenzia
result = agent.full_workflow(description)

print("Proposal:", result['proposal'])
print("Code:", result['diagram_code'])
print("Review:", result['review'])
```

## 📚 Metódy

### `propose_diagram(description: str) -> str`
Navrhuje štruktúru diagramu.

```python
proposal = agent.propose_diagram("Cloud infrastructure s VPC a EC2")
```

### `generate_diagram(description: str) -> str`
Generuje kompletný Mermaid kód.

```python
code = agent.generate_diagram("CI/CD pipeline s GitHub a Kubernetes")
```

### `edit_diagram(diagram_code: str, edit_request: str) -> str`
Upravuje existujúci diagram.

```python
updated = agent.edit_diagram(existing_diagram, "Pridaj Payment Service node")
```

### `review_diagram(diagram_code: str, description: str) -> str`
Kontroluje a navrhuje vylepšenia.

```python
review = agent.review_diagram(diagram_code, "Microservices architecture")
```

### `full_workflow(description: str) -> dict`
Automatizovaný proces: návrh → generovanie → recenzia.

```python
result = agent.full_workflow("Váš popis systému")
# result['proposal'], result['diagram_code'], result['review']
```

## 📝 Príklady

Spusťte príklady:

```bash
# Spustite všetky príklady
python examples.py

# Alebo imports konkrétny príklad v kóde
python -c "from examples import example_full_workflow; example_full_workflow()"
```

## 🎨 Podporované typy diagramov

- **Flowchart** - Procesné toky a logika
- **Sequence** - Interakcie medzi komponentami
- **Class** - OOP hierarchie
- **State** - Stavové automaty
- **ER** - Databázové schémy
- **Gantt** - Projekty a časosy
- **A ďalšie...**

## ⚙️ Konfigurácia

### Environment variables

```env
# .env
OPENAI_API_KEY=sk-...
# Voliteľné:
# OPENAI_MODEL=gpt-4  (default: gpt-4)
```

## 🔄 Workflow príklady

### Príklad 1: Jednoduchý diagram
```python
agent = MermaidDiagramAgent()
code = agent.generate_diagram("Simple todo app architecture")
```

### Príklad 2: Úprava diagramu
```python
# Existujúci diagram
diagram = """graph TD
A[User] --> B[Server]
B --> C[Database]"""

# Upraviť ho
updated = agent.edit_diagram(diagram, "Add caching layer between Server and Database")
```

### Príklad 3: Overenie a vylepšenie
```python
# Skontrolovať kvalitu
review = agent.review_diagram(diagram, "E-commerce checkout flow")
```

## 🐛 Riešenie problémov

### OpenAI API kľúč
- Skontrolujte, či je kľúč správne nastavený v `.env`
- Overite kredity na OpenAI účte

### CrewAI chyby
- Nainštalujte najnovšiu verziu: `pip install --upgrade crewai`

### Generovanie trvá dlho
- Normálne trvá 30-60 sekúnd
- Skontrolujte internetové pripojenie

## 📖 Dodatočné zdroje

- [Mermaid dokumentácia](https://mermaid.js.org/)
- [CrewAI dokumentácia](https://docs.crewai.io/)
- [OpenAI API](https://platform.openai.com/docs)

## 📄 Licencia

MIT

## 👤 Autor

Vytvorené pre [`jakub1duch-a11y`](https://github.com/jakub1duch-a11y)

---

**Poznámka:** Agent vyžaduje aktívnu OpenAI API súbscripciu.
