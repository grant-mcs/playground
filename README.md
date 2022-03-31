README for playground

## HTML Application (Via Docker)

The [html-app](/html-app) is a bare-bones HTML website
that is launched through docker (internally running nginx).
This aligns with [pass-offline-docker](https://github.com/OA-PASS/pass-offline-docker)
as a site that `hosts a single HTML file that displays that PASS is offline.`

To build the application locally you will need [Docker Deskop](https://www.docker.com/products/developer-tools/)

```bash
cd html-app && \
  docker build -t hello-world .
```

To launch a build container, run

```bash
docker run -p 8080:80 hello-world
```

And then you can visit http://127.0.0.1:8080

![HTML App running in browser](/docs/assets/html_app_nginx.png)
