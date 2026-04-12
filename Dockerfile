FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY llm_eval/ ./llm_eval/

CMD ["python3", "-m", "llm_eval.evaluator"]
