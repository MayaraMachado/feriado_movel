#!/bin/bash

sudo docker login --username $HEROKU_DOCKER_USERNAME --password $HEROKU_AUTH_TOKEN registry.heroku.com
sudo docker tag verifica-feriado:latest registry.heroku.com/verifica-feriadwebo
if [ $TRAVIS_BRANCH == "master" ] && [ $TRAVIS_PULL_REQUEST == "false" ]; then sudo docker push registry.heroku.com/verifica-feriado/web; fi

chmod +x heroku-container-release.sh
sudo chown $USER:docker ~/.docker
sudo chown $USER:docker ~/.docker/config.json
sudo chmod g+rw ~/.docker/config.json

./heroku-container-release.sh