# Welcome to Auth0-Streamlit

**The fastest way to provide comprehensive login inside Streamlit**

![Example of Streamlit-Auth0|635x380](demo.gif?raw=true)

## DEV Installation
1. If custom_components doesn't already exist, `mkdir custom_components && cd custom_components`
 
3. `git clone git@github.com:arbitrationcity/streamlit-auth0-ac.git`

4. Build: `cd streamlit-auth0-ac/auth0_component/frontend/  &&  npm install  &&  npm run build  &&  cd  ../../../../`

4. Use pip (or conda, etc) to install locally
`pip install custom_components/streamlit-auth0-ac`

5. Now you can rebuild and reinstall if any changes are made, or you can delete custom_components/


## PRODUCTION Installation
1. Copy or clone the production branch into the local directory custom_components/ as streamlit-auth0-ac/

2. Use pip (or conda, etc) to install locally
`pip install custom_components/streamlit-auth0-ac`


## Setup

- Register for Auth0
- Create a Single Page Application and navigate to the "settings" tab 
- set your callback url's to `http://localhost:8501/component/auth0_component.login_button/index.html` assuming you're running on localhost or `http://YOUR_DOMAIN/component/auth0_component.login_button/index.html` if you're deploying
- Copy `client_id` from this page, `domain` is your custom domain registered with Auth0. `audience` is the audience id of the auth0 API (the default is `https://{tenant}.eu.auth0.com`).
- Follow example below

## An example
On Auth0 website start a "Single Page Web Application" and copy your client-id / domain / audience into code below.

```
from auth0_component import login_button
import streamlit as st

clientId = "...."
domain = "...."
audience = "...."

user_info = login_button(clientId, domain = domain, audience = audience)       
st.write(user_info)
```

`user_info` will now contain your user's information 


## Todo

- Pass all info through JWT, at the moment the `sub` field is the only field assing through verification
- Test with other providers, only Google tested 



## Deploy

- `Change version in setup.py`
- `cd auth0_component/frontend/  && npm run build && cd .. && cd .. && rm -rf dist/* && python setup.py sdist bdist_wheel`
- `twine upload dist/*`