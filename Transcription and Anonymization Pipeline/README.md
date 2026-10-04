# Transcription & Anonymization Pipeline Package
## PA2534 Master's Thesis in Software Engineering
**Thesis Title:** *Decision-Making Under Uncertainty in Bug Triage and Defect Prioritisation*  
**Authors:** Naga Sai Abhiram Gopal Vemana & Vineeth Kumar Vajja  
**Supervisor:** Muhammad Laiq  
**Institution:** Blekinge Institute of Technology (BTH), Karlskrona, Sweden  
**Date:** May 2026  

---

### Package Contents

This directory contains the complete deterministic data processing pipeline used to convert raw qualitative interview audio recordings into de-identified, verified research transcripts:

```
Transcription and Anonymization Pipeline/
├── 00_TRANSCRIPTION_PIPELINE_KNOWLEDGE_MAP_AND_AUDIT_MATRIX.md  <-- Complete Knowledge Map & Defense Guide
├── README.md                                                    <-- This Overview File
├── run_entire_pipeline.py                                       <-- Master Entrypoint (Runs Steps 01 -> 02 -> 03)
├── 01_transcribe_audio_to_raw.py                                <-- Step 01: Verbatim Faster-Whisper ASR Transcription
├── 02_format_and_anonymize_transcripts.py                       <-- Step 02: Deterministic De-ID & Phonetic Correction
├── 03_verify_transcript_fidelity.py                             <-- Step 03: Line-by-Line Parity & Audit Log
└── requirements.txt                                             <-- Python Dependencies
```

---

### Execution Instructions

To run the full end-to-end pipeline with automated verification:
```powershell
python run_entire_pipeline.py
```

Or run individual steps sequentially:
```powershell
python 01_transcribe_audio_to_raw.py
python 02_format_and_anonymize_transcripts.py
python 03_verify_transcript_fidelity.py
```

For complete technical specifications, GDPR compliance rules, and oral defense Q&A, see [`00_TRANSCRIPTION_PIPELINE_KNOWLEDGE_MAP_AND_AUDIT_MATRIX.md`](file:///C:/Users/mkris/Desktop/Final%20Master%20thesis%20%20draft%20preparation/Transcription%20and%20Anonymization%20Pipeline/00_TRANSCRIPTION_PIPELINE_KNOWLEDGE_MAP_AND_AUDIT_MATRIX.md).
