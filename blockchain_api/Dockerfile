FROM node:14.5-slim

ENV APP /usr/src/app
RUN mkdir $APP
WORKDIR $APP
COPY package* $APP/

RUN npm i

COPY . $APP/
CMD ["node", "start"]
