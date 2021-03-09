FROM python:3.8

EXPOSE 8000

COPY . .

RUN ls /app

RUN pip install -r requirements.txt

# COPY ./app /app

WORKDIR /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]