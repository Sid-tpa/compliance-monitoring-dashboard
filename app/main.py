from fastapi import FastAPI
app = FastAPI(title="Compliance Monitoring Dashboard")
@app.get("/api/v1/compliance/metrics")
def metrics(): return {"toxicity":0.02,"bias":0.01,"hallucination":0.03,"compliance_score":98.5}
@app.get("/health")
def health(): return {"monitoring":"active","alerts":2}
