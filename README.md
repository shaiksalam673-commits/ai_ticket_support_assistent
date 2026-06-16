# AI-Powered Support Ticket Analytics System

## Overview

This project is an AI-powered support ticket analytics system built for the AI Engineer Assessment. The system ingests customer support ticket data, enables natural language querying using a Large Language Model (LLM), detects anomalies in support operations, and provides an interactive Streamlit-based user interface.

The application allows users to:

* Query support ticket data using natural language.
* Analyze ticket statistics and agent performance.
* Detect operational anomalies.
* Explore ticket datasets through an intuitive dashboard.

---

## Features

### Natural Language Querying

Users can ask questions such as:

* How many tickets are currently open?
* Which agent resolved the most tickets?
* What is the average customer rating for Technical tickets?
* Show all Critical tickets that remain unresolved.

The system uses the Groq API with Llama 3 to convert natural language questions into Pandas expressions and execute them against the dataset.

---

### Anomaly Detection

The system automatically identifies:

#### Long Resolution Time Tickets

Tickets whose resolution time exceeds:

Mean Resolution Time + 2 × Standard Deviation

#### Critical Unresolved Tickets

Critical-priority tickets that have not yet been resolved.

#### Low Customer Satisfaction Tickets

Tickets with customer ratings less than or equal to 2.

---

### Dataset Exploration

Users can:

* View dataset records
* Inspect ticket details
* Explore support metrics

---

## System Architecture

```text
User
 │
 ▼
Streamlit Interface
 │
 ▼
Query Engine
 │
 ▼
Groq LLM (Llama 3)
 │
 ▼
Generated Pandas Query
 │
 ▼
Pandas DataFrame
 │
 ▼
Results
```

Anomaly detection operates directly on the Pandas DataFrame and presents findings through the Streamlit dashboard.

---

## Project Structure

```text
ai-support-assistant/

│
├── data/
│   └── support_tickets.xlsx
│
├── src/
│   ├── data_loader.py
│   ├── llm.py
│   ├── query_engine.py
│   ├── anomaly_detector.py
│
├── app.py
├── requirements.txt
├── README.md
├── .env
└── .gitignore
```

---

## Technologies Used

| Component             | Technology    |
| --------------------- | ------------- |
| Language              | Python        |
| UI                    | Streamlit     |
| Data Processing       | Pandas        |
| LLM                   | Groq Llama 3  |
| Environment Variables | python-dotenv |
| Dataset Format        | Excel (.xlsx) |

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd ai-support-assistant
```

### Create Virtual Environment

Linux/Mac:

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Setup

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Get a free API key from:

https://console.groq.com

---

## Running the Application

Start the application with a single command:

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

---

## Example Queries

### Query 1

Input:

```text
How many tickets are currently open?
```

Output:

```text
43
```

---

### Query 2

Input:

```text
Which agent has the lowest average customer rating?
```

Output:

```text
AGT-07
```

---

### Query 3

Input:

```text
What is the average customer rating for Technical tickets?
```

Output:

```text
3.9
```

---

## API/LLM Workflow

1. User enters a natural language question.
2. The question is sent to the Groq LLM.
3. The LLM converts the question into a valid Pandas expression.
4. The expression is executed against the DataFrame.
5. Results are displayed in the Streamlit interface.

---

## Anomaly Detection Logic

### Long Resolution Time

```python
resolution_time > mean + 2 * standard_deviation
```

### Critical Unresolved Tickets

```python
priority == "Critical" and status != "Resolved"
```

### Low Customer Ratings

```python
customer_rating <= 2
```

---

## Assumptions

* Dataset schema remains consistent.
* Groq API key is available.
* The dataset is stored locally in the data directory.
* Natural language queries are related to the provided dataset.

---

## Known Limitations

* LLM-generated queries may occasionally require prompt refinement.
* Query execution currently uses controlled Pandas expressions.
* The application is designed for a single dataset.

---

## Future Improvements

* SQL query generation instead of direct Pandas expressions.
* Docker containerization.
* Role-based authentication.
* Advanced anomaly detection using machine learning.
* Visualization dashboards with Plotly.
* Multi-dataset support.

---

## Author

Shaik Salam


