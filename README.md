# Coffee Shop Full Stack



This project is full stack drink menu application where the user can:

1) Display graphics representing the ratios of ingredients in each drink.
2) Allow public users to view drink names and graphics.
3) Allow the shop baristas to see the recipe information.
4) Allow the shop managers to create new drinks and edit existing drinks.

## Getting Started
------------------
### Prerequisites
- Python3
- PIP
- Node
### Backend
---------
**Virtual Environment**
- Create a Virtual Environment in backend directory
```bash
python3 -m venv /path/to/new/virtual/environment
```
- Activate venv
```bash
$ source <venv>/bin/activate
```
> [Creation and Activation of virtual environments](https://docs.python.org/3/library/venv.html)

**PIP Dependencies**

Now you have your venv created and activated, navigate to the ```/backend``` directory and run the following command to install all required packages:

```bash
pip install -r requirements.txt
```


**Running the server**
```bash
export FLASK_APP=api.py
flask run --reload
```
The --reload flag will detect file changes and restart the server automatically.
### Frontend
-------------
**Installing Node and NPM**

Install Node and NPM from https://nodejs.org/en/download.

**Installing project dependencies**

in ```/frontend```, run the following command to install the required packages:

```bash
npm install
```
**Running the frontend**

```bash
ionic serve
```
By default, the frontend will run on ```127.0.0.1:8100```
### Postman testing
----------------------
Download Postman: https://www.postman.com/downloads/
- Open postman after installation
- Import the following Postman collection: ```./starter_code/backend/udacity-fsnd-udaspicelatte.postman_collection.json```
- Run the collection


