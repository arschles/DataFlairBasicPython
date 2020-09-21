FROM node:12.16.1 as install

WORKDIR /app

COPY package*.json ./

RUN npm ci
#RUN npm install

COPY . .

#CMD ["npm","start"]
RUN npm run build

#production
FROM nginx:stable-alpine
COPY --from=install /app/build /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]


