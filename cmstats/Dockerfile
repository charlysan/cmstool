FROM alpine

RUN apk add --no-cache libpng freetype libstdc++ python py-pip
RUN apk add --no-cache --virtual .build-deps \
	    gcc \
	    build-base \
	    python-dev \
	    libpng-dev \
	    musl-dev \
	    freetype-dev
RUN ln -s /usr/include/locale.h /usr/include/xlocale.h \
	&& pip install numpy \
	&& pip install matplotlib \
	&& apk del .build-deps
WORKDIR /opt/cmstats
ADD . /opt/cmstats
RUN pip install -r requirements.txt
EXPOSE 8888
ENTRYPOINT [ "python", "./cmstats_cli.py" ]

