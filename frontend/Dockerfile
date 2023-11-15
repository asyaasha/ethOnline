# sveltkit docker image
# Build: docker build -t sveltkit .
from node:16.14.0 as build
WORKDIR /app
COPY package.json .
COPY package-lock.json .
ENV AGENT_URL=agent.station.codes
ENV GRAFANA_URL=grafana.station.codes
RUN npm install
COPY . .
CMD ["npm", "run", "build"]