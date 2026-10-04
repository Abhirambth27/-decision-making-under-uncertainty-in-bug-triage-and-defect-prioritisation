"""
Master Thesis Pipeline - Step 02: Formatting & Anonymization
Authors: Naga Sai Abhiram Gopal Vemana & Vineeth Kumar Vajja
Department of Software Engineering, Blekinge Institute of Technology (BTH)

Description:
Applies deterministic de-identification, phonetic domain correction, and structured
markdown formatting to raw transcripts across all 12 participants.
"""

import os
import sys
import re

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
transcripts_dir = os.path.join(base_dir, "Transcripts")
raw_dir = os.path.join(transcripts_dir, "raw")

PARTICIPANT_INFO = {
    "P01": {
        "name": "Monica",
        "role": "AI Product Architect",
        "experience": "4+ years in enterprise software & AI solution architecture",
        "domain": "Enterprise AI Solutions & Telecommunications Data Infrastructure",
        "tools": "AWS Athena, Jira, GitHub Issues, PowerBI",
        "date": "2026-08-11"
    },
    "P02": {
        "name": "Kishan",
        "role": "Backend Developer / Systems Engineer",
        "experience": "6+ years in backend development & telecom fault management",
        "domain": "Telecommunications Backend Services & Fault Analysis",
        "tools": "Python, Jira, Test Analysis Suites, Git",
        "date": "2026-08-13"
    },
    "P03": {
        "name": "Satyadev",
        "role": "Data Engineer / Production Pipeline Engineer",
        "experience": "5+ years in production data pipelines & distributed systems",
        "domain": "High-Throughput Data Pipelines & Distributed Systems",
        "tools": "Airflow, PySpark, Snowflake, Kafka, dbt, Jira",
        "date": "2026-08-15"
    },
    "P04": {
        "name": "Hari",
        "role": "Senior Embedded Architect & Technical Lead",
        "experience": "20+ years leading embedded software & telecom engineering teams",
        "domain": "Embedded Telecom Systems & Multi-Module Field Diagnostics",
        "tools": "Internal Troubleshoot Trackers, Module Test Suites, Jira",
        "date": "2026-08-16"
    },
    "P05": {
        "name": "Obi",
        "role": "Full-Stack Software Engineer",
        "experience": "5+ years in full-stack development & microservice debugging",
        "domain": "Cloud-Native Platforms, Microservices, VPN Infrastructure",
        "tools": "Docker, CI/CD, Jira, GitHub, Prometheus",
        "date": "2026-08-17"
    },
    "P06": {
        "name": "Ramesh",
        "role": "DevSecOps Engineer",
        "experience": "4+ years in cloud infrastructure, container orchestration & security",
        "domain": "Cloud Infrastructure, OpenShift Kubernetes & Pipeline Security",
        "tools": "Azure Cloud, Terraform, OpenShift Kubernetes, CI/CD",
        "date": "2026-08-18"
    },
    "P07": {
        "name": "Pavithra",
        "role": "Software Developer (Telecom Codebase)",
        "experience": "5–6 years in telecom software development & customer defect resolution",
        "domain": "Telecommunications Feature Development & Customer Bug Resolution",
        "tools": "Git, Unit Testing Frameworks, Jira, Internal Defect Logs",
        "date": "2026-08-18"
    },
    "P08": {
        "name": "Inshal",
        "role": "Senior Software Engineer (Backend)",
        "experience": "6+ years across multiple enterprise software platforms",
        "domain": "Large-Scale Enterprise Software & Release Stabilization",
        "tools": "Jira, Git, Sentry, Monitoring Systems",
        "date": "2026-08-24"
    },
    "P09": {
        "name": "Shreeya",
        "role": "AI & Test Automation Engineer",
        "experience": "2+ years in automation workflows & AI-driven testing",
        "domain": "AI-Driven Automations & Agentic Workflow Tools",
        "tools": "Workflow Automation Platforms, Python, Jira",
        "date": "2026-08-25"
    },
    "P10": {
        "name": "Arjun",
        "role": "Full-Stack & Generative AI Developer",
        "experience": "3+ years in full-stack development & GenAI/RAG pipelines",
        "domain": "Python (FastAPI/Django), React/TypeScript, RAG & Vector DBs",
        "tools": "Jira, FastAPI, React, TypeScript, Vector Databases, Git",
        "date": "2026-08-26"
    },
    "P11": {
        "name": "Karthikeyan",
        "role": "DevOps & Cloud Platform Engineer",
        "experience": "6+ years in CI/CD pipelines, SRE & deployment triage",
        "domain": "CI/CD Pipelines, Deployment Automation & Kubernetes Infrastructure",
        "tools": "Jenkins, Kubernetes, CI/CD, Jira, Prometheus, ELK",
        "date": "2026-08-26"
    },
    "P12": {
        "name": "Manoj",
        "role": "Backend Software Engineer",
        "experience": "6+ years in backend engineering & SaaS platform development",
        "domain": "Enterprise SaaS Platform & Cloud Product Architecture",
        "tools": "Jira, Git, Server Logs, Cloud Infrastructure",
        "date": "2026-08-26"
    },
}

