FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .


CMD ["python", "app.py"]
CMD ["streamlit", "run", "web/home.py"]


EXPOSE 8501