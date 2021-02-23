FROM python:3.8
ADD ./flask_app /app
WORKDIR /app
RUN pip3 install -r requirements.txt
EXPOSE 8080
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app"]