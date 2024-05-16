FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["bash", "run.sh"]
EXPOSE 7755