"""
Master Execution Entrypoint: Transcription, Anonymization & Verification Pipeline
Authors: Naga Sai Abhiram Gopal Vemana & Vineeth Kumar Vajja
Department of Software Engineering, Blekinge Institute of Technology (BTH)

Usage:
    python run_entire_pipeline.py

This script executes the entire empirical research data processing pipeline in sequential order:
    1. 01_transcribe_audio_to_raw.py
    2. 02_format_and_anonymize_transcripts.py
    3. 03_verify_transcript_fidelity.py
"""

import os
import sys
import subprocess
import time

def main():
    pipeline_dir = os.path.dirname(os.path.abspath(__file__))
    steps = [
        ("01_transcribe_audio_to_raw.py", "Step 01: Transcribing Raw Audio Recordings (.m4a)"),
        ("02_format_and_anonymize_transcripts.py", "Step 02: De-Identification, Formatting & Demographics Indexing"),
        ("03_verify_transcript_fidelity.py", "Step 03: Mathematical Fidelity Verification & Audit Reporting")
    ]
    
    print("=" * 70)
    print("  Blekinge Institute of Technology (BTH) - Master Thesis Pipeline")
    print("  Decision-Making Under Uncertainty in Bug Triage & Prioritisation")
    print("=" * 70 + "\n")
    
    t_start = time.time()
    for script_name, description in steps:
        script_path = os.path.join(pipeline_dir, script_name)
        print(f"[*] RUNNING: {description} ({script_name})...")
        res = subprocess.run([sys.executable, script_path], cwd=pipeline_dir)
        if res.returncode != 0:
            print(f"[!] ERROR: {script_name} failed with exit code {res.returncode}")
            sys.exit(res.returncode)
            
    total_time = time.time() - t_start
    print("=" * 70)
    print(f"  ALL PIPELINE STAGES COMPLETED SUCCESSFULLY IN {total_time:.2f}s!")
    print("=" * 70)

if __name__ == "__main__":
    main()
