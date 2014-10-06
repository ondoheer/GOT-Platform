!#/usr/bin/bash

echo 'Deploying GOT platform'
cd $PWD

echo '#################################'
echo 'conecting to Linode and deploying'
echo '#################################'
rsync -avz * 50.116.30.151:/var/www/codingwesteros.com/