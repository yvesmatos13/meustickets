FROM python:latest

WORKDIR /app
 
COPY ./ ./

RUN pip install --root-user-action=ignore --upgrade pip

RUN pip install --root-user-action=ignore --no-cache-dir --upgrade -r requirements.txt

RUN rm requirements.txt Dockerfile

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]