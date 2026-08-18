# CrewAI M2MCent Tools Integration

Official CrewAI multi-agent integration connecting autonomous agent teams to **1,005 specialized MCP micro-services** via the **M2MCent API Gateway** (`https://api.m2mcent.com`) on **Base Mainnet**.

## 🚀 Quickstart

```python
from crewai import Agent, Task, Crew

# 1. Define autonomous agents with M2MCent MCP endpoints
analyst = Agent(
    role="DeFi Risk Specialist",
    goal="Evaluate credit risk and liquidity parameters.",
    mcps=[
        "https://api.m2mcent.com/credit-risk-mcp/sse",
        "https://api.m2mcent.com/uniswap-pool-stats-mcp/sse"
    ],
    verbose=True
)

# 2. Run multi-agent crew
task = Task(description="Analyze credit risk for address 0xDb48... on Base", agent=analyst, expected_output="JSON risk score")
crew = Crew(agents=[analyst], tasks=[task])
crew.kickoff()
```

## 🛠️ Features
- **1,005 Plug-and-Play Tools:** DeFi, security auditing, bioinformatics, 3D processing, NLP.
- **x402 Micropayment Protocol:** Trustless USDC settlement on Base Mainnet (`0xDb48F51A2de8F4a80CD1d0BAdcd18E847734A74a`).
