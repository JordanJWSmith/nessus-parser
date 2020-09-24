FROM node:12-alpine

WORKDIR /srv
EXPOSE 8080

# Let Docker cache dependencies
COPY ./package*.json ./
RUN npm install

COPY . /srv

CMD ["npm", "run", "serve"]
