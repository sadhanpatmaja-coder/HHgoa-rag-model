from src.pipeline import run_pipeline

def test_pipeline():
    result = run_pipeline("sample.wav")
    assert isinstance(result, str)
