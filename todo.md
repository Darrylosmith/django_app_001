0. Setup this project in GitHub
1. Add a model for a Band in addition to musician
    - enhance model for musician to have a foreign key to the band
2. Get the ./manage.py runserver call working in the docker entrypoint.sh script
3. Setup Django Rest Framework and expose /api/musician and /api/band/ as webservice endpoints
4. Setup an Angular frontend app, and read data from the above endpoints
    - print to console
    - print to HTML/WebUI in angular using data provided from webservice
5. Authenticate with Google Social Authentication
6. Setup a better-than-sqlite database, such as postgres
    - use docker!
    - use AWS RDS!

