from agents.manager_agent import generate_summary

intent_output = """
Category: VPN Connectivity
Priority: High
Business Impact: Remote work blocked.
Recommendation: Assign to Network Team.
SLA: 4 Hours
"""

solution = "Restart VPN client and reconnect."

ticket_id = "INC123456"

result = generate_summary(
    intent_output,
    solution,
    ticket_id
)

print(result)