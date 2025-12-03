
# Task 0

All packages were successfully installed and I have uploaded the screenshot in the repo.

Coming to the app and dockerization, the first thing I did was create the app using `fastapi` in python. Created a docker file for the same.

Since my ubuntu did not allow a system wide pip install, due to a `PEP 668` error, I created a virutual env, in which I installed all required python packages.

Creating and activating the venv:\
`python3 -m venv venv`\
`source venv/bin/activate`

Building the dockerfile and running it,\
`docker build -t server .`\
`docker run -p 8000:8000 server`


