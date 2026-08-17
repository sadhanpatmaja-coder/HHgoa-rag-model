from src.guardrails import apply_guardrails

def test_guardrails():
    assert "cannot answer" in apply_guardrails("random", [], "answer")