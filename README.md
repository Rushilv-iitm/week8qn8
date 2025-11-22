# Healthcare Patient Satisfaction – 2024 Quarterly Analysis

**Author / Contact:** 23f2000060@ds.study.iitm.ac.in  

This repository contains an LLM-assisted analysis of a healthcare company's **patient satisfaction score** across the four quarters of 2024, compared against an **industry benchmark target**.

We used an LLM (ChatGPT / Jules / Codex-style assistant) to help:
- Design the analysis approach
- Generate Python code
- Suggest visualization types
- Structure this data story

---

## 1. Dataset

**Quarterly Patient Satisfaction Scores – 2024**

| Quarter | Patient Satisfaction Score |
|---------|----------------------------|
| Q1      | 0.11                       |
| Q2      | 1.29                       |
| Q3      | 4.33                       |
| Q4      | 7.59                       |

- **Average (2024): 3.33**  
- **Industry Target: 4.5**

The data shows a strong upward trend across the year, but the **current average of 3.33 is still below the industry benchmark of 4.5**.

---

## 2. Analysis Code

The main analysis is implemented in [`analysis.py`](analysis.py).

It:

1. Loads the data from `data.csv`
2. Computes the average satisfaction score
3. Compares it with the industry target
4. Generates two visualizations:
   - `quarterly_trend.png` – line chart of satisfaction over quarters
   - `quarterly_vs_target.png` – bar chart vs. benchmark line

Python environment assumptions:
- Python 3.x
- `pandas`
- `matplotlib`

Run:

```bash
pip install pandas matplotlib
python analysis.py
