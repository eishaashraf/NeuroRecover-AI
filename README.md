# 🧠 NeuroRecover AI

### AI-Assisted Concussion Recovery Monitoring

NeuroRecover AI is a web-based health technology prototype designed to help individuals monitor self-reported concussion-related symptoms, sleep, cognitive load, and physical activity over time.

The system uses data visualization, statistical pattern analysis, and machine learning to identify personalized trends in a user's recovery logs.

> ⚠️ NeuroRecover AI is an educational monitoring tool. It does not diagnose concussion, determine medical clearance, or replace professional healthcare.

---

## 🎯 Problem

Concussion recovery can involve changing physical, cognitive, emotional, and sleep-related symptoms.

Individuals may find it difficult to understand how their symptoms change over time or how their own activity and sleep patterns relate to their reported symptoms.

NeuroRecover AI provides a simple way to record recovery information and transform those records into understandable personal patterns.

---

## 💡 Solution

NeuroRecover AI follows:

**Track → Analyze → Explain → Support**

Users can:

- Record daily symptoms
- Track sleep
- Record cognitive load
- Record physical activity
- Visualize symptom trends
- Explore sleep/activity relationships
- Receive explainable AI-assisted insights
- Review safety information and evidence resources

---

## 🤖 AI / Machine Learning

The application combines:

- Statistical correlation analysis
- Trend analysis
- Random Forest regression
- Feature importance analysis

The model analyzes:

- Sleep duration
- Cognitive load
- Physical activity
- Reported symptom scores

The system focuses on identifying **personal patterns**, rather than making medical diagnoses.

Example:

> Higher cognitive-load entries have been associated with higher reported symptom scores in the user's logged data.

This is presented as an association rather than a causal or clinical conclusion.

---

## 🛡️ Responsible AI

NeuroRecover AI was designed with safety and responsible AI principles in mind.

### Data minimization
The prototype collects only information necessary for recovery monitoring.

### Explainability
AI insights identify the variables and analytical approach used.

### Human oversight
Healthcare decisions remain with qualified healthcare professionals.

### No diagnosis
The system does not diagnose concussion or determine recovery status.

### No medical clearance
The system does not determine whether a user is medically ready for sports, school, work, or other activities.

### Limitations
Statistical associations do not establish causation, and the prototype is not a clinical decision-support system.

---

## 🧠 Main Features

### Daily Check-in
Users can record:

- Headache
- Dizziness
- Nausea
- Vision problems
- Light/noise sensitivity
- Fatigue
- Concentration difficulty
- Memory difficulty
- Brain fog
- Irritability
- Anxiety
- Sadness
- Sleep duration
- Sleep quality
- Cognitive load
- Physical activity
- Activity duration

### Recovery Dashboard

Provides:

- Symptom trends
- Sleep vs symptom visualization
- Cognitive load vs symptom visualization
- Recovery data table
- Recent trend metrics

### AI Recovery Insights

Provides:

- Cognitive-load pattern analysis
- Sleep-pattern analysis
- Activity-pattern analysis
- Machine-learning feature importance
- Explainability information

### Safety Center

Clearly explains:

- What the system can do
- What it cannot do
- When professional medical evaluation may be appropriate
- Responsible AI principles

---

## 🏗️ Technology Stack

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Plotly
- GitHub
- Render

---

## 📁 Project Structure

```text
NeuroRecover-AI/
│
├── app.py
├── requirements.txt
├── README.md
└── venv/