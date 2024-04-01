ARG NODE_VERSION=20.12.0-alpine3.18

# the image we want to use
FROM node:${NODE_VERSION}
LABEL maintainer="mutuakennedy.crunchgarage.com"

# Create our woking directory
RUN mkdir -p /frontend

# Set created directory as our working directory
WORKDIR /frontend

COPY package.json /frontend

RUN set -ex && \
    yarn

COPY . .

EXPOSE 5173

CMD ["yarn", "dev"]