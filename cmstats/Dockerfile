FROM python:3.8-slim
RUN pip install --no-cache-dir matplotlib==3.3.2 pandas

WORKDIR /opt/cmstats
ADD . /opt/cmstats
RUN pip install -r requirements.txt
EXPOSE 8888
ENTRYPOINT [ "python", "./cmstats_cli.py" ]

