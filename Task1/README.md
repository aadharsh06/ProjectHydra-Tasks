# Task1-C

## Objective
The core objectives were to set up a basic server and a monitoring system through Docker, Prometheus and Grafana. Containerization of microservices, using Prometheus and Grafana, and finally bringing everything together using Docker compose were also demonstrated in this task.


## Steps / Implementation

First, I activate my python venv to install pip packages.
`python3 -m venv venv`  
`source venv/bin/activate`

Next, I write a python script using FastAPI, creating the server, according to the requirements, and containerize it using a dockerfile.
I use uvicorn to run it, exposing it at port 8080.
Name of service: **hydrabase**

I use `prometheus_client` in python to write code to scrape and set values in Prometheus format in a separate port, here I used 8600.
`requests` I have used before, hence I knew how to work with it to scrape data from hydrabase.
Name of service: **pyexporter**

At this point, I connected both services by creating a docker compose YAML and using a network, **hydra-net**.

Now I had to pull and run the Prometheus and configure a yml file to get data from pyexporter's port and store it in a timeseries format. 
I set the delay to 10s. I exposed this on 9090 (This was the port used in the docs, so I stuck with it). I updated my docker compose to include this as well.
Name of service: **prometheus**

Finally, was Grafana's connection to the prometheus service. I directly integrated grafana to the compose YAML (courtesy of grafana's docs), and exposed it on port 3000.
I used the UI to create the connection to prometheus and created the three dashboards for each of the metrics.
Name of service: **grafana**

Added volumes for hydrabase and pyexporter.
Final step was committing the changes to GitHub. 

## Observations

Running docker compose: 
`(venv) aadharsh-venkat@aadharsh-venkat-IdeaPad-Slim-3-15AMN8:~/proj-hydra/Task1$ docker compose up`
[+] Running 5/5
 ✔ Network task1_hydra-net       Created                                                                                                    0.1s 
 ✔ Container task1-hydrabase-1   Created                                                                                                    0.1s 
 ✔ Container grafana             Created                                                                                                    0.1s 
 ✔ Container task1-pyexporter-1  Created                                                                                                    0.1s 
 ✔ Container task1-prometheus-1  Created                                                                                                    0.1s `
 ...
hydrabase-1   | INFO:     172.19.0.4:58774 - "GET /health HTTP/1.1" 200 OK
hydrabase-1   | INFO:     172.19.0.4:58788 - "GET /metrics HTTP/1.1" 200 OK
hydrabase-1   | INFO:     172.19.0.4:58792 - "GET /simulate_failure HTTP/1.1" 200 OK
hydrabase-1   | INFO:     172.19.0.4:41734 - "GET /health HTTP/1.1" 200 OK
hydrabase-1   | INFO:     172.19.0.4:41738 - "GET /metrics HTTP/1.1" 200 OK
hydrabase-1   | INFO:     172.19.0.4:41754 - "GET /simulate_failure HTTP/1.1" 200 OK
...

## Issues Faced & Fixes
- My main issue was with the ports, which I had to troubleshoot for quite a while. Getting everything to work by connecting on the right ports.
- I directly tried to connect pyexporter to grafana, which did not work. Then I learnt that Grafana needed a full fledged Prometheus API, which I later implemented.


