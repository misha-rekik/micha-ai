# Command to run the backend

## after running poetry shell

uvicorn main:app --reload

## without poetry shell

poetry run uvicorn main:app --reload
