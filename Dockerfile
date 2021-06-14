FROM  python:alpine3.7
COPY . /app
WORKDIR /app
RUN apk add bash build-base
RUN pip install --upgrade pip
RUN pip install flask pandas numpy openpyxl xlrd
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]