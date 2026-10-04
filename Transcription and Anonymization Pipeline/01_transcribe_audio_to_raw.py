"""
Master Thesis Pipeline - Step 01: Audio Transcription
Authors: Naga Sai Abhiram Gopal Vemana & Vineeth Kumar Vajja
Department of Software Engineering, Blekinge Institute of Technology (BTH)

Description:
Converts qualitative interview audio recordings (.m4a) across all 12 participants
into verbatim, timestamped raw text segments using Faster-Whisper (small.en, int8).
"""

import os
import sys
import time
from faster_whisper import WhisperModel

def run_transcription(audio_dir=None, output_dir=None, model_size="small.en", threads=8):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if audio_dir is None:
        audio_dir = os.path.join(base_dir, "all interview audio", "Audio")
    if output_dir is None:
        output_dir = os.path.join(base_dir, "Transcripts", "raw")
        
    os.makedirs(output_dir, exist_ok=True)
    print(f"=== [Step 01] Initializing Faster-Whisper ({model_size}) with {threads} CPU threads ===")
    model = WhisperModel(model_size, device="cpu", compute_type="int8", cpu_threads=threads)
    
    folders = sorted([f for f in os.listdir(audio_dir) if os.path.isdir(os.path.join(audio_dir, f))],
                     key=lambda x: int(x) if x.isdigit() else x)
    
    print(f"Found {len(folders)} audio interview directories to process.")
    for folder in folders:
        sub_path = os.path.join(audio_dir, folder)
        m4a_files = [f for f in os.listdir(sub_path) if f.endswith(".m4a")]
        if not m4a_files:
            continue
            
        p_num = int(folder) if folder.isdigit() else folder
        p_id = f"P{p_num:02d}" if isinstance(p_num, int) else f"P_{p_num}"
        audio_file = os.path.join(sub_path, m4a_files[0])
        raw_out = os.path.join(output_dir, f"{p_id}_raw.txt")
        
        if os.path.exists(raw_out) and os.path.getsize(raw_out) > 0:
            with open(raw_out, "r", encoding="utf-8") as f:
                lines = f.readlines()
            print(f"[{p_id}] Verified existing raw transcript ({len(lines)} segments) -> {raw_out}")
            continue
            
        print(f"[{p_id}] Transcribing {m4a_files[0]}...")
        t0 = time.time()
        segments, info = model.transcribe(audio_file, beam_size=1, language="en", vad_filter=False)
        
        seg_count = 0
        with open(raw_out, "w", encoding="utf-8") as f_out:
            for seg in segments:
                text = seg.text.strip()
                if text:
                    line = f"[{seg.start:06.2f} - {seg.end:06.2f}] {text}"
                    f_out.write(line + "\n")
                    f_out.flush()
                    seg_count += 1
                    
        elapsed = time.time() - t0
        print(f"[{p_id}] Finished {seg_count} segments in {elapsed:.1f}s ({elapsed/60:.2f} mins) -> {raw_out}")

    print("=== [Step 01] Transcription Complete for All Participants ===\n")

if __name__ == "__main__":
    run_transcription()
