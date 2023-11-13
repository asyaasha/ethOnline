# sveltkit docker image
# Build: docker build -t sveltkit .
from node:16.14.0 as build
WORKDIR /app
COPY package.json .
COPY package-lock.json .
RUN npm install
COPY . .
CMD ["npm", "run", "dev"]