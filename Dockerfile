# 
FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1 
ENV MODE "PRODUCTION"
EXPOSE 9797
# 
WORKDIR /app

#Copy pipfile to the directory
COPY ./Pipfile .

# Install pipenv and compilation dependencies
RUN pip install pipenv
RUN apt-get update && apt-get install -y --no-install-recommends gcc

RUN pipenv install
# RUN pipenv install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy everything from ./src directory to /app in the container
COPY . . 

# RUN pip install -r requirements.txt
CMD ["pipenv","run", "server"]
