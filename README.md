# 🌾 Snowflake CoCo Smart Agro Engine (GCP Integrated)

An end-to-end Automated Smart Agriculture Telemetry & Analytics Pipeline built for the Snowflake CoCo Hackathon. This platform continuously ingests real-time drone telemetry and crop-health datasets from Google Cloud Platform (GCP) into Snowflake CoCo Data Cloud for AI-driven insights.

---

## 🚀 Architecture Overview

```text
[ Smart Agro Drones / Sensors ]
              │
              ▼
  [ Google Cloud Platform ] ────► (e2-medium Linux Instance running 24/7 Agro Engine)
              │
              ▼
[ Snowflake CoCo Data Cloud ] ───► (Automated Data Pipeline & AI-driven SQL Analytics)
              │
              ▼
  [ Real-time Streamlit Dashboard ]
