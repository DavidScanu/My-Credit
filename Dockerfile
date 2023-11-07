FROM continuumio/miniconda3

WORKDIR /home/app
COPY requirements.txt .

RUN pip install -r requirements.txt
RUN pip install streamlit --upgrade

COPY . .

CMD streamlit run app.py --server.port $PORT