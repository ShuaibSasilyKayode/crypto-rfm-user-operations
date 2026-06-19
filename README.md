# Crypto Platform User Operations: Programmatic RFM Segmentation Engine

## Project Overview
This project builds an automated **Recency, Frequency, and Monetary (RFM)** user segmentation and retention engine designed for cryptocurrency platforms. It connects a real-time tracking data layer (Google Sheets) to a programmatic user routing script (Python) to trigger automated marketing and account management sequences.

## System Proof of Work

### 1. Live Google Sheets RFM Dashboard Prototype
![RFM Spreadsheet Dashboard](dashboard.png)

### 2. Live Python Automation Engine Execution Output
![Colab Terminal Output](terminal.png)

## Operational Lifecycle Pathways
* **Whale / VIP**: Volume threshold triggered. Dispatches webhooks directly to Account Managers for immediate premium handling.
* **Active Retail**: Highly frequent, lower volume traders. Routed to gamified interface events and trading volume tournaments.
* **At-Risk / Slipping**: Inactivity windows tracked. Automatically issues zero-fee incentive structures to minimize user churn.
