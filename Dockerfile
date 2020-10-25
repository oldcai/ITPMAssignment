#FROM mirror.ccs.tencentyun.com/oldcai/sky_base:latest
FROM mirror.ccs.tencentyun.com/library/python:3.8
#FROM 4brp6gm1.mirror.aliyuncs.com/library/python:3.7
RUN mkdir /code/
WORKDIR /code/
ADD . /code/
RUN sed -i 's/deb.debian.org/mirrors.tencentyun.com/g' /etc/apt/sources.list && \
    sed -i 's/security.debian.org/mirrors.tencentyun.com/g' /etc/apt/sources.list && \
    apt update && \
    apt install -y gconf-service libasound2 libatk1.0-0 libc6 libcairo2 libcups2 \
    libdbus-1-3 libexpat1 libfontconfig1 libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 \
    libglib2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 \
    libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxext6 \
    libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 ca-certificates \
    fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils wget
RUN bash /code/scripts/init.sh

ENV PYTHONUNBUFFERED 1

# uWSGI will listen on this port
EXPOSE 8000

# Add any custom, static environment variables needed by Django or your settings file here:
ENV DJANGO_SETTINGS_MODULE=itpm.settings

CMD ["/code/scripts/runserver.sh"]
