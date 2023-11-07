FROM continuumio/miniconda3

WORKDIR /home/app
COPY requirements.txt .

RUN pip install -r requirements.txt
RUN pip install streamlit --upgrade

COPY . .

RUN python -m unittest -v test.py

CMD streamlit run app.py --server.port $PORT