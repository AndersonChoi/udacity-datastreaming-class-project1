# Optimizing-Public-Transportation
Udacity data stream project01

## PROJECT SPECIFICATION

### Kafka Producer

Kafka topics are created with appropriate settings
> Using the Kafka Topics CLI, topics appear for arrivals on each train line in addition to the turnstiles for each of those stations.

Kafka messages are produced successfully
> Using the Kafka Topics CLI, messages continuously appear for each station on the train line, for both arrivals and turnstile actions.

All messages have an associated value schema
> Using the Schema Registry API, a schema is visible for arrivals and turnstile events.

### Kafka Consumer

Messages are consumed from Kafka
> Stations, status, and weather data appear and update in the Transit Status UI.

Stations data is consumed from the beginning of the topic
> All Blue, Green, and Red Line stations appear in the Transit Status UI.

### Kafka REST Proxy

Kafka REST Proxy successfully delivers messages to the Kafka Topic
> Using the kafka-console-consumer, weather messages are visible in the weather topic and are regularly produced as the simulation runs.

Messages produced to the Kafka REST Proxy include a value schema
> Using the Kafka Schema Registry REST API, a schema is defined for the weather topic.

### Kafka Connect

Kafka Connect successfully loads Station data from Postgres to Kafka
> Using the kafka-console-consumer, all stations defined in Postgres are visible in the stations topic.

Kafka Connect is configured to define a Schema
> Using the Kafka Connect REST API, the Kafka Connect configuration is configured to use JSON for both key and values.
> Using the Schema Registry REST API, the schemas for stations key and value are visible.

Kafka Connect is configured to load on an incrementing ID
> Using the Kafka Connect REST API, the Kafka Connect configuration uses an incrementing ID, and the ID is configured to be stop_id.

### Faust Streams

The Faust application ingests data from the stations topic
> A consumer group for Faust is created on the Kafka Connect Stations topic.

Data is translated correctly from the Kafka Connect format to the Faust table format
> Data is ingested in the Station format and is then transformed into the TransformedStation format.

Transformed Station Data is Present for each Station ID in the Kafka Topic
> A topic is present in Kafka with the output topic name the student supplied. Inspecting messages in the topic, every station ID is represented.

### KSQL

Turnstile topic is translated into a KSQL Table
> Using the KSQL CLI, turnstile data is visible in the table TURNSTILE.

Turnstile table is aggregated into a summary table
> Using the KSQL CLI, verify that station IDs have an associated count column.
