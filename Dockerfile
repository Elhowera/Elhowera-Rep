FROM python:3.9-slim


WORKDIR /app


COPY main.py /app/
COPY paragraphs.txt /app/

RUN pip install --no-cache-dir nltk
RUN python -c "import nltk; nltk.download('punkt')"

CMD ["python", "main.py"]