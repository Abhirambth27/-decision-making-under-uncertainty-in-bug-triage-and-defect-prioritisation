# Replication Package: Decision-Making Under Uncertainty in Bug Triage and Defect Prioritisation

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Methodology: Convergent Mixed-Methods](https://img.shields.io/badge/Methodology-Mixed--Methods-blue.svg)](https://link.springer.com/book/10.1007/978-3-642-48607-4)
[![GDPR: Article 89 Compliant](https://img.shields.io/badge/GDPR-Article%2089%20Compliant-green.svg)](https://gdpr-info.eu/art-89-gdpr/)
[![Institution: BTH](https://img.shields.io/badge/Institution-Blekinge%20Institute%20of%20Technology-navy.svg)](https://www.bth.se/)

This repository serves as the official open-access **Empirical Replication Package** for the Master's Thesis:

> **"Decision-Making Under Uncertainty in Bug Triage and Defect Prioritisation: An Empirical Investigation of Cognitive Heuristics and Socio-Technical Constraints"**  
> **Authors:** Naga Sai Abhiram Gopal Vemana (`nave23@student.bth.se`) & Vineeth Kumar Vajja (`viva23@student.bth.se`)  
> **Academic Supervisor:** Muhammad Laiq  
> **Department:** Department of Software Engineering, Faculty of Computing, Blekinge Institute of Technology (BTH), Karlskrona, Sweden.

---

## Executive Summary & Research Scope

Software maintenance accounts for the majority of software lifecycle costs, with bug triage serving as the critical resource-allocation gateway. When defect reports lack execution steps, omit environment logs, or describe non-reproducible bugs, automated machine learning models fail, forcing human practitioners to make risk-informed judgment calls under impending release deadlines.

This research investigates the cognitive strategies, heuristics, and organizational boundaries governing defect triage under uncertainty through a **Convergent Mixed-Methods Design**:
* **Qualitative Strand:** 12 in-depth semi-structured interviews with software engineering practitioners ($N=12$, participants $P_{01}$ to $P_{12}$) across 12 distinct software enterprises, generating **2,043 timestamped conversational utterances** analyzed via 6-phase reflexive thematic analysis (saturation confirmed at $P_{08}$).
* **Quantitative Strand:** An exploratory cross-sectional industry survey of 65 verified software professionals ($N=65$) providing empirical data triangulation across diverse roles, system domains, and experience tiers.
* **Theoretical Grounding:** Naturalistic Decision Making (NDM), Gary Klein's Recognition-Primed Decision (RPD) model, Herbert Simon's Bounded Rationality and Satisficing, and Lipshitz & Strauss's RAWFS uncertainty coping taxonomy.

---

## Curated Replication Manifest

To make navigation seamless and immediate for examiners and peer researchers, instruments and coding manuals are provided directly as clean, self-contained PDF documents:

```text
├── Codebook/
│   └── codebook.pdf                          # Formatted Qualitative Thematic Codebook Manual (13 axial codes)
│
├── Interview/
│   └── Interview_Document.pdf                # Complete 12-Question Semi-Structured Interview Protocol Guide
│
├── Survey/
│   └── Survey_Document.pdf                   # Complete 11-Question Cross-Sectional Industry Survey Instrument
│
├── Transcription and Anonymization Pipeline/
│   ├── 01_transcribe_audio_to_raw.py         # Offline local Automated Speech Recognition (Faster-Whisper)
│   ├── 02_format_and_anonymize_transcripts.py# Regex entity de-identification & structural markdown generator
│   ├── 03_verify_transcript_fidelity.py      # Automated mathematical line-by-line fidelity verification
│   ├── run_entire_pipeline.py                # End-to-end orchestration pipeline runner
│   ├── Transcript_Fidelity_and_Anonymization_Audit_Report.md # Full 2,043-utterance audit report
│   ├── requirements.txt                      # Python dependencies for the pipeline
│   ├── 00_TRANSCRIPTION_PIPELINE_KNOWLEDGE_MAP_AND_AUDIT_MATRIX.md # Knowledge map & audit matrix
│   └── README.md                             # Pipeline execution and reproduction instructions
│
├── Transcripts/
│   ├── P01_Transcript_Anonymized.md          # De-identified verbatim transcript for Participant P01
│   ├── P02_Transcript_Anonymized.md          # De-identified verbatim transcript for Participant P02
│   ├── ...                                   # De-identified transcripts for P03 through P11
│   └── P12_Transcript_Anonymized.md          # De-identified verbatim transcript for Participant P12
│
└── README.md                                 # Master replication package documentation (this file)
```

---

## Thematic Taxonomy Summary (13 Axial Codes across 3 Master Themes)

| Master Theme | Axial Code | Canonical Descriptor & Operational Definition |
| :--- | :--- | :--- |
| **Theme 1: Typology of Uncertainty** | `UNC-INCOMP` | **Incomplete Descriptions & Missing Steps:** Omission of reproduction steps, build hashes, or payloads. |
| | `UNC-NONREPRO` | **Environmental Divergence & Non-Repro:** Distributed systems, concurrency flakes, and OS/browser drift. |
| | `UNC-ASYNC-LAG` | **Asynchronous Latency & Information Loops:** Dormant ticket delay while awaiting reporter clarification. |
| | `UNC-SEV-AMBIG` | **Severity Ambiguity & Priority Disagreement:** Subjective priority inflation vs technical reality across QA/Dev. |
| **Theme 2: Cognitive Heuristics (RQ1)** | `HEUR-BLAST-RAD` | **Blast-Radius Estimation:** Mental simulation of failure scope, affected users, and critical pathways. |
| | `HEUR-HIST-ANALOG`| **Historical Analogy & Pattern Matching:** Recognition-primed symptom matching against past outages. |
| | `HEUR-TIME-BOX` | **Investigation Time-Boxing:** Bounding exploratory debugging to a fixed diagnostic threshold (1--4 hrs). |
| | `HEUR-MIN-DELTA` | **Minimum Delta Probing & Bisection:** Isolating recent PR diffs, commits, and configuration changes. |
| | `HEUR-PRAG-WORK` | **Decoupled Pragmatic Mitigation:** Deploying temporary workarounds/feature flags under release pressure. |
| **Theme 3: Socio-Technical Constraints (RQ2)** | `ORG-RELEASE-GATE`| **Release Gating & Deadline Compression:** Impending deployment deadlines forcing binary blocker triage. |
| | `ORG-LOAD-THROT` | **Workload Throttling & Overload Management:** Ticket batching and backlog pruning to avoid cognitive fatigue. |
| | `ORG-MGMT-ALIGN` | **Management Expectations & Business SLAs:** Commercial client priorities and contractual SLA alignments. |
| | `ORG-SOC-CONSULT` | **Social Consultation & Consensus:** Synchronous cross-functional huddles to resolve contested priority. |

---

## Ethics, Privacy, and GDPR Compliance Statement

This empirical research strictly adheres to the ethical standards of Blekinge Institute of Technology (BTH) and the **European Union General Data Protection Regulation (Regulation EU 2016/679, Article 89)** governing scientific research:
1. **Informed Consent:** Explicit, voluntary consent was obtained from all 12 interviewees and 65 survey respondents prior to data collection.
2. **Strict Anonymization & De-Identification:** All personal identities, employer names, proprietary software titles, internal domain names, and server URLs were systematically replaced with standardized alphanumeric tokens ($P_{01}\text{--}P_{12}$, generic technology labels).
3. **Exclusion of Raw Audio Recordings:** In accordance with participant consent agreements and institutional privacy protocols, raw acoustic audio recordings and un-anonymized intermediate files are **strictly excluded from this public repository** to protect participant confidentiality.
4. **Fidelity Verification:** An automated mathematical audit confirmed that de-identification achieved a 100% utterance match (2,043 raw segments exactly matching 2,043 anonymized segments) with zero content deletion or narrative distortion.

---

## How to Run the Transcription & Verification Pipeline

To inspect or execute the automated transcription, regex masking, and fidelity verification scripts:

### Prerequisites
* Python 3.10+
* Virtual environment (`venv` recommended)

### Setup & Execution
```bash
# 1. Navigate to the pipeline folder
cd "Transcription and Anonymization Pipeline"

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the automated line-by-line fidelity audit check
python 03_verify_transcript_fidelity.py

# 4. Or execute the entire verification suite
python run_entire_pipeline.py
```

---

## Citation & Contact

If you utilize this replication package, dataset, or codebook in academic research, please cite:

```bibtex
@mastersthesis{vemana_vajja_2026_triage,
  author       = {Naga Sai Abhiram Gopal Vemana and Vineeth Kumar Vajja},
  title        = {Decision-Making Under Uncertainty in Bug Triage and Defect Prioritisation: 
                  An Empirical Investigation of Cognitive Heuristics and Socio-Technical Constraints},
  school       = {Blekinge Institute of Technology (BTH), Faculty of Computing},
  year         = {2026},
  month        = {September},
  address      = {Karlskrona, Sweden},
  type         = {Master's Thesis}
}
```

**Correspondence:**
* Naga Sai Abhiram Gopal Vemana (`nave23@student.bth.se`)
* Vineeth Kumar Vajja (`viva23@student.bth.se`)
* Department of Software Engineering, Blekinge Institute of Technology, SE--371 79 Karlskrona, Sweden.
