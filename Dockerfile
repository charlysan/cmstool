FROM python:2.7.15-alpine
WORKDIR /opt/cmstool
ADD . /opt/cmstool
RUN pip install -r requirements.txt
ENTRYPOINT [ "python", "./cmscraper_cli.py" ]
