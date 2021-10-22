FROM python:3.9.7

WORKDIR /usr/src/app

COPY . .

ENTRYPOINT ["python3"]

CMD ["game.py"]
