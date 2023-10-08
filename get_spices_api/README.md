#Create db
#create schema

#Env setup
pythom -m venv gs_env
gs_env/script/activate

pip install -r requirements.txt

#RUN APP
uvicorn app.main:app --reload  --host 0.0.0.0 --port 8000 --env-file .env