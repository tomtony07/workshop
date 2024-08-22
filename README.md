## Flask Boilerplate Code

## Steps to follow
1. `git clone https://github.com/abdulhakkeempa/flask-ml-boilerplate.git`  
2. `cd flask-ml-boilerplate`
3. For Windows Users  
     `python -m venv venv`  
     `venv/Scripts/Activate`  
4.   For Linux Users  
      `python3 -m venv venv`    
      `source venv/bin/activate`  
5. `pip install -r requirements.txt`  
6. `python app.py`

## Contact
Email: abdulhakkeempa2002@gmail.com  
Linkedin: https://www.linkedin.com/in/abdul-hakkeem-pa  
Twitter: https://twitter.com/abdulhakkeempa  


## Code
```
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

if __name__ == '__main__':
       app.run()
```


