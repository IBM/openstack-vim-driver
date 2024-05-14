FROM python:3.10-alpine

ARG DRIVER_PORT
ENV DRIVER_PORT ${DRIVER_PORT:-8292}
ARG NUM_PROCESSES
ENV NUM_PROCESSES ${NUM_PROCESSES:-4}

COPY whls/*.whl /whls/

RUN addgroup -S ovd \
 && adduser -S ovd -G ovd -u 101 \
 # set group to 0 to allow arbitrary users in OCP to write to these directories
 && chown -R ovd:0 /home/ovd \
 && chmod -R 775 /home/ovd \
 && mkdir -p /var/ovd \
 # set group to 0 to allow arbitrary users in OCP to write to these directories
 && chown -R ovd:0 /var/ovd \
 && chmod -R 775 /var/ovd \
 && apk add --no-cache bash binutils libc-dev \
 # These packages need to be installed so that we can install the Python dependencies.
 # We make this virtual so that we can remove them later
 && apk add --no-cache --virtual .build-deps gcc musl-dev libffi-dev openssl-dev python3-dev make git cargo \
 && for i in /whls/ignition*.whl; do if [ "$i" != "/whls/ignition*.whl" ]; then pip install --no-warn-script-location "$i"; fi done \
 && for i in /whls/*.whl; do pip install "$i"; done \
 && apk del .build-deps gcc musl-dev libffi-dev openssl-dev python3-dev make git

USER ovd
WORKDIR /home/ovd

EXPOSE 8292

CMD if [ $SSL_ENABLED | tr [:upper:] [:lower:] == "true" ]; then SSL="--certfile /var/ovd/certs/tls.crt --keyfile /var/ovd/certs/tls.key" ; fi \
&& gunicorn -k uvicorn.workers.UvicornWorker --workers $NUM_PROCESSES --bind :$DRIVER_PORT $SSL "osvimdriver:create_wsgi_app()"