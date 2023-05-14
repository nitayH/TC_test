RUN mkdir /app 
COPY test.py /app
COPY read_envs.sh /app
WORKDIR /app

RUN pytest test.py
RUN read_envs.sh
