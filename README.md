#                                                        EmailPhishEx 

# A Comprehensive Phishing Email Detection and Reporting System

##  Overview

**PhishGuard** is an intelligent, modular system designed to automatically detect and report phishing emails. It mimics real-world email inspection by analyzing content, attachments, sender behavior, and structural patterns using a blend of natural language processing, behavioral analysis, and metadata extraction.

---

## Key Features

### 1. Attachment Scanning
- Detects potentially harmful files (scripts, executables, or macro-enabled documents).
- Analyzes structure and embedded content for malicious behavior.
- Extracts metadata, flags unusual file types or obfuscation techniques.

### 2. Email Parsing
- Extracts email headers, subject, body (HTML & plain text), sender details, and message structure.
- Identifies discrepancies like mismatched reply-to addresses or spoofed senders.
- Detects embedded links and encoded content.

### 3. Domain Lookup
- Inspects the sender domain for suspicious characteristics.
- Checks domain age, DNS records, and registrant information.
- Identifies lookalike or misspelled domains.

### 4. Stylometry Analysis
- Examines the writing style of the email body.
- Evaluates linguistic features such as punctuation, sentence structure, and word choice.
- Flags deviations from known or expected writing behavior.

### 5. Phishing Detection via NLP
- Analyzes the email content for social engineering patterns.
- Detects urgency, threats, fake requests, and suspicious links.
- Evaluates keyword presence, tone, and language complexity.
- Uses both text and HTML structures (like tag frequency and form usage) for classification.

---

