import json

def load_fake_profile(name):
    with open('data/fake_profiles.json', 'r') as f:
        profiles = json.load(f)
    return profiles.get(name, {})
