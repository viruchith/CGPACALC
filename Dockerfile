FROM nginx:1.25.3-alpine

COPY nginx.conf /etc/nginx/nginx.conf

# RUN nginx -s reload -c /etc/nginx/nginx.conf

COPY ./build/ /usr/share/nginx/html

EXPOSE 80
