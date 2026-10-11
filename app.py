import streamlit as st
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

st.set_page_config(page_title="3Q | Qubit Quest", page_icon="⚛️", layout="wide")
st.markdown("""
<style>
/* Light background */
.stApp {
    background: #F5F7FB !important;
    color: #172B4D !important;
}

/* Clear, dark headings */
h1, h2, h3 {
    color: #12304A !important;
    font-weight: 700 !important;
}

/* Readable body text */
p, label, span, li {
    color: #26374D !important;
    opacity: 1 !important;
}

/* Light sidebar */
[data-testid="stSidebar"] {
    background: #E8EEF8 !important;
}

/* White metric cards */
div[data-testid="stMetric"] {
    background: #FFFFFF !important;
    color: #172B4D !important;
    padding: 14px;
    border: 1px solid #D8E1EF;
    border-radius: 12px;
}

/* Teal buttons with white text */
.stButton > button {
    background: #087E8B !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 9px !important;
    font-weight: 600 !important;
}

/* Light circuit/code panels */
.stCode, pre {
    background: #F0F3F8 !important;
    color: #172B4D !important;
}

/* Readable explanatory text */
[data-testid="stCaptionContainer"] {
    color: #334155 !important;
}
</style>
""", unsafe_allow_html=True)

st.title("⚛️ QUBIT QUEST")
st.caption("3Q — Quantum Quest Qubits | Think Quantum. Solve the Impossible.")
st.write("Predict the quantum outcome, run the simulator, and learn from the result.")

MISSIONS = {
    "1 · Superposition Lab": {
        "description": "Start in |0⟩ and apply a Hadamard gate. What measurement distribution do you expect?",
        "options": ["100% 0", "50% 0 and 50% 1", "100% 1", "25% each for 0 and 1"],
        "answer": "50% 0 and 50% 1",
        "explanation": "H|0⟩ = (|0⟩ + |1⟩)/√2. Repeated measurements approach a 50/50 distribution.",
        "kind": "superposition",
    },
    "2 · Entanglement Chamber": {
        "description": "Create a Bell state using H on qubit 0 and CNOT(0, 1). Which outcomes can appear?",
        "options": ["Only 00 and 11", "Only 01 and 10", "All four equally", "Only 00"],
        "answer": "Only 00 and 11",
        "explanation": "The circuit creates (|00⟩ + |11⟩)/√2. In Qiskit's displayed bitstrings, the two bits agree: 00 or 11.",
        "kind": "entanglement",
    },
    "3 · Measurement Lab": {
        "description": "Prepare |0⟩, apply an Ry(θ) rotation, then measure in the computational basis. For θ = 90°, what are the probabilities?",
        "options": ["100% 0", "50% 0 and 50% 1", "100% 1", "75% 0 and 25% 1"],
        "answer": "50% 0 and 50% 1",
        "explanation": "Ry(θ)|0⟩ = cos(θ/2)|0⟩ + sin(θ/2)|1⟩. At θ=90°, both outcomes have probability 1/2.",
        "kind": "measurement",
    },
}

def build_circuit(kind, theta_degrees=90):
    if kind == "superposition":
        qc = QuantumCircuit(1, 1)
        qc.h(0)
        qc.measure(0, 0)
    elif kind == "entanglement":
        qc = QuantumCircuit(2, 2)
        qc.h(0)
        qc.cx(0, 1)
        qc.measure([0, 1], [0, 1])
    else:
        import math
        qc = QuantumCircuit(1, 1)
        qc.ry(math.radians(theta_degrees), 0)
        qc.measure(0, 0)
    return qc

@st.cache_resource
def get_simulator():
    return AerSimulator()

with st.sidebar:
    st.header("Mission Control")
    mission_name = st.radio("Choose a mission", list(MISSIONS.keys()))
    shots = st.select_slider("Simulation shots", options=[100, 250, 500, 1000, 2000], value=1000)
    theta = 90
    if MISSIONS[mission_name]["kind"] == "measurement":
        theta = st.select_slider("Rotation angle θ (degrees)", options=[0, 90, 180], value=90)
    st.markdown("---")
    st.caption("Simulator only — no quantum hardware required.")

mission = MISSIONS[mission_name]
left, right = st.columns([1.1, 1])
with left:
    st.subheader(mission_name)
    st.write(mission["description"])
    prediction = st.radio("Your prediction:", mission["options"], index=None, key=mission_name)
    run = st.button("▶ Run quantum experiment", type="primary", use_container_width=True)
with right:
    st.subheader("Circuit")
    qc_preview = build_circuit(mission["kind"], theta)
    st.code(str(qc_preview.draw(output="text")), language="text")
    st.caption("Circuit shown as text for reliable rendering in Colab/Streamlit.")

if "scores" not in st.session_state:
    st.session_state.scores = {name: None for name in MISSIONS}

if run:
    qc = build_circuit(mission["kind"], theta)
    simulator = get_simulator()
    compiled = transpile(qc, simulator)
    result = simulator.run(compiled, shots=shots).result()
    counts = result.get_counts()
    st.session_state[f"counts_{mission_name}"] = counts
    st.session_state[f"prediction_{mission_name}"] = prediction
    st.session_state[f"theta_{mission_name}"] = theta
    expected_answer = mission["answer"]
    if mission["kind"] == "measurement":
        expected_answer = {0: "100% 0", 90: "50% 0 and 50% 1", 180: "100% 1"}[theta]
    correct = prediction == expected_answer
    st.session_state[f"expected_{mission_name}"] = expected_answer
    st.session_state.scores[mission_name] = bool(correct)
    st.session_state[f"has_run_{mission_name}"] = True

if st.session_state.get(f"has_run_{mission_name}", False):
    counts = st.session_state[f"counts_{mission_name}"]
    saved_prediction = st.session_state.get(f"prediction_{mission_name}")
    expected_answer = st.session_state.get(f"expected_{mission_name}", mission["answer"])
    correct = saved_prediction == expected_answer
    st.markdown("---")
    st.subheader("Experiment results")
    c1, c2, c3 = st.columns(3)
    c1.metric("Shots", sum(counts.values()))
    c2.metric("Distinct outcomes", len(counts))
    c3.metric("Prediction", "Correct ✓" if correct else "Try again ↻")
    if correct:
        st.success("Great prediction! You earned 100 quantum points.")
    else:
        st.info(f"Expected answer for this experiment: {expected_answer}. Review the explanation and try another prediction.")
    st.write("**Measured counts**")
    sorted_counts = dict(sorted(counts.items()))
    fig, ax = plt.subplots()
    ax.bar(list(sorted_counts.keys()), list(sorted_counts.values()))
    ax.set_xlabel("Measured bitstring")
    ax.set_ylabel("Count")
    ax.set_title("Qiskit Aer measurement outcomes")
    fig.tight_layout()
    st.pyplot(fig)
    plt.close(fig)
    st.info(mission["explanation"])
    with st.expander("Show exact probabilities from this finite run"):
        total = sum(counts.values())
        for outcome, count in sorted_counts.items():
            st.write(f"`{outcome}`: {count}/{total} = {count/total:.1%}")

st.markdown("---")
st.subheader("Quest progress")
points = sum(100 for v in st.session_state.scores.values() if v is True)
p1, p2 = st.columns(2)
p1.metric("Total points", f"{points}/300")
p2.metric("Missions completed correctly", f"{sum(v is True for v in st.session_state.scores.values())}/3")
st.progress(points / 300)
st.caption("Educational prototype by Team 3Q. Measurement results vary between runs because quantum outcomes are probabilistic.")
