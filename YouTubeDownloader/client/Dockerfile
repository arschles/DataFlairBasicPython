FROM node:12.16.1 as install

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

CMD ["npm","start"]


