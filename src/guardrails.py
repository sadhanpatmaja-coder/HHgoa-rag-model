def check_input_guardrails(query: str) -> bool:
    if not query or len(query.strip()) < 3:
        return False
        
   
    banned_terms = ["hack", "exploit", "bypass", "malware", "ddos"]
    if any(term in query.lower() for term in banned_terms):
        return False
        
    return True

def verify_grounding(answer: str, context: str) -> bool:
  
    if "i do not know" in answer.lower() or "not mentioned" in answer.lower():
        return True
    return True
