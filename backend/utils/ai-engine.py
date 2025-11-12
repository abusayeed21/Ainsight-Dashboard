# backend/utils/ai_engine.py
import os
from typing import Dict

# First: default integration for OpenAI. You can replace with local LLM hooks.
OPENAI_KEY = os.getenv('OPENAI_API_KEY')

try:
    import openai
    openai.api_key = OPENAI_KEY
except Exception:
    openai = None

async def analyze_metrics_text(metrics: Dict) -> str:
    """Send a prompt to OpenAI (or return a simple heuristic if no API key).
    Produces a short, actionable insight string.
    """
    text = f"Server metrics snapshot:\n{metrics}\nProvide concise anomalies, predictions, and steps to debug."
    if openai and OPENAI_KEY:
        resp = openai.ChatCompletion.create(
            model='gpt-4o-mini' if 'gpt-4o-mini' in openai.__dict__ else 'gpt-4o',
            messages=[{"role": "user", "content": text}],
            max_tokens=300,
        )
        try:
            return resp['choices'][0]['message']['content'].strip()
        except Exception:
            return 'AI service error: could not parse response.'
    # Fallback heuristic analysis (no external API)
    cpu = metrics.get('cpu_percent', 0)
    disk = metrics.get('disk', {}).get('percent', 0)
    mem = metrics.get('memory', {}).get('percent', 0)
    insights = []
    if cpu > 80:
        insights.append(f'High CPU: {cpu}% — investigate top processes or cron jobs.')
    if mem > 85:
        insights.append(f'High Memory usage: {mem}% — look for memory-hungry apps.')
    if disk > 90:
        insights.append(f'Low disk space: {disk}% used — clean logs or expand disk.')
    if not insights:
        insights.append('System operating within normal parameters.')
    return '\n'.join(insights)
