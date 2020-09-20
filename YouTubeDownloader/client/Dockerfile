FROM node:12.16.1 

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

CMD ["npm","start"]



#FROM node:lts-slim as install

#WORKDIR /app

#COPY . . 

#RUN npm install 

#RUN npm run build

#CMD npm run start

#FROM nginx:alpine

#COPY --from=install /app/public /usr/share/nginx/html
#EXPOSE 80
#CMD ["nginx","-g","daemon off;"]



