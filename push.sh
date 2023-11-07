# Connect to Heroku
#heroku login

# Heroku container login
heroku container:login

# Create Heroku app
#heroku create streamlit-isen-g4

# Build Image MAC ARM
#docker buildx build --platform linux/amd64 -t streamlit-isen-g4 .

# Build Image 
docker build -t streamlit-isen-g4 .

# Tag Image to Heroku app
docker tag streamlit-isen-g4 registry.heroku.com/streamlit-isen-g4/web

# Push Image to Heroku
docker push registry.heroku.com/streamlit-isen-g4/web

# Release Image to Heroku
heroku container:release web -a streamlit-isen-g4

# Open Heroku app
heroku open -a streamlit-isen-g4

# Logs
heroku logs --tail -a streamlit-isen-g4