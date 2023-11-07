FROM  continuumio/miniconda3

WORKDIR /home/app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD uvicorn app:app --host=0.0.0.0 --port=$PORT