import pytest
from src.osint.collector import load_fake_profile

def test_load_fake_profile():
    profile = load_fake_profile("Ahmed Ali")
    assert profile is not None
    assert isinstance(profile, dict)
    assert "job" in profile
