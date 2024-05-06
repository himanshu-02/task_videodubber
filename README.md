# task_videodubber

## Setup

```
cd task_2
python3 -m pip install -r requirements.txt
```

## Usage 

In parent directory execute ->
```
uvicorn task_2.main:app --reload  
```

You can also remove the ```database.db``` 

## Check on aws instance:
Check out 
```http://16.170.140.225```

and 

```http://16.170.140.225/docs```

for the api reference

## Tech stack
- python3
- fastapi
- sqlite3
- uvicorn
- sqlalchemy
- aws EC2 instance
- nginx for location context


