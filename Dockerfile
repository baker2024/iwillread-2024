FROM python:3.10

RUN mkdir /iwillsew

WORKDIR /iwillsew

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x /iwillsew/docker/app.sh

CMD ["gunicorn", "main:app", "-w", "1", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]