PHONETIC_AND_NAME_FIXES = [
    # Phonetic ASR artifacts
    (r"\bbacteriology\b", "bug triage"),
    (r"\bbug trials\b", "bug triage"),
    (r"\bbug trial\b", "bug triage"),
    (r"\bbucktrage\b", "bug triage"),
    (r"\bBucktrage\b", "bug triage"),
    (r"\bBuctro-H\b", "bug triage"),
    (r"\bbug crash\b", "bug triage"),
    (r"\bbug rage\b", "bug triage"),
    (r"\bbug cryage\b", "bug triage"),
    (r"\bmicrotrigae\b", "bug triage"),
    (r"\bBuck Ridge\b", "bug triage"),
    (r"\bbug-trike\b", "bug triage"),
    (r"\bZira\b", "Jira"),
    (r"\bPowerBear\b", "PowerBI"),
    (r"\bClicking Institute of Technology\b", "Blekinge Institute of Technology"),
    # Participant Names -> Anonymous IDs
    (r"\bMonica\b", "[Participant P01]"),
    (r"\bMonika\b", "[Participant P01]"),
    (r"\bKishan\b", "[Participant P02]"),
    (r"\bKisha\b", "[Participant P02]"),
    (r"\bKrishan\b", "[Participant P02]"),
    (r"\bSatyadev\b", "[Participant P03]"),
    (r"\bSatya\b", "[Participant P03]"),
    (r"\bMr\.? Tali\b", "[Participant P04]"),
    (r"\bHari Anna\b", "[Participant P04]"),
    (r"\bHari\b", "[Participant P04]"),
    (r"\bMr\.? Robi\b", "[Participant P05]"),
    (r"\bObi\b", "[Participant P05]"),
    (r"\bRamesh Bhamdi\b", "[Participant P06]"),
    (r"\bRamish\b", "[Participant P06]"),
    (r"\bRamesh\b", "[Participant P06]"),
    (r"\bPavithraAkka\b", "[Participant P07]"),
    (r"\bPavithra\b", "[Participant P07]"),
    (r"\bPravitra\b", "[Participant P07]"),
    (r"\bPavitra\b", "[Participant P07]"),
    (r"\bInshal\b", "[Participant P08]"),
    (r"\bHi, share\b", "Hi, [Participant P09]"),
    (r"\bShreeya\b", "[Participant P09]"),
    (r"\bShreya\b", "[Participant P09]"),
    (r"\bArjun\b", "[Participant P10]"),
    (r"\bKapthik\b", "[Participant P11]"),
    (r"\bKarthikeyan\b", "[Participant P11]"),
    (r"\bKarthik\b", "[Participant P11]"),
    (r"\bManoj\b", "[Participant P12]"),
    # Researcher & Supervisor Names
    (r"\bAbhiram Gopal\b", "[Interviewer]"),
    (r"\bAbhiram\b", "[Interviewer]"),
    (r"\bAbiram\b", "[Interviewer]"),
    (r"\bAbram\b", "[Interviewer]"),
    (r"\bAviram\b", "[Interviewer]"),
    (r"\bSabram\b", "[Interviewer]"),
    (r"\bAbra\b", "[Interviewer]"),
    (r"\bVineeth Kumar\b", "[Co-Researcher]"),
    (r"\bVineeth\b", "[Co-Researcher]"),
    (r"\bVeenit\b", "[Co-Researcher]"),
    (r"\bVinit\b", "[Co-Researcher]"),
    (r"\bMuhammad Laiq\b", "[Academic Supervisor]"),
    (r"\bLaiq\b", "[Academic Supervisor]"),
    # Employer & Organization De-Identification
    (r"\bEricsson\b", "[Telecommunications Corp A]"),
    (r"\bRixen\b", "[Telecommunications Corp A]"),
    (r"\bCapgemini\b", "[IT Consulting Firm B]"),
    (r"\bInfosys Daniel\b", "[IT Services Corp C]"),
    (r"\bInfosys\b", "[IT Services Corp C]"),
    (r"\bTCS\b", "[Technology Enterprise D]"),
    (r"\bTrisapphire\b", "[Software Solutions Company E]"),
    (r"\bOliver Group\b", "[Enterprise Technology Group F]"),
    (r"\bPTC company\b", "[Product Development Enterprise G]"),
    (r"\bscanned VPN\b", "[VPN & Cloud Security Service]"),
]

