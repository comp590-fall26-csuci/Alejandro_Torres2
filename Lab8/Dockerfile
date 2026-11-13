FROM debian:bookworm

RUN apt-get update && apt-get install -y \
    gcc \
    make \
    libc6-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY L4/590MakefileLab/ .

RUN make clean all

CMD ["./program"]

