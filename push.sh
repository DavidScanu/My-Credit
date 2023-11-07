# Connect to Heroku
#heroku login

# Heroku container login
#heroku container:login

# Create Heroku app
#heroku create streamlit-isen-g4

# Build Image MAC ARM
# docker buildx build --platform linux/amd64 -t streamlit-isen  .

# Build Image 
# docker build -t davidscanu/my-credit-fast-api:v1.0 .

# Tag Image to Heroku app
docker tag davidscanu/my-credit-fast-api:v1.0 registry.heroku.com/api-isen-g4/web

# Push Image to Heroku
docker push registry.heroku.com/api-isen-g4/web

# Release Image to Heroku
heroku container:release web -a api-isen-g4

# Open Heroku app
heroku open -a api-isen-g4

# Logs
heroku logs --tail -a api-isen-g4