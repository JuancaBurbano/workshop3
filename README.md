# Readme about the workshop3

## Introduction
This workshop is about an application of a prediction model, implementing a data transmission.
We have 5 csvs on happiness data for different countries and each csv is a different year, they are put together to obtain a more complete dataset. And create a prediction model with that data so that it can then be passed through a topic and saved in a database.

## Technologies used

- Python
- Jupyter Notebook
- Kafka
- Docker

## Folder architecture
- Data: folder where we have our csvs
- Kafka: folder where we will have the Kafka environment, the consumer and producer
- Models: The model that we will make in the eda with the data will be saved here
- Notebook: folder where we will have 2 main Notebooks, Eda and Métricas
- Finally we have the Docker.yml file (To run this tool)

## How to run this project?
First we must create a virtual environment with the following command:
```
python -m venv {name of your environment}
name of your environment\Scripts\activate

```
Now we will download the. Kafka application using Docker which contains our Docker yml file,
With the command:
```
Docker-compose UP - d

```
After we have the applications installed, we must install all the requirements of the libraries that are used in this project with the command
```
cd Confi
pip install -r requirements.txt

```

Now that we have installed the requirements in our environment we must do the following
- We run the eda Notebook
This eda will show us an analysis of the data and will create the model that goes in Models, and will also save the csv that we are going to send through the Kafka topic

We must also create a folder called Config which inside it will have the following json
credentials.json
and credentials2.json
Within these will be the following information

In credentials.json:
```
{
    "host" : "localhost",
    "user" : "",
    "password" : "",

}

```
And in credentials2.json:
```
{
    "host" : "localhost",
    "user" : "",
    "password" : "",
    "database" : "workshopdb1"  
}

```

Ready, now having this, let's create the topic
With the following commands in the terminal:

```
docker exec -it kafka bash
kafka-topics --bootstrap-server kafka:9092 --create --topic {topic}

```

Now we start our producer
And at the same time you see the Notebook, what do we have as a consumer?
This will apply the model and save the data in a database
To see the metrics we must run the Notebook Metrics and we will obtain the model metrics