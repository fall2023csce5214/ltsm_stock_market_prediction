FROM ubuntu:latest as compilesys

WORKDIR "/lstm"

COPY lstm_stock_market_prediction /lstm/lstm_stock_market_prediction
COPY ./tests /lstm/tests
COPY ./poetry.lock /lstm/poetry.lock
COPY ./pyproject.toml /lstm/pyproject.toml
COPY ./docker-entrypoint.sh /lstm/docker-entrypoint.sh

RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y \
    make \
    build-essential \
    libssl-dev \
    zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    wget \
    curl \
    llvm \
    libncurses5-dev \
    libncursesw5-dev \
    xz-utils \
    tk-dev \
    libffi-dev \
    liblzma-dev \
    git

# Install pyenv
RUN git clone https://github.com/pyenv/pyenv.git .pyenv
ENV HOME  /lstm
ENV PYENV_ROOT $HOME/.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH
RUN pyenv install 3.9.5
RUN pyenv global 3.9.5
RUN eval "$(/pyenv/bin/pyenv init -)"

# Install poetry
RUN curl -sSL https://install.python-poetry.org | python -
ENV PATH="/lstm/.local/bin:$PATH"
RUN poetry install
RUN poetry run pip install tensorflow==2.13.0

ENTRYPOINT ["sh", "/lstm/docker-entrypoint.sh"]