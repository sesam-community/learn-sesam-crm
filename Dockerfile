FROM --platform=linux/amd64 python:3.7-alpine
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["service.py"]