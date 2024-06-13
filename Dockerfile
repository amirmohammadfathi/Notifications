FROM python
LABEL MAINTAINER="AmirMohammadFathi"
ENV PYTHONUNBUFFERD=TRUE
ENV TZ=Asia/Tehran
RUN apt-get -y update && apt-get -y upgrade && apt-get install vim -y
WORKDIR /notif
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY requirements.txt requirements.txt
RUN python -m pip install --upgrade pip && pip install -r requirements.txt
COPY . .
CMD ["sh", "entrypoint.sh"]
