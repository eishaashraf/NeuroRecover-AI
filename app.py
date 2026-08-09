import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import date, timedelta
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler

# ============================================================
# CONFIG
# ============================================================

st.set_page_config(
    page_title="NeuroRecover AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>
    .main {
        background-color: #f7f9fc;
    }

    .hero {
        padding: 30px;
        border-radius: 18px;
        background: linear-gradient(135deg, #eef4ff, #f8fbff);
        border: 1px solid #dbe6f5;
        margin-bottom: 25px;
    }

    .hero h1 {
        font-size: 42px;
        margin-bottom: 8px;
    }

    .hero p {
        font-size: 18px;
        color: #526071;
    }

    .card {
        padding: 20px;
        border-radius: 15px;
        background: white;
        border: 1px solid #e2e8f0;
        margin-bottom: 15px;
    }

    .insight {
        padding: 20px;
        border-radius: 15px;
        background: #f0f7ff;
        border-left: 5px solid #4f7cff;
        margin-bottom: 15px;
    }

    .warning {
        padding: 18px;
        border-radius: 12px;
        background: #fff8e8;
        border-left: 5px solid #f0ad4e;
    }

    .metric-box {
        padding: 18px;
        border-radius: 14px;
        background: white;
        border: 1px solid #e2e8f0;
        text-align: center;
    }

    .small-text {
        color: #64748b;
        font-size: 14px;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================
# SESSION STATE
# ============================================================

if "records" not in st.session_state:
    st.session_state.records = None

if "checkin_submitted" not in st.session_state:
    st.session_state.checkin_submitted = False


# ============================================================
# DEMO DATA
# ============================================================

def create_demo_data():

    np.random.seed(42)

    days = 14
    dates = [date.today() - timedelta(days=i) for i in range(days - 1, -1, -1)]

    cognitive = np.random.randint(1, 6, days)
    physical = np.random.randint(1, 6, days)
    sleep = np.round(np.random.uniform(5.5, 8.5, days), 1)

    headache = np.clip(
        6 - np.arange(days) * 0.18 + np.random.normal(0, 0.8, days),
        0, 6
    )

    dizziness = np.clip(
        4.5 - np.arange(days) * 0.12 + np.random.normal(0, 0.7, days),
        0, 6
    )

    concentration = np.clip(
        cognitive + np.random.normal(0, 0.8, days),
        0, 6
    )

    fatigue = np.clip(
        5 - (sleep - 6.5) * 0.7 + np.random.normal(0, 0.7, days),
        0, 6
    )

    symptoms = (
        headache
        + dizziness
        + concentration
        + fatigue
    ) / 4

    symptoms = np.clip(symptoms, 0, 6)

    df = pd.DataFrame({
        "Date": dates,
        "Sleep Hours": sleep,
        "Cognitive Load": cognitive,
        "Physical Activity": physical,
        "Headache": np.round(headache, 1),
        "Dizziness": np.round(dizziness, 1),
        "Concentration Difficulty": np.round(concentration, 1),
        "Fatigue": np.round(fatigue, 1),
        "Overall Symptoms": np.round(symptoms, 1)
    })

    return df


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🧠 NeuroRecover AI")

st.sidebar.caption(
    "Personalized concussion recovery monitoring"
)

page = st.sidebar.radio(
    "Navigate",
    [
        "🏠 Home",
        "📝 Daily Check-in",
        "📊 Recovery Dashboard",
        "🤖 AI Insights",
        "🛡️ Safety Center",
        "📚 Resources"
    ]
)

st.sidebar.markdown("---")

if st.sidebar.button("Load Demo Recovery Data"):
    st.session_state.records = create_demo_data()
    st.sidebar.success("Demo data loaded!")

if st.session_state.records is None:
    st.session_state.records = create_demo_data()


df = st.session_state.records.copy()


# ============================================================
# HOME
# ============================================================

if page == "🏠 Home":

    st.markdown("""
    <div class="hero">
        <h1>🧠 NeuroRecover AI</h1>
        <p>
        AI-assisted concussion recovery monitoring with
        personalized and explainable health insights.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.info(
        "NeuroRecover AI is an educational monitoring tool. "
        "It does not diagnose concussion, provide medical clearance, "
        "or replace a healthcare professional."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
        <h3>📝 Track</h3>
        <p>
        Record symptoms, sleep, cognitive activity,
        and physical activity over time.
        </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
        <h3>🤖 Analyze</h3>
        <p>
        Identify personal patterns and trends
        in your recovery data.
        </p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
        <h3>🛡️ Protect</h3>
        <p>
        Use safety-focused, explainable AI
        without diagnostic claims.
        </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### How it works")

    st.progress(25, text="1. Daily Check-in")
    st.progress(50, text="2. Recovery Tracking")
    st.progress(75, text="3. Pattern Analysis")
    st.progress(100, text="4. Explainable Insights")

    st.markdown("---")

    st.markdown("""
    ### 🎯 Our goal

    NeuroRecover AI transforms personal recovery logs into
    understandable patterns involving symptoms, sleep,
    cognitive load, and activity.

    **Track → Analyze → Explain → Support**
    """)


# ============================================================
# DAILY CHECK-IN
# ============================================================

elif page == "📝 Daily Check-in":

    st.title("📝 Daily Recovery Check-in")

    st.caption(
        "Record today's information to build your personal recovery timeline."
    )

    st.markdown(
        "### 🧠 Symptoms"
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        headache = st.slider("Headache", 0, 6, 2)
        dizziness = st.slider("Dizziness / balance", 0, 6, 1)
        nausea = st.slider("Nausea", 0, 6, 0)
        vision = st.slider("Vision problems", 0, 6, 0)

    with col2:
        light_noise = st.slider("Light / noise sensitivity", 0, 6, 1)
        fatigue = st.slider("Fatigue", 0, 6, 2)
        concentration = st.slider(
            "Concentration difficulty", 0, 6, 2
        )
        memory = st.slider("Memory difficulty", 0, 6, 1)

    with col3:
        brain_fog = st.slider("Brain fog", 0, 6, 2)
        irritability = st.slider("Irritability", 0, 6, 1)
        anxiety = st.slider("Anxiety / nervousness", 0, 6, 1)
        sadness = st.slider("Sadness", 0, 6, 0)

    st.markdown("### 😴 Sleep")

    col1, col2 = st.columns(2)

    with col1:
        sleep_hours = st.number_input(
            "Hours of sleep",
            min_value=0.0,
            max_value=14.0,
            value=7.0,
            step=0.5
        )

    with col2:
        sleep_quality = st.slider(
            "Sleep quality",
            1,
            5,
            3
        )

    st.markdown("### ⚡ Daily Activity")

    col1, col2, col3 = st.columns(3)

    with col1:
        cognitive_load = st.slider(
            "Cognitive load",
            1,
            5,
            2,
            help="1 = low, 5 = high"
        )

    with col2:
        physical_activity = st.slider(
            "Physical activity",
            1,
            5,
            2,
            help="1 = very light, 5 = high"
        )

    with col3:
        activity_duration = st.number_input(
            "Activity duration (minutes)",
            0,
            600,
            30
        )

    symptom_change = st.selectbox(
        "How did symptoms respond after activity?",
        [
            "No noticeable change",
            "Improved",
            "Slightly worse",
            "Moderately worse",
            "Much worse"
        ]
    )

    notes = st.text_area(
        "Optional notes",
        placeholder="Describe anything important about today's activities or symptoms..."
    )

    if st.button(
        "💾 Save Today's Check-in",
        type="primary"
    ):

        overall = np.mean([
            headache,
            dizziness,
            nausea,
            vision,
            light_noise,
            fatigue,
            concentration,
            memory,
            brain_fog,
            irritability,
            anxiety,
            sadness
        ])

        new_row = pd.DataFrame([{
            "Date": date.today(),
            "Sleep Hours": sleep_hours,
            "Cognitive Load": cognitive_load,
            "Physical Activity": physical_activity,
            "Headache": headache,
            "Dizziness": dizziness,
            "Concentration Difficulty": concentration,
            "Fatigue": fatigue,
            "Overall Symptoms": round(overall, 2)
        }])

        df = st.session_state.records

        # Replace today's record if it exists
        df = df[df["Date"] != date.today()]

        st.session_state.records = pd.concat(
            [df, new_row],
            ignore_index=True
        ).sort_values("Date")

        st.session_state.checkin_submitted = True

        st.success(
            "✅ Today's recovery check-in has been saved."
        )

        st.info(
            "Your information is used to identify personal trends. "
            "It is not used to diagnose or medically clear you."
        )


# ============================================================
# DASHBOARD
# ============================================================

elif page == "📊 Recovery Dashboard":

    st.title("📊 Recovery Dashboard")

    if len(df) == 0:
        st.warning("No recovery data available.")
        st.stop()

    latest = df.iloc[-1]

    avg_symptoms = df["Overall Symptoms"].mean()
    avg_sleep = df["Sleep Hours"].mean()

    if len(df) >= 7:
        recent_symptoms = df["Overall Symptoms"].tail(7).mean()
        previous_symptoms = df["Overall Symptoms"].head(7).mean()
    else:
        recent_symptoms = avg_symptoms
        previous_symptoms = avg_symptoms

    change = recent_symptoms - previous_symptoms

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Latest Symptoms",
            f"{latest['Overall Symptoms']:.1f}/6"
        )

    with col2:
        st.metric(
            "Average Sleep",
            f"{avg_sleep:.1f} h"
        )

    with col3:
        st.metric(
            "Days Tracked",
            len(df)
        )

    with col4:
        st.metric(
            "Recent Trend",
            f"{change:+.1f}"
        )

    st.markdown("---")

    st.subheader("📈 Symptom Trend")

    fig = px.line(
        df,
        x="Date",
        y="Overall Symptoms",
        markers=True,
        title="Overall reported symptom score"
    )

    fig.update_yaxes(range=[0, 6])

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("😴 Sleep vs Symptoms")

        fig_sleep = px.scatter(
            df,
            x="Sleep Hours",
            y="Overall Symptoms",
            size="Cognitive Load",
            hover_data=["Date"],
            title="Sleep duration and symptom score"
        )

        st.plotly_chart(
            fig_sleep,
            use_container_width=True
        )

    with col2:

        st.subheader("🧠 Cognitive Load vs Symptoms")

        fig_cognitive = px.scatter(
            df,
            x="Cognitive Load",
            y="Overall Symptoms",
            size="Physical Activity",
            hover_data=["Date"],
            title="Cognitive load and symptom score"
        )

        st.plotly_chart(
            fig_cognitive,
            use_container_width=True
        )

    st.subheader("📋 Recovery Data")

    st.dataframe(
        df.sort_values("Date", ascending=False),
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# AI INSIGHTS
# ============================================================

elif page == "🤖 AI Insights":

    st.title("🤖 AI Recovery Insights")

    st.caption(
        "Insights are based on patterns in the logged data — "
        "not medical diagnosis."
    )

    if len(df) < 5:
        st.warning(
            "More data is needed before meaningful personal patterns can be identified."
        )
        st.stop()

    # --------------------------------------------------------
    # Cognitive relationship
    # --------------------------------------------------------

    cognitive_corr = df[
        ["Cognitive Load", "Overall Symptoms"]
    ].corr().iloc[0, 1]

    sleep_corr = df[
        ["Sleep Hours", "Overall Symptoms"]
    ].corr().iloc[0, 1]

    activity_corr = df[
        ["Physical Activity", "Overall Symptoms"]
    ].corr().iloc[0, 1]

    # --------------------------------------------------------
    # ML MODEL
    # --------------------------------------------------------

    features = [
        "Sleep Hours",
        "Cognitive Load",
        "Physical Activity"
    ]

    X = df[features]
    y = df["Overall Symptoms"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_scaled, y)

    importance = pd.DataFrame({
        "Feature": features,
        "Importance": model.feature_importances_
    }).sort_values(
        "Importance",
        ascending=False
    )

    # --------------------------------------------------------
    # INSIGHT 1
    # --------------------------------------------------------

    if cognitive_corr > 0.25:

        st.markdown("""
        <div class="insight">
        <h3>🧠 Pattern detected: Cognitive Load</h3>
        <p>
        Your logged data shows a positive association between
        cognitive load and reported symptom scores.
        </p>
        </div>
        """, unsafe_allow_html=True)

    elif cognitive_corr < -0.25:

        st.markdown("""
        <div class="insight">
        <h3>🧠 Pattern detected: Cognitive Load</h3>
        <p>
        Your recent data shows that higher cognitive-load
        entries have not consistently corresponded with
        higher symptom scores.
        </p>
        </div>
        """, unsafe_allow_html=True)

    else:

        st.markdown("""
        <div class="insight">
        <h3>🧠 Pattern: No strong relationship detected</h3>
        <p>
        Your current dataset does not show a strong relationship
        between cognitive load and symptoms.
        </p>
        </div>
        """, unsafe_allow_html=True)

    # --------------------------------------------------------
    # INSIGHT 2
    # --------------------------------------------------------

    if sleep_corr < -0.25:

        st.markdown("""
        <div class="insight">
        <h3>😴 Pattern detected: Sleep</h3>
        <p>
        Longer sleep duration has tended to coincide with
        lower reported symptom scores in your logged data.
        </p>
        </div>
        """, unsafe_allow_html=True)

    else:

        st.markdown("""
        <div class="card">
        <h3>😴 Sleep Pattern</h3>
        <p>
        No strong sleep-symptom association has been detected
        in the current dataset.
        </p>
        </div>
        """, unsafe_allow_html=True)

    # --------------------------------------------------------
    # INSIGHT 3
    # --------------------------------------------------------

    if activity_corr > 0.25:

        st.markdown("""
        <div class="insight">
        <h3>🏃 Activity Pattern</h3>
        <p>
        Higher activity levels have tended to coincide with
        higher symptom scores in your logged data.
        </p>
        </div>
        """, unsafe_allow_html=True)

    # --------------------------------------------------------
    # ML IMPORTANCE
    # --------------------------------------------------------

    st.subheader("🔍 Model Feature Importance")

    fig = px.bar(
        importance,
        x="Importance",
        y="Feature",
        orientation="h",
        title="Which logged variables contributed most to the model?"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # --------------------------------------------------------
    # EXPLAINABILITY
    # --------------------------------------------------------

    st.subheader("🔎 How was this calculated?")

    st.markdown("""
    <div class="card">

    <b>Data used</b>

    • Sleep duration<br>
    • Cognitive load<br>
    • Physical activity<br>
    • Reported symptom scores

    <br><br>

    <b>Analysis</b>

    NeuroRecover AI combines trend analysis, correlation,
    and a Random Forest regression model to explore patterns
    in the user's logged data.

    <br><br>

    <b>Important limitation</b>

    Statistical association does not establish causation.
    The model does not diagnose concussion, predict medical
    recovery, or provide medical clearance.

    </div>
    """, unsafe_allow_html=True)

    st.warning(
        "⚠️ AI-generated patterns should be discussed with a qualified "
        "healthcare professional when making healthcare decisions."
    )


# ============================================================
# SAFETY CENTER
# ============================================================

elif page == "🛡️ Safety Center":

    st.title("🛡️ Safety Center")

    st.error(
        "NeuroRecover AI does NOT diagnose concussion, determine "
        "medical clearance, or replace professional medical care."
    )

    st.markdown("### What NeuroRecover AI CAN do")

    st.markdown("""
    - Track self-reported symptoms
    - Visualize personal trends
    - Analyze relationships within logged data
    - Provide educational information
    - Help users prepare information for discussion with healthcare professionals
    """)

    st.markdown("### What NeuroRecover AI CANNOT do")

    st.markdown("""
    - Diagnose a concussion
    - Determine whether someone has recovered
    - Provide medical clearance
    - Replace a clinician
    - Guarantee that an activity is medically safe
    - Predict an individual's medical outcome
    """)

    st.markdown("### 🚨 When to seek medical help")

    st.warning("""
    If someone has a possible concussion, worsening symptoms,
    concerning new symptoms, or symptoms that are not improving
    as expected, they should seek appropriate medical evaluation.

    For severe or emergency symptoms, seek emergency medical care
    immediately.
    """)

    st.markdown("### 🔐 Responsible AI principles")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
        <div class="card">
        <h3>Data Minimization</h3>
        Only information needed for recovery monitoring
        is collected.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="card">
        <h3>Explainability</h3>
        Insights show which variables were used and
        acknowledge model limitations.
        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class="card">
        <h3>Human Oversight</h3>
        Healthcare decisions remain with qualified
        healthcare professionals.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="card">
        <h3>No Diagnostic Claims</h3>
        The AI is restricted from declaring diagnosis
        or medical recovery.
        </div>
        """, unsafe_allow_html=True)


# ============================================================
# RESOURCES
# ============================================================

elif page == "📚 Resources":

    st.title("📚 Evidence & Resources")

    st.markdown("""
    ### CDC — Concussion Information

    Centers for Disease Control and Prevention guidance
    covering concussion symptoms, recovery, and return to activity.
    """)

    st.link_button(
        "Open CDC HEADS UP",
        "https://www.cdc.gov/heads-up/"
    )

    st.markdown("---")

    st.markdown("""
    ### International Consensus

    NeuroRecover AI's concept is informed by international
    concussion consensus recommendations, while avoiding
    independent medical diagnosis or clearance.
    """)

    st.link_button(
        "International Consensus Statement",
        "https://bjsm.bmj.com/content/57/11/695"
    )

    st.markdown("---")

    st.markdown("""
    ### 🧠 Research Foundation

    The application focuses on:

    - symptom monitoring
    - sleep
    - cognitive activity
    - physical activity
    - symptom response
    - longitudinal personal trends

    These variables are used for educational monitoring rather
    than clinical diagnosis.
    """)

    st.markdown("---")

    st.info(
        "For the hackathon submission, the final README will contain "
        "the complete research references and responsible-AI methodology."
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "NeuroRecover AI • Hack for Humanity Summer 2026 • "
    "Educational recovery monitoring prototype"
)