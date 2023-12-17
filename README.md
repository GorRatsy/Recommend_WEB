# Recommendation web-service
The main goal of this project was to create web-servie that will allow to make prediction for each user from the database.
Database contains information about users' activity and desription about all products.

## Model building
The basement of recommend system is [KNNBasic-algorithm from Surprise-libruary](https://surprise.readthedocs.io/en/stable/knn_inspired.html#surprise.prediction_algorithms.knns.KNNBasic)

## Web-service
The basement of web-service is Flask. All components of pages are in templates (html) and static folders.

# Try service
If you want to try it please use docker. 
The image is [here](https://hub.docker.com/repository/docker/gorratsy/rec_sys/general)
