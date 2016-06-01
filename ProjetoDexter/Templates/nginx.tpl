server {
    listen 80;
    server_name {{ url_projeto }} ;

    location / {
        proxy_pass http://{{container_ip}};
    }
}
