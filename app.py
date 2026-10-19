import streamlit as st
import pandas as pd
import joblib


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Student Performance AI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# LOAD MODEL
# ============================================================

@st.cache_resource
def load_model():
    return joblib.load("models/final_model.pkl")


model = load_model()


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #f8fafc 0%,
        #eef4ff 50%,
        #f8fafc 100%
    );
}

.block-container {
    max-width: 1250px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

section[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #0f172a 0%,
        #172554 100%
    );
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

section[data-testid="stSidebar"] .stRadio label {
    padding: 8px 5px;
    border-radius: 8px;
}

.hero {
    background: linear-gradient(
        135deg,
        #1d4ed8,
        #2563eb,
        #4f46e5
    );
    padding: 35px 40px;
    border-radius: 24px;
    color: white;
    margin-bottom: 28px;
    box-shadow: 0 15px 35px rgba(37, 99, 235, 0.20);
}

.hero-title {
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 8px;
}

.hero-subtitle {
    font-size: 17px;
    opacity: 0.90;
    line-height: 1.6;
}

.hero-badge {
    display: inline-block;
    margin-top: 18px;
    padding: 7px 14px;
    border-radius: 50px;
    background: rgba(255,255,255,0.15);
    font-size: 13px;
    font-weight: 600;
}

.section-title {
    font-size: 25px;
    font-weight: 750;
    color: #0f172a;
    margin-top: 10px;
    margin-bottom: 5px;
}

.section-subtitle {
    color: #64748b;
    margin-bottom: 18px;
}

.stat-card {
    background: rgba(255,255,255,0.90);
    border: 1px solid #e2e8f0;
    border-radius: 16px;
    padding: 20px;
    text-align: center;
    box-shadow: 0 5px 18px rgba(15,23,42,0.05);
    min-height: 115px;
}

.stat-number {
    font-size: 28px;
    font-weight: 800;
    color: #1d4ed8;
}

.stat-label {
    font-size: 13px;
    color: #64748b;
    margin-top: 5px;
}

.input-card {
    background: rgba(255,255,255,0.85);
    border: 1px solid #e2e8f0;
    border-radius: 18px;
    padding: 20px;
    margin-bottom: 20px;
    box-shadow: 0 4px 15px rgba(15,23,42,0.04);
}

.result-card {
    background: white;
    border-radius: 24px;
    padding: 35px;
    margin-top: 25px;
    border: 2px solid #2563eb;
    box-shadow: 0 15px 40px rgba(37,99,235,0.14);
    text-align: center;
}

.result-label {
    color: #64748b;
    font-size: 16px;
    font-weight: 600;
}

.result-score {
    color: #2563eb;
    font-size: 64px;
    line-height: 1.1;
    font-weight: 850;
    margin: 8px 0;
}

.result-category {
    display: inline-block;
    padding: 8px 18px;
    border-radius: 50px;
    background: #eff6ff;
    color: #1d4ed8;
    font-weight: 700;
    margin-top: 8px;
}

.result-secondary {
    color: #64748b;
    margin-top: 14px;
    font-size: 14px;
}

.gauge-container {
    margin: 25px auto 10px auto;
    max-width: 700px;
    text-align: left;
}

.gauge-labels {
    display: flex;
    justify-content: space-between;
    color: #64748b;
    font-size: 12px;
    margin-bottom: 7px;
}

.gauge {
    height: 15px;
    width: 100%;
    border-radius: 20px;
    background: linear-gradient(
        90deg,
        #ef4444 0%,
        #f97316 25%,
        #eab308 50%,
        #22c55e 75%,
        #16a34a 100%
    );
    position: relative;
}

.gauge-marker {
    position: absolute;
    top: -6px;
    width: 26px;
    height: 26px;
    border-radius: 50%;
    background: white;
    border: 4px solid #1d4ed8;
    box-shadow: 0 3px 10px rgba(0,0,0,0.2);
}

.insight-card {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 16px;
    padding: 20px;
    height: 100%;
    box-shadow: 0 5px 18px rgba(15,23,42,0.04);
}

.insight-title {
    font-weight: 700;
    font-size: 16px;
    color: #0f172a;
    margin-bottom: 7px;
}

.insight-value {
    font-size: 24px;
    font-weight: 800;
    color: #2563eb;
}

.insight-text {
    color: #64748b;
    font-size: 13px;
    margin-top: 5px;
}

.about-card {
    background: white;
    padding: 25px;
    border-radius: 18px;
    border: 1px solid #e2e8f0;
    height: 100%;
    box-shadow: 0 5px 18px rgba(15,23,42,0.04);
}

.stButton > button {
    border-radius: 12px;
    height: 52px;
    font-size: 16px;
    font-weight: 700;
    border: none;
}

.footer {
    text-align: center;
    color: #94a3b8;
    font-size: 13px;
    margin-top: 50px;
    padding-top: 25px;
    border-top: 1px solid #e2e8f0;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.html("""
    <div style="
        font-size:28px;
        font-weight:800;
        margin-bottom:5px;
    ">
        🎓 Student AI
    </div>

    <div style="
        font-size:13px;
        opacity:0.75;
        margin-bottom:25px;
    ">
        Machine Learning Portfolio
    </div>
    """)

    page = st.radio(
        "Navigation",
        [
            "🏠 Prediction Dashboard",
            "🤖 About the Model"
        ]
    )

    st.markdown("---")

    st.markdown("### 🚀 Project")

    st.caption(
        "An end-to-end machine learning application "
        "that predicts a student's final academic grade."
    )

    st.markdown("---")

    st.caption(
        "Python • Pandas • Scikit-learn • Streamlit"
    )


# ============================================================
# PREDICTION DASHBOARD
# ============================================================

if page == "🏠 Prediction Dashboard":

    # --------------------------------------------------------
    # HERO
    # --------------------------------------------------------

    st.html("""
    <div class="hero">

        <div class="hero-title">
            🎓 Student Performance AI
        </div>

        <div class="hero-subtitle">
            Predict a student's final academic performance
            using a trained machine learning pipeline.
        </div>

        <div class="hero-badge">
            ⚡ 32 Features &nbsp; • &nbsp;
            🤖 Machine Learning &nbsp; • &nbsp;
            📊 G3 Prediction
        </div>

    </div>
    """)


    # --------------------------------------------------------
    # MODEL OVERVIEW
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">📊 Model Overview</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Key information about the prediction system.'
        '</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.html("""
        <div class="stat-card">
            <div class="stat-number">32</div>
            <div class="stat-label">Input Features</div>
        </div>
        """)

    with col2:
        st.html("""
        <div class="stat-card">
            <div class="stat-number">G3</div>
            <div class="stat-label">Prediction Target</div>
        </div>
        """)

    with col3:
        st.html("""
        <div class="stat-card">
            <div class="stat-number">0–20</div>
            <div class="stat-label">Grade Scale</div>
        </div>
        """)

    with col4:
        st.html("""
        <div class="stat-card">
            <div class="stat-number">ML</div>
            <div class="stat-label">Prediction Engine</div>
        </div>
        """)


    st.write("")
    st.divider()


    # --------------------------------------------------------
    # STUDENT INFORMATION
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">👤 Student Information</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Basic demographic and school information.'
        '</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        school = st.selectbox(
            "School",
            ["GP", "MS"]
        )

        sex = st.selectbox(
            "Sex",
            ["F", "M"]
        )

        age = st.number_input(
            "Age",
            min_value=15,
            max_value=25,
            value=17
        )

    with col2:

        address = st.selectbox(
            "Address",
            ["U", "R"],
            format_func=lambda x:
                "Urban" if x == "U" else "Rural"
        )

        famsize = st.selectbox(
            "Family Size",
            ["LE3", "GT3"],
            format_func=lambda x:
                "3 or fewer" if x == "LE3"
                else "More than 3"
        )

        Pstatus = st.selectbox(
            "Parent Status",
            ["T", "A"],
            format_func=lambda x:
                "Together" if x == "T"
                else "Apart"
        )

    with col3:

        guardian = st.selectbox(
            "Guardian",
            ["mother", "father", "other"]
        )

        reason = st.selectbox(
            "School Choice Reason",
            ["home", "reputation", "course", "other"]
        )

        internet = st.selectbox(
            "Internet Access",
            ["yes", "no"]
        )


    st.divider()


    # --------------------------------------------------------
    # FAMILY & EDUCATION
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">👨‍👩‍👧 Family & Education</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Family background and educational support.'
        '</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        Medu = st.slider(
            "Mother's Education",
            0,
            4,
            2,
            help="0 = none, 4 = higher education"
        )

        Fedu = st.slider(
            "Father's Education",
            0,
            4,
            2,
            help="0 = none, 4 = higher education"
        )

    with col2:

        Mjob = st.selectbox(
            "Mother's Job",
            [
                "teacher",
                "health",
                "services",
                "at_home",
                "other"
            ]
        )

        Fjob = st.selectbox(
            "Father's Job",
            [
                "teacher",
                "health",
                "services",
                "at_home",
                "other"
            ]
        )

    with col3:

        famrel = st.slider(
            "Family Relationship",
            1,
            5,
            4
        )

        famsup = st.selectbox(
            "Family Educational Support",
            ["yes", "no"]
        )


    st.divider()


    # --------------------------------------------------------
    # ACADEMIC INFORMATION
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">📚 Academic Information</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Study habits, academic support and previous performance.'
        '</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        traveltime = st.slider(
            "Travel Time",
            1,
            4,
            1
        )

        studytime = st.slider(
            "Study Time",
            1,
            4,
            2
        )

        failures = st.slider(
            "Past Class Failures",
            0,
            4,
            0
        )

    with col2:

        schoolsup = st.selectbox(
            "Extra Educational Support",
            ["yes", "no"]
        )

        paid = st.selectbox(
            "Extra Paid Classes",
            ["yes", "no"]
        )

        activities = st.selectbox(
            "Extra-curricular Activities",
            ["yes", "no"]
        )

    with col3:

        nursery = st.selectbox(
            "Attended Nursery School",
            ["yes", "no"]
        )

        higher = st.selectbox(
            "Wants Higher Education",
            ["yes", "no"]
        )

        romantic = st.selectbox(
            "Romantic Relationship",
            ["yes", "no"]
        )


    st.divider()


    # --------------------------------------------------------
    # LIFESTYLE & HEALTH
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">🏃 Lifestyle & Health</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Lifestyle, free time, health and attendance.'
        '</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        freetime = st.slider(
            "Free Time",
            1,
            5,
            3
        )

        goout = st.slider(
            "Going Out",
            1,
            5,
            3
        )

    with col2:

        Dalc = st.slider(
            "Workday Alcohol Consumption",
            1,
            5,
            1
        )

        Walc = st.slider(
            "Weekend Alcohol Consumption",
            1,
            5,
            1
        )

    with col3:

        health = st.slider(
            "Health Status",
            1,
            5,
            3
        )

        absences = st.number_input(
            "Number of Absences",
            min_value=0,
            max_value=100,
            value=5
        )


    st.divider()


    # --------------------------------------------------------
    # PREVIOUS ACADEMIC PERFORMANCE
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">'
        '📈 Previous Academic Performance'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Previous grades are important inputs for predicting G3.'
        '</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        G1 = st.number_input(
            "First Period Grade (G1)",
            min_value=0,
            max_value=20,
            value=10
        )

    with col2:

        G2 = st.number_input(
            "Second Period Grade (G2)",
            min_value=0,
            max_value=20,
            value=10
        )


    # --------------------------------------------------------
    # PROFILE PREVIEW
    # --------------------------------------------------------

    with st.expander("👀 Preview Student Profile"):

        profile_col1, profile_col2, profile_col3, profile_col4 = st.columns(4)

        with profile_col1:
            st.metric("Age", age)

        with profile_col2:
            st.metric("Study Time", f"{studytime}/4")

        with profile_col3:
            st.metric("Absences", absences)

        with profile_col4:
            st.metric("G2", f"{G2}/20")


    st.divider()


    # --------------------------------------------------------
    # PREDICTION
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">🎯 Generate Prediction</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'The trained machine learning pipeline will analyze '
        'the student information and estimate the final grade.'
        '</div>',
        unsafe_allow_html=True
    )

    predict_button = st.button(
        "🚀 Predict Final Grade",
        use_container_width=True,
        type="primary"
    )


    if predict_button:

        # ----------------------------------------------------
        # CREATE INPUT DATA
        # ----------------------------------------------------

        student_data = {

            "school": school,
            "sex": sex,
            "age": age,
            "address": address,
            "famsize": famsize,
            "Pstatus": Pstatus,

            "Medu": Medu,
            "Fedu": Fedu,

            "Mjob": Mjob,
            "Fjob": Fjob,

            "reason": reason,
            "guardian": guardian,

            "traveltime": traveltime,
            "studytime": studytime,
            "failures": failures,

            "schoolsup": schoolsup,
            "famsup": famsup,
            "paid": paid,

            "activities": activities,
            "nursery": nursery,
            "higher": higher,

            "internet": internet,
            "romantic": romantic,

            "famrel": famrel,
            "freetime": freetime,
            "goout": goout,

            "Dalc": Dalc,
            "Walc": Walc,
            "health": health,

            "absences": absences,

            "G1": G1,
            "G2": G2
        }


        student_df = pd.DataFrame(
            [student_data]
        )


        # ----------------------------------------------------
        # MODEL PREDICTION
        # ----------------------------------------------------

        prediction = model.predict(
            student_df
        )[0]

        prediction = max(
            0,
            min(20, prediction)
        )


        # ----------------------------------------------------
        # INTERPRETATION
        # ----------------------------------------------------

        if prediction >= 16:

            interpretation = "Excellent Performance 🌟"
            emoji = "🏆"

        elif prediction >= 12:

            interpretation = "Good Performance 👍"
            emoji = "📈"

        elif prediction >= 10:

            interpretation = "Satisfactory Performance 📚"
            emoji = "📚"

        else:

            interpretation = "Needs Improvement 💡"
            emoji = "💡"


        percentage = prediction * 5

        score_10 = prediction / 2

        gauge_position = min(
            max(
                (prediction / 20) * 100,
                0
            ),
            100
        )


        # ----------------------------------------------------
        # RESULT CARD
        # ----------------------------------------------------

        st.html(f"""
        <div class="result-card">

            <div class="result-label">
                {emoji} Predicted Final Grade
            </div>

            <div class="result-score">
                {prediction:.2f} / 20
            </div>

            <div class="result-category">
                {interpretation}
            </div>

            <div class="result-secondary">
                Equivalent to
                <b>{score_10:.2f} / 10</b>
                &nbsp; • &nbsp;
                <b>{percentage:.1f}%</b>
            </div>

            <div class="gauge-container">

                <div class="gauge-labels">
                    <span>0</span>
                    <span>5</span>
                    <span>10</span>
                    <span>15</span>
                    <span>20</span>
                </div>

                <div class="gauge">

                    <div
                        class="gauge-marker"
                        style="left: calc(
                            {gauge_position}% - 13px
                        );"
                    ></div>

                </div>

            </div>

        </div>
        """)


        st.success(
            "Prediction generated successfully using the trained ML model."
        )


        # ----------------------------------------------------
        # PERFORMANCE SNAPSHOT
        # ----------------------------------------------------

        st.markdown(
            '<div class="section-title">'
            '🔎 Student Performance Snapshot'
            '</div>',
            unsafe_allow_html=True
        )

        insight1, insight2, insight3, insight4 = st.columns(4)


        with insight1:

            st.html(f"""
            <div class="insight-card">

                <div class="insight-title">
                    📊 G2 Grade
                </div>

                <div class="insight-value">
                    {G2}/20
                </div>

                <div class="insight-text">
                    Second-period academic performance
                </div>

            </div>
            """)


        with insight2:

            st.html(f"""
            <div class="insight-card">

                <div class="insight-title">
                    📚 Study Time
                </div>

                <div class="insight-value">
                    {studytime}/4
                </div>

                <div class="insight-text">
                    Weekly study-time category
                </div>

            </div>
            """)


        with insight3:

            st.html(f"""
            <div class="insight-card">

                <div class="insight-title">
                    🚫 Absences
                </div>

                <div class="insight-value">
                    {absences}
                </div>

                <div class="insight-text">
                    Recorded school absences
                </div>

            </div>
            """)


        with insight4:

            st.html(f"""
            <div class="insight-card">

                <div class="insight-title">
                    🎯 G1 Grade
                </div>

                <div class="insight-value">
                    {G1}/20
                </div>

                <div class="insight-text">
                    First-period academic performance
                </div>

            </div>
            """)


        # ----------------------------------------------------
        # ACADEMIC CHART
        # ----------------------------------------------------

        st.write("")

        st.markdown(
            '<div class="section-title">'
            '📈 Academic Performance'
            '</div>',
            unsafe_allow_html=True
        )

        chart_data = pd.DataFrame(
            {
                "Grade": [
                    G1,
                    G2,
                    prediction
                ]
            },
            index=[
                "G1",
                "G2",
                "Predicted G3"
            ]
        )

        st.bar_chart(
            chart_data,
            y="Grade",
            height=300
        )


# ============================================================
# ABOUT PAGE
# ============================================================

else:

    # --------------------------------------------------------
    # ABOUT HERO
    # --------------------------------------------------------

    st.html("""
    <div class="hero">

        <div class="hero-title">
            🤖 About Student Performance AI
        </div>

        <div class="hero-subtitle">
            An end-to-end machine learning project for
            predicting student final academic performance.
        </div>

    </div>
    """)


    # --------------------------------------------------------
    # PROJECT INFORMATION
    # --------------------------------------------------------

    col1, col2 = st.columns(2)


    with col1:

        st.html("""
        <div class="about-card">

            <h3>🎯 Project Goal</h3>

            <p>
            The goal of this project is to build a machine
            learning system that estimates a student's final
            academic grade using demographic, family,
            academic, lifestyle and previous performance data.
            </p>

            <p>
            The target variable is <b>G3</b>, the student's
            final grade.
            </p>

        </div>
        """)


    with col2:

        st.html("""
        <div class="about-card">

            <h3>⚙️ How It Works</h3>

            <p>
            The application collects 32 student features,
            converts them into the format expected by the
            trained preprocessing pipeline and sends them
            to the saved machine learning model.
            </p>

            <p>
            The model then returns an estimated final grade.
            </p>

        </div>
        """)


    st.write("")
    st.divider()


    # --------------------------------------------------------
    # TECHNOLOGIES
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">'
        '🛠 Technologies Used'
        '</div>',
        unsafe_allow_html=True
    )

    tech1, tech2, tech3, tech4 = st.columns(4)

    with tech1:
        st.info("🐍 Python")

    with tech2:
        st.info("🐼 Pandas")

    with tech3:
        st.info("🤖 Scikit-learn")

    with tech4:
        st.info("🌐 Streamlit")


    st.divider()


    # --------------------------------------------------------
    # MACHINE LEARNING PIPELINE
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">'
        '🔄 Machine Learning Pipeline'
        '</div>',
        unsafe_allow_html=True
    )

    st.write("")


    step1, step2, step3, step4 = st.columns(4)


    with step1:

        st.html("""
        <div class="about-card">

            <h3>1️⃣ Data</h3>

            <p>
            Student performance dataset containing
            demographic, family, academic and lifestyle
            information.
            </p>

        </div>
        """)


    with step2:

        st.html("""
        <div class="about-card">

            <h3>2️⃣ Preprocessing</h3>

            <p>
            Numerical and categorical features are processed
            using the trained preprocessing pipeline.
            </p>

        </div>
        """)


    with step3:

        st.html("""
        <div class="about-card">

            <h3>3️⃣ Model</h3>

            <p>
            The saved machine learning pipeline receives
            the processed student information.
            </p>

        </div>
        """)


    with step4:

        st.html("""
        <div class="about-card">

            <h3>4️⃣ Prediction</h3>

            <p>
            The model estimates the student's final G3
            grade on a 0–20 scale.
            </p>

        </div>
        """)


    st.divider()


    # --------------------------------------------------------
    # PROJECT STRUCTURE
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">'
        '📁 Project Structure'
        '</div>',
        unsafe_allow_html=True
    )

    st.code("""
Student-Performance-Prediction/
│
├── data/
│   └── student-mat.csv
│
├── images/
│   └── app-screenshot.png
│
├── models/
│   └── final_model.pkl
│
├── notebooks/
│   └── Student_Performance_Prediction_Final.ipynb
│
├── app.py
├── README.md
├── requirements.txt
└── .gitignore
    """)


    st.divider()


    # --------------------------------------------------------
    # WARNING
    # --------------------------------------------------------

    st.warning(
        "This application is an educational machine learning "
        "portfolio project. Predictions are estimates and should "
        "not be treated as definitive assessments of a student's "
        "future academic performance."
    )


# ============================================================
# FOOTER
# ============================================================

st.html("""
<div class="footer">

    🎓 Student Performance AI
    &nbsp; • &nbsp;
    Machine Learning Portfolio Project
    &nbsp; • &nbsp;
    Built with Python & Streamlit

</div>
""")