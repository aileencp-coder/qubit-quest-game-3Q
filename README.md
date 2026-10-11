# Qiskit Fall Fest 2026 — Project Submission Template
**IIIT Kottayam Quantum Hackathon (24-Hour Sprint)**

> ⚠️ **CRITICAL INSTRUCTIONS FOR PARTICIPANTS:**
> 1. **Do NOT rename or delete the section headings** below. The automated AI evaluation and filtering system relies on this exact Markdown structure to parse and grade your project.
> 2. Replace all placeholder text enclosed in `[brackets]` with your project's details.
> 3. **Commit History Audit:** All project commits must be timestamped strictly within the 24-hour hackathon window (between **October 10, 2026 at 7:05 PM** and **October 11, 2026 at 7:05 PM**). Commits observed outside this window will result in **immediate disqualification**.
> 4. Ensure all Jupyter Notebooks have their cells **run and outputs displayed** before pushing.
> 5. Starter resources and reference guides are located in the [`references/`](./references/) folder.
> 6. **Tech Stack Flexibility:** You are free to use any external frameworks/technologies (e.g., Streamlit, React, Pygame, FastAPI, NetworkX) for your frontend, app logic, or classical baselines. However, **Qiskit MUST power the quantum core** of your project.
> 7. **Full Event Guide & Rules:** For full schedule details, track inspirations, submission steps, and grading focus areas, refer to [`HACKATHON_GUIDE.md`](./HACKATHON_GUIDE.md).

*(You may delete the instructions box above when preparing your final repository submission)*

---

# Project Title

## Project Metadata

* **Project Title:** `Qubit Quest — The Quantum Escape Room`
* **Team Name:** `3Q — Quantum Quest Qubits`
* **Chosen Track:** `Track 1: Quantum Games & Interactive Puzzles`
* **Video Presentation Link:** `https://drive.google.com/drive/folders/1Y17OpZS2hwWB8Qj3D2iHTJ25aedYYOWB?usp=sharing`
  *(⚠️ Crucial: Ensure link access is set to "Anyone with the link can view" on Google Drive or "Unlisted / Public" on YouTube. Locked/inaccessible links cannot be scored!)*
* **Live Demo Timestamp in Video:** `00.00` 

### Team Members (Max 4 members)
| Name | Email | GitHub Username |
| :--- | :--- | :--- |
| `Ms.P.Aileen Chris` | `aileencp@hindustanuniv.ac.in` | `@aileencp-coder` |
| `Dr. B. Monica Jenefer` | `bmonica@hindustanuniv.ac.in` | `monicajenefer.hits@gmail.com` |
| `Dr. Abisheka PON` | `abishekap@hindustanuniv.ac.in` | `abishekapon@gmail.com` |

---

## 1. Project Overview & Motivation

* **Summary (3–4 sentences):**  
  `Qubit Quest — The Quantum Escape Room is an interactive educational game that introduces quantum computing through three missions: superposition, entanglement, and quantum measurement. Players solve quantum challenges by predicting measurement outcomes and verifying them through simulated experiments. The game uses Python, Streamlit, Qiskit, and Qiskit Aer, with a maximum score of 300 points across the three missions. It makes fundamental quantum concepts engaging and accessible without requiring quantum hardware.`

* **Why this problem / game?**  
  `Quantum computing can be difficult for beginners to understand because quantum states and measurement probabilities are not directly visible. Qubit Quest transforms these abstract ideas into interactive missions with predictions, simulations, feedback, and scoring. The game encourages active learning and helps students connect quantum theory with circuit behavior.`

---

## 2. Quantum Architecture & Mechanics

* **Core Quantum Principles Used:**  
  `Superposition using the Hadamard gate, entanglement using a Bell-state circuit, quantum measurement, and angle-dependent measurement probabilities using the Ry rotation gate.`

* **How the Quantum Circuit is Integrated:**  
  `The game presents players with quantum challenges and asks them to predict the expected outcomes. Qiskit constructs and executes the quantum circuits using the Qiskit Aer simulator. The resulting measurement statistics are displayed to help players compare their predictions with the simulated behavior. Mission completion and scoring provide feedback on their progress.`

* **Circuit Details:**  
  * **Number of Qubits:** `1 qubit for the superposition and measurement concepts; 2 qubits for the entanglement mission.`
  * **Key Gates Used:** `H, CX/CNOT, Ry, and measurement.`
  * **Primitives Used:** `Qiskit Aer simulator`
  * **Other Technologies Used:** `Python, Streamlit, Qiskit, and Qiskit Aer`

