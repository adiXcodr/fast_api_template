<div align="center" class="row">
  <img src="logo.jpg" width="200"/>
</div>
<h3 align="center">FAST API TEST</h3>
<br>

## Technologies used
* Python
* Fast API
* MySql

### First-time setup
* Execute `pip install pipenv` globally
* In root directory, Execute `pipenv install`

### Running Server
* In root directory, Execute `pipenv run server`

### Installing new pip packages
* In root directory, Execute `pipenv install <package-name>`

### Updating pip packages
* In root directory, Execute `pipenv update <package-name>`

### Uninstalling old pip packages
* In root directory, Execute `pipenv uninstall <package-name>`

### Rebuild requirements.txt
* In root directory, Execute `pipenv lock --keep-outdated -d -r > requirements.txt`

### Docker
* Create image using `sudo docker build -t mydockerimage .`
* Start using `sudo docker run -d -p 9797:9797 mydockerimage`
