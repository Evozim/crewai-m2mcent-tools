# CrewAI M2MCent Tools Integration (v1.0.3)

[![PyPI version](https://img.shields.io/pypi/v/crewai-plugin-x402.svg)](https://pypi.org/project/crewai-plugin-x402/)
[![Vouch Protocol Grade A](https://img.shields.io/badge/Vouch_Trust_Index-Grade_A_(100%2F100)-00ff88?style=flat-square)](https://vouch-protocol.com/agent-trust-index/)
[![Base Mainnet](https://img.shields.io/badge/Settlement-Base_Mainnet_(USDC)-0052FF?style=flat-square)](https://basescan.org)
[![Post-Quantum Ready](https://img.shields.io/badge/Post--Quantum-ML--DSA--65_(FIPS_204)-purple?style=flat-square)](https://csrc.nist.gov/pubs/fips/204/final)

Official CrewAI multi-agent integration connecting autonomous agent teams to **1,057 deterministic MCP micro-services** (`$0.010`–`$0.250` USDC, `<250ms` compute SLA) via the **M2MCent API Gateway** (`https://api.m2mcent.com`) on **Base Mainnet (`eip155:8453`)**.

## 🚀 Installation & Quickstart

```bash
pip install crewai-plugin-x402==1.0.3
```

```python
import os
from crewai import Agent
from crewai_plugin_x402 import M2MCentCrewAITool

m2m_tool = M2MCentCrewAITool(
    endpoint_url="https://api.m2mcent.com/autonomous-trading-bot-mcp/api/process",
    private_key=os.getenv("EVM_PRIVATE_KEY")
)

analyst = Agent(
    role="DeFi Quantitative Analyst",
    goal="Execute live 50-candle Coinbase EMA-12/26/9 MACD and Wilder RSI-14 signals.",
    backstory="Institutional quantitative agent settling x402 V2 USDC micropayments on Base L2.",
    tools=[m2m_tool]
)
```

## 🛠️ Features & Contracts
- **1,057 Deterministic Tools (`<250ms` Compute SLA):** Quantitative finance, EIP-5564 cryptography, Base L2 gas telemetry, KYT/OFAC, bioinformatics, 3D spatial algorithms.
- **x402 V2 Micropayment Settlement:** Gasless EIP-3009 USDC settlement via Escrow (`0x5d47070A36A37DAf417e64FF27a1e5B3F1c84efa`).
- **Multi-Sig Safe Treasury:** `0x8aaBAB75bE8825d0f5D514a9a5cBa04B7bF84920`.
- **Vouch Trust Index:** Grade A (`100/100`) · Post-Quantum `ML-DSA-65` (FIPS 204).
