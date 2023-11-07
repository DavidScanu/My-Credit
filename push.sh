# Connect to Heroku
#heroku login

# Heroku container login
#heroku container:login

# Create Heroku app
#heroku create streamlit-isen-g1


# Build Image MAC ARM
#docker buildx build --platform linux/amd64 -t streamlit-isen  .

# Build Image 
docker build -t streamlit-isen  .

# Tag Image to Heroku app
docker tag streamlit-isen registry.heroku.com/streamlit-isen/web

# Push Image to Heroku
docker push registry.heroku.com/streamlit-isen/web

# Release Image to Heroku
heroku container:release web -a streamlit-isen

# Open Heroku app
heroku open -a streamlit-isen

# Logs
heroku logs --tail -a streamlit-isen