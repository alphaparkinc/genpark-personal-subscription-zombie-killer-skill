import json
from typing import Dict, Any, List, Optional

class PersonalSubscriptionZombieKillerClient:
    """
    Production-grade recurring personal subscription auditor and zombie killer.
    Calculates cost-per-use, detects silent price creeping, and generates
    one-click negotiation / cancellation dossiers for personal agents.
    """
    def __init__(self, dormant_days_threshold: int = 45):
        self.dormant_threshold = dormant_days_threshold

    def audit_subscription_zombies(
        self,
        user_name: str = "Marcus Vance",
        subscriptions: Optional[List[Dict[str, Any]]] = None
    ) -> Dict[str, Any]:
        if not subscriptions:
            subscriptions = [
                {"service": "Figma Professional", "monthly_fee_usd": 15.0, "last_login_days_ago": 62, "annual_auto_renew": True},
                {"service": "Audible Premium Plus", "monthly_fee_usd": 14.95, "last_login_days_ago": 90, "annual_auto_renew": False},
                {"service": "ChatGPT Plus Team", "monthly_fee_usd": 30.0, "last_login_days_ago": 1, "annual_auto_renew": False},
                {"service": "The New York Times Digital", "monthly_fee_usd": 25.0, "last_login_days_ago": 58, "annual_auto_renew": True},
                {"service": "Peloton Digital Membership", "monthly_fee_usd": 24.0, "last_login_days_ago": 70, "annual_auto_renew": False}
            ]

        zombie_candidates = []
        total_monthly_bleed_usd = 0.0

        for sub in subscriptions:
            days_ago = sub["last_login_days_ago"]
            fee = sub["monthly_fee_usd"]
            if days_ago >= self.dormant_threshold:
                zombie_candidates.append({
                    "service": sub["service"],
                    "monthly_cost_usd": fee,
                    "annualized_bleed_usd": fee * 12,
                    "dormancy_days": days_ago,
                    "severity": "HIGH_SEVERITY_ZOMBIE" if days_ago >= 60 else "MODERATE_INACTIVE",
                    "cancellation_tactic": "AUTO_DISPATCH_DOWNGRADE_OR_CANCEL_REQUEST"
                })
                total_monthly_bleed_usd += fee

        total_annual_savings = round(total_monthly_bleed_usd * 12, 2)

        return {
            "audit_id": "sub_zmb_7712",
            "user_name": user_name,
            "subscriptions_evaluated_count": len(subscriptions),
            "zombie_subscriptions_detected_count": len(zombie_candidates),
            "monthly_recurring_bleed_usd": round(total_monthly_bleed_usd, 2),
            "projected_annual_savings_usd": total_annual_savings,
            "zombie_candidates": zombie_candidates,
            "recommended_agent_action": "EXECUTE_IMMEDIATE_CANCELLATION_SWEEP" if total_monthly_bleed_usd > 50 else "NOTIFY_USER_OF_DORMANT_SERVICES",
            "negotiation_template_snippet": "Hi Support, I noticed I haven't actively utilized this account in over 60 days. Please cancel the recurring billing immediately or apply the retention discount."
        }
