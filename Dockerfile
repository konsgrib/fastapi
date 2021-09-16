FROM continuumio/miniconda3

WORKDIR /app

# Create the environment:
COPY spec-file.txt .
RUN conda create --name myenv --file spec-file.txt

# Make RUN commands use the new environment:
RUN echo "conda activate myenv" >> ~/.bashrc
SHELL ["/bin/bash", "--login", "-c"]

# Demonstrate the environment is activated:
RUN echo "FastAPI is installed:"
RUN python -c "import fastapi"

# The code to run when container is started:
COPY . ./
RUN ["chmod", "+x", "./entrypoint.sh"]
ENTRYPOINT ["./entrypoint.sh"]
