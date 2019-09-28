echo/ "start deploy ..."
cd /
mkdir -p hot-list || exit 1
cd hot-list
curl -o docker-compose.yml https://raw.githubusercontent.com/guygubaby/hot-list/master/docker-compose.yml
docker-compose up -d
echo "service start successful :)"