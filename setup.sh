dockerImageName='guygubaby/hotlist-server:latest'

docker build -t $dockerImageName .
docker push $dockerImageName
echo "server ok"