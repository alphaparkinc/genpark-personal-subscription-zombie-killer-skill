import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import PersonalSubscriptionZombieKillerClient

def main():
    client = PersonalSubscriptionZombieKillerClient()
    res = client.audit_subscription_zombies()
    print("=== Personal Subscription Zombie Killer Output ===")
    print(f"User: {res['user_name']} | Evaluated: {res['subscriptions_evaluated_count']} subs")
    print(f"Zombies Found: {res['zombie_subscriptions_detected_count']} | Monthly Bleed: ${res['monthly_recurring_bleed_usd']}/mo")
    print(f"Projected Annual Recovered Savings: ${res['projected_annual_savings_usd']}/yr")
    print("\nDormant Subscriptions Identified:")
    for z in res['zombie_candidates']:
        print(f"  * {z['service']:25s} | Dormant: {z['dormancy_days']}d | Cost: ${z['monthly_cost_usd']}/mo (${z['annualized_bleed_usd']}/yr)")

if __name__ == '__main__':
    main()
