FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
ENV FLASK_APP=todo_project
ENV IP_APPLICATION=0.0.0.0
ENV SECRET_KEY=45cf93c4d41348cd9980674ade9a7356
CMD ["python", "todo_project/run.py"]