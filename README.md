# The Universe Vault API
The Universe Vault API is a RESTful API that allows you to manage Planets, Stars, Moons, Solar Systems and Galaxies in the Universe.
It will be a major part of the future systems like StarID (Interstellar Identification System) and the Universe Explorer as well as general knownledge-database.

### Live Demo
The Universe Vault API is currently under development and there is no live demo available at the moment.

### Features
- [x] Create/Read for Planets, Stars, Moons, Solar Systems and Galaxies
- [ ] Update/Delete (full CRUD) for Planets, Stars, Moons, Solar Systems and Galaxies
- [ ] Search/Filter for Planets, Stars, Moons, Solar Systems and Galaxies
- [ ] User Authentication and Authorization
- [ ] Rate Limiting and Security
- [ ] API Documentation
- [ ] Testing and CI/CD
- [ ] Docker Deployment
- [ ] Live Demo
- [ ] More features to come...
## Codebase Note
At the moment Python3, FastAPI and MongoDB used for this project, as it makes development fast and easy, exactly what we need for concept or you can say MVP.
However in the future I'll rewrite everything to Rust-lang, and possibly will keep MongoDB as a database, tips and feedback is welcome!

## Getting Started
To get started with the Universe Vault API, you need to have the following installed on your machine (Recomended way):
- Docker (https://www.docker.com/)
- Docker Compose (https://docs.docker.com/compose/)

Manual installation is also possible, for the testing purposes, but it is not recommended for production:
- Python ^3.9 (https://www.python.org/)
- MongoDB Server (either local or in the cloud, like Atlas) (https://www.mongodb.com/)

### API Documentation 
Coming soon...

### Docker Installation (Recomended)
To install the Universe Vault API, you need to clone the repository and run the following command:
```bash
git clone https://github.com/integrityofstellar/TheUniverseVaultAPI
cd TheUniverseVaultAPI
docker-compose up
```

### Manual Installation
To install the Universe Vault API, you need to clone the repository and run the following command:
```bash
git clone https://github.com/integrityofstellar/TheUniverseVaultAPI
cd TheUniverseVaultAPI
```
We using `poetry` for the package management, you can use it to install the dependencies, or you can use `pip` as well:
```bash
poetry install
```
or
```bash
pip install -r requirements.txt
```
Then you need to set the environment variables in the `.env` file, you can use the `.env.example` file as a template.  
Also, you need to have MongoDB installed on your machine or use a cloud service like Atlas.

After installing the dependencies and database with env variables, you can activate venv and run the API using the following command:
```bash
poetry shell
uvicorn app.main:app --reload
```
or
```bash
source venv/bin/activate
uvicorn app.main:app --reload
```

Usually, the API will be running on `http://127.0.0.1:8000/` and the swagger docs will be available at `http://127.0.0.1:8000/docs`.

## Contributing
If you want to contribute to the Universe Vault API, you can fork the repository and create a pull request with your changes.
Currently, there are no guidelines for contributing, but you can follow the existing code style and structure.
