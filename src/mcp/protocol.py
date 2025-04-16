from src.osint.collector import load_fake_profile
from src.context_analysis.analyzer import analyze_text
from src.phishing_generator.generator import generate_phishing_message
from src.risk_analysis.evaluator import evaluate_message

def run_pipeline(target_name):
    profile = load_fake_profile(target_name)
    context = analyze_text(profile.get('bio', ''))
    message = generate_phishing_message(context)
    risk = evaluate_message(message)
    return {
        "profile": profile,
        "context": context,
        "message": message,
        "risk": risk
    }  
