# CrewAI M2MCent Tools Integration

[![PyPI version](https://img.shields.io/pypi/v/crewai-plugin-x402.svg)](https://pypi.org/project/crewai-plugin-x402/)
[![Vouch Protocol Grade A](https://img.shields.io/badge/Vouch_Trust_Index-Grade_A_(100%2F100)-00ff88?style=flat-square)](https://vouch-protocol.com/agent-trust-index/)
[![Base Mainnet](https://img.shields.io/badge/Settlement-Base_Mainnet_(USDC)-0052FF?style=flat-square)](https://basescan.org)
[![Post-Quantum Ready](https://img.shields.io/badge/Post--Quantum-ML--DSA--65_(FIPS_204)-purple?style=flat-square)](https://csrc.nist.gov/pubs/fips/204/final)

Official CrewAI multi-agent integration connecting autonomous agent teams to **1,062 specialized MCP micro-services** (896 flagship deterministic in-memory engines) via the **M2MCent API Gateway** (`https://api.m2mcent.com`) on **Base Mainnet**.

## 🚀 Quickstart

```python
from crewai import Agent, Task, Crew

# 1. Define autonomous agents with M2MCent MCP endpoints
analyst = Agent(
    role="DeFi Risk Specialist",
    goal="Evaluate credit risk and liquidity parameters.",
    mcps=[
        "https://api.m2mcent.com/credit-risk-mcp/sse",
        "https://api.m2mcent.com/autonomous-trading-bot-mcp/sse"
    ],
    verbose=True
)

# 2. Run multi-agent crew
task = Task(description="Analyze credit risk and live indicators on Base", agent=analyst, expected_output="JSON risk score")
crew = Crew(agents=[analyst], tasks=[task])
crew.kickoff()
```

## 🛠️ Features & Contracts
- **1,062 Plug-and-Play Tools:** DeFi, quantitative trading, cryptography, bioinformatics, 3D processing, NLP.
- **x402 Micropayment Settlement:** Trustless USDC settlement on Base Mainnet (`0x5d47070A36A37DAf417e64FF27a1e5B3F1c84efa`).
- **Multi-Sig Safe Treasury:** `0x8aaBAB75bE8825d0f5D514a9a5cBa04B7bF84920`.
- **Vouch Trust Index:** Grade A (100/100).
- **Post-Quantum Cryptography:** FIPS 204 ML-DSA-65 readiness.
