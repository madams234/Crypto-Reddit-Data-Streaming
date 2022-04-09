
#start kafka source connection from reddit

    #start kafka cluster
    docker-compose up kafka-cluster

    #copy connector plugin to container 
    docker cp ./C0urante-kafka-connect-reddit-0.1.3.zip b8d19615ae5f:/connectors/ #use docker ps to find correct bin

    #Enter container
    docker run --rm -it -v %cd%:/tutorial --net=host landoop/fast-data-dev:cp3.3.0 bash

    #unzip file
    unzip ./C0urante-kafka-connect-reddit-0.1.3.zip

    #move into etc
    cd etc

    #edit connect-standalone.properties and kafka-connect-reddit-source.properties files
    vi connect-standalone.properties
    vi kafka-connect-reddit-source.properties

    #create topic
    kafka-topics --create --topic reddit_toppic --partitions 3 --replication-factor 1 --zookeeper 127.0.0.1:2181

    #run kafka source connector
    connect-standalone connect-standalone.properties kafka-connect-reddit-source.properties


