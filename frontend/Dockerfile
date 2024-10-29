# sveltkit docker image
# Build: docker build -t sveltkit .
from node:16.14.0 as build
WORKDIR /app
COPY package.json .
COPY package-lock.json .
ENV PUBLIC_AGENT_URL=agent.station.codes
ENV PUBLIC_GRAFANA_URL=grafana.station.codes
RUN npm install
COPY . .
CMD ["npm", "run", "build"]

FROM nginx:1.25
COPY --from=build /app/build/ /usr/share/nginx/html
# Copy the default nginx.conf provided by tiangolo/node-frontend
COPY nginx.conf /etc/nginx/conf.d/default.conf