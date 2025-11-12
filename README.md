# 🎓 Predicting Student Course Engagement Using AI

This project applies the **AI Development Workflow** (problem definition → data → model → evaluation → deployment) to predict **student course engagement** in a university setting. It follows the CRISP-DM framework and includes ethical and practical analysis.

---

## 🧠 Overview

Student engagement directly impacts academic success. This project demonstrates how AI can be applied to predict engagement levels using behavioral, academic, and contextual data. The goal is to support universities in improving teaching strategies and course design.

**Model Performance (Real Results):**
- **Accuracy:** 93%
- **Precision (Disengaged Students):** 0.79
- **Recall (Disengaged Students):** 0.38
- **F1-score:** 0.51

These metrics show that the model performs well overall, but recall for disengaged students is an area for improvement.

---

## 🧩 Project Structure

```
ai-workflow-assignment/
│
├── data/
│   ├── raw/                # Original data (student_engagement.csv)
│   └── processed/          # Cleaned/prepared data
│
├── notebooks/
│   ├── 00-generate-data.ipynb
│   ├── 01-data-exploration.ipynb
│   ├── 02-model-training.ipynb
│   └── 03-evaluation.ipynb
│
├── src/
│   ├── data/preprocess.py
│   ├── models/train_model.py
│   ├── eval/evaluate.py
│   └── app/app.py
│
├── reports/
│   └── final_report.md
│
├── diagrams/
│   └── workflow_diagram.svg
│
├── models/                 # Saved trained models
├── artifacts/              # Generated metrics, plots, etc.
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## 🧰 Installation

```bash
# Clone the repository
git clone https://github.com/<your-username>/ai-workflow-assignment.git
cd ai-workflow-assignment

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate (on Windows)

# Install dependencies
pip install -r requirements.txt
```

---

## 🚀 Usage

### 1. Generate synthetic dataset
```bash
python notebooks/00-generate-data.ipynb
```

### 2. Train the model
```bash
python src/models/train_model.py
```

### 3. Evaluate the model
```bash
python src/eval/evaluate.py
```

### 4. Run the prediction app
```bash
python src/app/app.py
```

---

## 📊 Example Features

| Feature | Description |
|----------|--------------|
| `avg_class_length` | Average duration of classes |
| `teacher_feedback_score` | Instructor rating |
| `num_assignments_due` | Weekly assignments |
| `previous_engagement` | Engagement trend from previous weeks |
| `engagement_level` | Target variable (0 = low, 1 = high) |

---

## ⚖️ Ethical Considerations

- Respect student data privacy (e.g., anonymization).
- Prevent algorithmic bias (balance dataset across majors, gender, etc.).
- Ensure transparency in predictions for educators and students.

---

## 📈 Evaluation Metrics

- **Accuracy:** 93%
- **Precision:** 0.79
- **Recall:** 0.38
- **F1-Score:** 0.51

---

## 🧩 AI Workflow Diagram

![Workflow Diagram](diagrams/workflow_diagram.svg)

---

## 👩‍💻 Author

- **Bikila Keneni**

---

## 🪄 License

MIT License © 2025