```python
# Optional: Paste a representative snippet of your core Qiskit circuit code here
```
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Superposition mission
qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)

simulator = AerSimulator()
result = simulator.run(qc, shots=1000).result()
counts = result.get_counts()

print("Superposition measurement results:", counts)

---

## 3. Repository Structure & How to Run

### Project Structure
```qubit-quest-game-3Q/
├── README.md
├── requirements.txt
├── app.py
├── src/
├── notebooks/
└── references/
```

### Installation & Execution Instructions

**Environment Recommendation:** Use a fresh Python virtual environment or Google Colab to avoid dependency conflicts.

1. **Clone the repository:**

   ```bash
   git clone https://github.com/aileencp-coder/qubit-quest-game-3Q.git
   cd qubit-quest-game-3Q
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the project / demo:**

   ```bash
   streamlit run app.py
   ```
## 4. Implementation Walkthrough & Live Demo

* **Walkthrough of Gameplay / Optimization Pipeline:**  
  `Mission 1 — Superposition: Players explore how the Hadamard gate transforms the initial qubit state into a superposition, producing approximately balanced measurement outcomes.

Mission 2 — Entanglement: Players explore a Bell-state circuit prepared using the Hadamard gate and CNOT. The ideal measurement outcomes are correlated, with 00 and 11 observed.

Mission 3 — Measurement Lab: Players investigate how Ry rotations change measurement probabilities. At 0°, the probability of measuring 1 is 0%; at 90°, it is approximately 50%; and at 180°, it is 100%, subject to the circuit's angle convention.

Scoring: Players earn points for successfully completing the missions, with a maximum score of 300 points.

Feedback: The application displays measurement results and mission progress to reinforce learning.`

* **Key Screenshots / Terminal Output:**  
  `[Paste sample terminal output, game screenshots, or optimization convergence plots here to demonstrate that the project runs.]`
<img width="1911" height="1142" alt="image" src="https://github.com/user-attachments/assets/e75800a8-7cdf-4120-8039-b30d0572d5e7" />
[3Q _ Qubit Quest Entanglement Result.pdf](https://github.com/user-attachments/files/33303060/3Q._.Qubit.Quest.Entanglement.Result.pdf)
[3Q _ Qubit Quest Measurement result.pdf](https://github.com/user-attachments/files/33303059/3Q._.Qubit.Quest.Measurement.result.pdf)
[3Q _ Qubit Quest Superposition Result.pdf](https://github.com/user-attachments/files/33303058/3Q._.Qubit.Quest.Superposition.Result.pdf)

---

## 5. Classical vs. Quantum Comparison

* **Classical Baseline / Counterpart:**  
The player's predictions and expected probability distributions act as the educational baseline against which the Qiskit Aer measurement results are compared.



* **Comparative Analysis:**  
 The project demonstrates how quantum circuits produce measurement distributions associated with superposition, entanglement, and single-qubit rotations. Simulated outcomes are compared with expected theoretical behavior. The project is an educational demonstration of quantum principles and does not claim quantum computational advantage over classical methods.

---

## 6. Performance, Results & Limitations

* **Key Results & Observations:**  
  The application provides three interactive missions with a maximum score of 300 points. The superposition circuit produces approximately 50/50 outcomes over sufficiently many shots. The Bell-state circuit produces correlated 00 and 11 outcomes in the ideal simulation. The measurement mission demonstrates how changing the Ry rotation angle changes the probability of observing the state 1.


* **Critical Reflection on Limitations:**  
  Critical Reflection on Limitations:
The current application uses a simulator rather than physical quantum hardware. Measurement results are statistical, so finite-shot experiments may differ slightly from theoretical probabilities. Larger circuits can require more computational resources, and real quantum devices introduce gate errors, noise, and decoherence. Future improvements could include noise-model experiments, additional missions, and execution on available quantum hardware.
---

## 7. References & Acknowledgments


Qiskit documentation: https://docs.quantum.ibm.com/

Qiskit Aer documentation: https://qiskit.github.io/qiskit-aer/

Streamlit documentation: https://docs.streamlit.io/

Acknowledgments: Qubit Quest was developed by Team 3Q — Quantum Quest Qubits for the IIIT Kottayam Quantum Hackathon. The project uses Python, Streamlit, Qiskit, and Qiskit Aer to provide an interactive introduction to quantum computing.
