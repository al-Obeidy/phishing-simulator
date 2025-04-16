from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

def generate_phishing_message(context):
    prompt = f"Based on this context: {context}, write a spear phishing email."
    return generator(prompt, max_length=100)[0]['generated_text']
