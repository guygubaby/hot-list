FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
ENV UWSGI_INI uwsgi.ini
WORKDIR /top-list
COPY requirements.txt /
RUN pip install --no-cache-dir -U pip \
    && RUN pip install --no-cache-dir -r /requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
COPY . .
EXPOSE 5000
#ENTRYPOINT [""]