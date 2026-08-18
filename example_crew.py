"""
M2MCent Multi-Agent Crew Example
Demonstrates how to connect CrewAI autonomous agents to M2MCent MCP micro-services via SSE.
"""

import os
from crewai import Agent, Task, Crew, Process

# Define specialized autonomous agents with M2MCent MCP endpoints
financial_auditor = Agent(
    role="Senior DeFi & Credit Risk Analyst",
    goal="Audit smart contracts, assess credit risk, and evaluate liquidity pools.",
    backstory="You are an autonomous AI specialist with access to institutional financial oracles on Base Mainnet.",
    mcps=[
        "https://api.m2mcent.com/credit-risk-mcp/sse",
        "https://api.m2mcent.com/uniswap-pool-stats-mcp/sse",
        "https://api.m2mcent.com/smart-contract-auditor-pro-mcp/sse"
    ],
    verbose=True
)

security_sentinel = Agent(
    role="Cryptographic & ZK Security Sentinel",
    goal="Verify ZK-SNARK proofs and scan for smart contract reentrancy vulnerabilities.",
    backstory="You are an autonomous security validator utilizing M2MCent's zero-knowledge validation tools.",
    mcps=[
        "https://api.m2mcent.com/reentrancy-detector-mcp/sse",
        "https://api.m2mcent.com/zk-snark-payload-verifier-mcp/sse"
    ],
    verbose=True
)

audit_task = Task(
    description="Perform a comprehensive audit of a DeFi vault: check credit risk score, pool liquidity, and verify contract security.",
    expected_output="A structured JSON audit report detailing risk parameters and security findings.",
    agent=financial_auditor
)

# Assemble and run the Crew
crew = Crew(
    agents=[financial_auditor, security_sentinel],
    tasks=[audit_task],
    process=Process.sequential,
    verbose=True
)

if __name__ == "__main__":
    print("🚀 Launching M2MCent Autonomous Agent Crew...")
    result = crew.kickoff()
    print("\n🏆 Final Multi-Agent Output:\n", result)
