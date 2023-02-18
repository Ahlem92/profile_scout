FROM python:3.8.12-buster


COPY profile_scout /profile_scout
COPY requirements_prod.txt /requirements.txt
COPY setup.py /setup.py

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD uvicorn profile_scout.api.fast:app --host 0.0.0.0 --port $PORT
