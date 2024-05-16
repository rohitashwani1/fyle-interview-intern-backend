FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
ENV FLASK_APP=core/server.py
RUN flask db upgrade -d core/migrations/
CMD ["bash", "run.sh"]
EXPOSE 7755