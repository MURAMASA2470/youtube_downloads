FROM python:3

ARG COMMIT_HASH

COPY requirements.txt ./

RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get install -y ffmpeg \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

RUN wget https://github.com/ytdl-org/youtube-dl/archive/${COMMIT_HASH}.zip \
    && unzip -n ${COMMIT_HASH}.zip && cd youtube-dl-${COMMIT_HASH} \
    && python -m pip uninstall -y youtube_dl && python -m pip install . \
    && cd .. && rm -r youtube-dl-${COMMIT_HASH}