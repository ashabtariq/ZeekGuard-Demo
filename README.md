# 🛡️ ZeekGuard (Demo)

## Baseline-Driven Network Anomaly Detection using Zeek + Machine Learning

### ZeekGuard is a practical, end-to-end network anomaly detection pipeline built on Zeek logs and unsupervised ML, designed to detect suspicious behavior without relying on attack signatures or labels.

#### This repository contains the public demo / community edition of ZeekGuard — focused on architecture, design, and methodology.

#### 🔒 The full production pipeline, training logic, detection logic, and detailed walkthrough are available in the Gumroad version.

🚨 Problem Statement

Traditional IDS systems:

- Depend on static signatures
- Miss novel or low-and-slow attacks
- Are hard to adapt to new environments

ZeekGuard solves this by:

- Learning what “normal” traffic looks like
- Flagging statistically significant deviations
- Operating without labeled attack data

This mirrors how real SOC anomaly systems work in production.

### 🧠 High-Level Approach

- Ingest Zeek conn.log data
- Clean & normalize traffic
- Generate behavioral features in time windows
- Profile baseline behavior
- Train an unsupervised anomaly model
- Score new traffic and evaluate separation
- Produce human-readable detection summaries

### 🧱 Architecture Overview
Zeek Logs
   ↓
[ Ingest & Cleaning ]
   ↓
[ Feature Engineering ]
   ↓
[ Baseline Profiling ]
   ↓
[ Unsupervised Model Training ]
   ↓
[ Detection & Reporting ]


Each phase is implemented as a clean, reproducible pipeline stage.

### 📂 Repository Structure (Demo)
zeekguard-demo/
├── pipeline/
│   ├── P1_Ingest/
│   │   └── prepare_conn.py        # schema validation & cleaning
│   ├── P2_Features/
│   │   ├── generate_conn_features.py
│   │   └── feature_catalog.py
│   ├── P3_Training/
│   │   ├── baseline_profiling.py
│   │   └── model_train.py
│   └── P4_Detection/
│       └── detection.py
│
├── data/
│   ├── samples/                   # small demo samples only
│
├── notebooks/
│   └── demo.ipynb                 # non-production demo notebook
│
├── README.md
└── LICENSE


## ⚠️ This demo repo does NOT contain the full production logic or datasets.

## 📊 Features (Examples)

ZeekGuard operates on behavioral network features, such as:

- Connection counts (volume)
- Bytes & packets transferred
- Inter-arrival timing
- Destination diversity
- Rate-based metrics

All features are:

- Time-windowed
- Host-centric
- Statistically profiled

## 📈 Detection Logic (Conceptual)

Rather than predicting “attack types”, ZeekGuard answers:

“Is this traffic statistically abnormal compared to baseline?”

Key signals:
- Mean score separation
- Tail concentration (95th / 99th percentile)
- Attack-to-baseline ratio
- Stability over time

This avoids brittle rule-based detection.

🧪 Demo Limitations (Intentional)

This public repo is educational and architectural, not production-ready.

## ❌ Not Included Here:

- Full training pipelines
- Final detection thresholds
- Real baseline/attack datasets
- End-to-end runnable system
- Executive-level reports

## 🔒 Full Version (Gumroad)

The full ZeekGuard package includes:

✔ Complete source code
✔ Production-safe pipeline
✔ Baseline & attack profiling
✔ Detection reports (CSV + JSON)
✔ Step-by-step PDF walkthrough
✔ Design decisions & pitfalls
✔ Interview-ready explanations

👉 [[Full Version](https://ashabariq2.gumroad.com/l/buyty)]

## 🎯 Who This Is For

- Cybersecurity engineers
- SOC analysts
- ML engineers entering security
- Students building serious portfolios
- Professionals learning anomaly detection the right way

## 🧠 Why This Project Matters

ZeekGuard demonstrates:

- Real-world security thinking
- Statistical reasoning (not buzzwords)
- ML applied responsibly
- System design under constraints
- This is how modern detection systems are actually built.

📜 License

This demo repository is released under the MIT License.

## 📬 Contact

If you’re a recruiter, hiring manager, or security professional and want to discuss this project:

💬 Open an issue or connect via LinkedIn [[https://www.linkedin.com/in/ashab-tariq/]]

⭐ If this repo helped you understand network anomaly detection, consider starring it.