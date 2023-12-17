FROM ubuntu
RUN apt update
RUN apt install python3 python3-pip -y
RUN pip install joblib flask scikit-surprise pandas

EXPOSE 5000

COPY . /app
WORKDIR /app

CMD ["flask", "run", "-h", "0.0.0.0", "-p", "5000"]
