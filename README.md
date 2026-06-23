# ASTRA Friction Tester (M2M Client)

A lightweight Python client designed to interface with the `api.robotaxis.ch` Autonomous Data Node. This script validates the topological friction algorithm for Level 4 routing in the DACH region based on ASTRA guidelines.

## Overview
Autonomous vehicles operating in alpine environments face significant signal degradation and topological friction. This client pings the Swiss infrastructure node to retrieve deterministic routing scores based on altitude.

## Usage

### Prerequisites
- Python 3.7+
- `requests` library (`pip install requests`)

### Execution
Run the script to simulate routing requests at various altitudes (e.g., Zurich baseline vs. alpine passes).

```bash
python test_astra_friction.py
