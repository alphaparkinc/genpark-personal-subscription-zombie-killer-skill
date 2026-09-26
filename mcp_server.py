import json, sys
from client import PersonalSubscriptionZombieKillerClient

def handle_mcp_request(payload):
    method = payload.get("method")
    req_id = payload.get("id", 1)
    if method == "initialize":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"protocolVersion": "2024-11-05", "serverInfo": {"name": "personal-subscription-zombie-killer", "version": "1.0.0"}}}
    elif method == "tools/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": [{"name": "audit_subscription_zombies", "description": "Audits recurring personal subscriptions, detects dormant zombie services, and calculates annual recovered savings."}]}}
    elif method == "tools/call":
        client = PersonalSubscriptionZombieKillerClient()
        res = client.audit_subscription_zombies()
        return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
    return {"jsonrpc": "2.0", "id": req_id, "result": {"status": "ACTIVE"}}

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print(json.dumps(handle_mcp_request({"method": "tools/list"})))
    else:
        client = PersonalSubscriptionZombieKillerClient()
        print(json.dumps(client.audit_subscription_zombies(), indent=2))
