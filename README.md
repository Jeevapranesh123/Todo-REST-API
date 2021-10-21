# Todo-REST-API

Simple REST API for a Basic ToDo App using FastAPI and Mongodb

### Steps to run the API

1. Install Docker Engine [For Windows](https://docs.docker.com/desktop/windows/install/) , [For MacOSX](https://docs.docker.com/desktop/mac/install/) , [For Ubuntu](https://docs.docker.com/engine/install/ubuntu/)

2. Install Docker Compose [For Ubuntu](https://docs.docker.com/compose/install/)

```
Note: Docker Compose Comes Default with Docker Desktop for Windows and MacOSX
```

3. Clone this Repository and cd /to/the/repository

4. Run `docker-compose up`

5. You should be able to see the Container getting build and once Built you should be able to see the container Logs

6. Once the build is done and the containers are up in running head to [Localhost](http://127.0.0.1:8008/test) in you Computer Browser or Postman

7. You should be able to see the following response.

```
{
    "Message":"Hurray you are now connected to MongoDB",
    "Api_Status":"Up",
}
```
8. That's it You are Good to go!

9. Head over to [Wiki](https://github.com/Jeevapranesh123/Todo-REST-API/wiki) Section of this Repository for API Documentation.

10. Report Bugs to `jeevadev02@gmail.com`

## API Testing

1. Find the Postman Export in the repository and Once the Docker Compose is Up Send the Reqests to localhost at port `8008`.

2. Refer to the [Localhost](http://127.0.0.1:8008) for the Documentation

3. Similarly head to [Docs](http://127.0.0.1:8008/docs) for Further Documentation.
