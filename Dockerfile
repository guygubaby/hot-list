FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
ENV UWSGI_INI uwsgi.ini
ENV MODE production
WORKDIR /top-list
COPY requirements.txt /
RUN pip install --no-cache-dir -U pip -i https://pypi.tuna.tsinghua.edu.cn/simple \
    && pip install --no-cache-dir -r /requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple \
    && apk add curl
COPY . .
EXPOSE 5000