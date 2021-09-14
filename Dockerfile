FROM python:alpine3.14
ADD . /app
RUN pip install fastapi uvicorn requests
EXPOSE 80
WORKDIR /app
ENTRYPOINT [ "uvicorn","web:app" ]
CMD [ "--host","0.0.0.0","--port","80" ]