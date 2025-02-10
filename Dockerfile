FROM python:3.13

WORKDIR /main

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8501

CMD ["streamlit","run","main.py","--server.port=8501","--server.address=0.0.0.0"]