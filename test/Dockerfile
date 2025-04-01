FROM hugomods/hugo:reg-exts-0.145.0

RUN apk add gcc build-base python3-dev py3-pip

# COPY package.json /src
COPY requirements.txt /src

WORKDIR /src

# RUN git config --global --add safe.directory /src && \
#     npm install
RUN git config --global --add safe.directory /src

RUN python3 -m venv .venv && \
    source .venv/bin/activate && \
    pip3 install -r requirements.txt

COPY sync.py run.sh /src/

CMD ["sh", "run.sh"]
