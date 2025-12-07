# MedicalDocAI

## Overview
An AI-powered assistant that transforms medical documents into clear, structured insights for clinicians and patients. Extracts key findings and actionable recommendations, making healthcare information accessible to everyone.

## 🎯 Purpose
- **For Patients**: Understand medical reports in plain language
- **For Clinicians**: Save 15-20 minutes per patient on document review
- **For Healthcare**: Reduce information barriers and improve health equity

## 🏗️ Architecture

### Tech Stack
- **Backend**: Python + FastAPI
- **AI/LLM**: Claude 3 API (via Raindrop platform)
- **Cloud Infrastructure**: Vultr (compute, storage, database)
- **AI Orchestration**: Raindrop Platform
- **Document Processing**: LangChain, PDF.js
- **Database**: PostgreSQL
- **Deployment**: Docker on Vultr

### Core Services Used
**Raindrop Platform:**
- Raindrop AI Orchestration
- LLM Integration (Claude API access)
- Workflow Builder for document pipelines
- Data Processing modules

**Vultr Services:**
- Cloud Compute (Ubuntu instances)
- Object Storage (document storage)
- Managed Database (PostgreSQL)
- DDoS Protection

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- API keys: Anthropic Claude API, Raindrop API
- Docker (optional, for containerization)

### Installation