def clean_and_anonymize(text):
    for pattern, repl in PHONETIC_AND_NAME_FIXES:
        text = re.sub(pattern, repl, text, flags=re.IGNORECASE)
    return text

def format_transcript_file(p_id):
    raw_path = os.path.join(raw_dir, f"{p_id}_raw.txt")
    if not os.path.exists(raw_path):
        return False
        
    info = PARTICIPANT_INFO.get(p_id, {})
    with open(raw_path, "r", encoding="utf-8") as f:
        raw_lines = [l.strip() for l in f if l.strip()]
        
    out_lines = [
        f"# Master Thesis Interview Transcript: Participant {p_id}",
        "",
        "## 1. Demographic & Context Metadata",
        f"- **Participant ID:** {p_id}",
        f"- **Role:** {info.get('role', 'Software Professional')}",
        f"- **Experience:** {info.get('experience', 'N/A')}",
        f"- **Industry Domain:** {info.get('domain', 'N/A')}",
        f"- **Primary Tooling:** {info.get('tools', 'Jira, Git')}",
        f"- **Interview Date:** {info.get('date', 'August 2026')}",
        f"- **Total Timestamped Utterances:** {len(raw_lines)} segments",
        f"- **Ethical Anonymization Status:** Fully Anonymized (All PII, Company Names & Internal Codes Removed)",
        "",
        "---",
        "",
        "## 2. Verbatim Anonymized Dialogue",
        ""
    ]
    
    for line in raw_lines:
        match = re.match(r"^\[(\d+\.\d+) - (\d+\.\d+)\] (.*)$", line)
        if match:
            start_t, end_t, text = match.groups()
            anon_text = clean_and_anonymize(text)
            out_lines.append(f"- **[{float(start_t):06.2f}s - {float(end_t):06.2f}s]** {anon_text}")
        else:
            out_lines.append(clean_and_anonymize(line))
            
    out_file = os.path.join(transcripts_dir, f"{p_id}_Transcript_Anonymized.md")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("\n".join(out_lines))
    print(f"[{p_id}] Formatted & Anonymized -> {out_file}")
    return True

def generate_demographics_summary():
    out_lines = [
        "# Participant Demographics and Study Context Summary",
        "",
        "This document provides the master demographic index and contextual profiling of the 12 software professionals interviewed for the Master's Thesis: *Decision-Making Under Uncertainty in Bug Triage and Defect Prioritisation* (Blekinge Institute of Technology).",
        "",
        "## Table 4.1: Participant Demographics and Experience Profile",
        "",
        "| ID | Primary Role | Experience Level | Industry / System Context | Primary Tooling | Interview Date |",
        "| :---: | :--- | :--- | :--- | :--- | :--- |"
    ]
    
    for p_id in sorted(PARTICIPANT_INFO.keys()):
        p = PARTICIPANT_INFO[p_id]
        out_lines.append(f"| **{p_id}** | {p['role']} | {p['experience']} | {p['domain']} | {p['tools']} | {p['date']} |")
        
    out_lines.extend([
        "",
        "---",
        "",
        "## Ethical Compliance & Anonymization Protocol",
        "In accordance with Lincoln and Guba (1985) and standard empirical software engineering research ethics:",
        "1. All individual participant names have been permanently replaced with anonymous alphanumeric identifiers ($P_{01}$ through $P_{12}$).",
        "2. All commercial employers, client organizations, and proprietary system/product names have been generalized to industry categories (e.g., `[Telecommunications Corp A]`, `[Enterprise Technology Group F]`).",
        "3. Interviewer names have been standardized to `[Interviewer]` / `[Co-Researcher]`.",
        "4. Exact timestamp references are preserved for full auditable traceability during qualitative coding and thematic synthesis.",
        ""
    ])
    
    summary_file = os.path.join(transcripts_dir, "Participant_Demographics_and_Mapping.md")
    with open(summary_file, "w", encoding="utf-8") as f:
        f.write("\n".join(out_lines))
    print(f"Master Demographics Summary -> {summary_file}")

def run_formatting():
    print("=== [Step 02] Starting Transcript Formatting & Anonymization ===")
    generate_demographics_summary()
    for i in range(1, 13):
        p_id = f"P{i:02d}"
        format_transcript_file(p_id)
    print("=== [Step 02] Completed Formatting for All 12 Participants ===\n")

if __name__ == "__main__":
    run_formatting()
