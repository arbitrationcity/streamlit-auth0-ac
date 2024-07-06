import os
import streamlit.components.v1 as components
import json
from urllib import request
from jose import jwt

# _RELEASE = False
_RELEASE = True


if not _RELEASE:
  _login_button = components.declare_component(
    "login_button",
    url="http://localhost:3000", # vite dev server port
  )
else:
  parent_dir = os.path.dirname(os.path.abspath(__file__))
  build_dir = os.path.join(parent_dir, "frontend/dist")
  _login_button = components.declare_component("login_button", path=build_dir)



def login_button(clientId, domain, audience, key=None, **kwargs):
    """
    Create a new instance of "login_button".
    When the user logs in, check if the sub returned from Auth0 matches the verified sub from the token from the same response.

    Parameters
    ----------
    clientId: str
        client_id per auth0 config on your Applications / Settings page
    
    domain: str
        domain per auth0 config on your Applications / Settings page in the form dev-xxxx.xx.auth0.com
        OR!  a custom domain, any FQDN
    audience: str
        audience of api. Default api is https://{tenant}.xx.auth0.com/api/v2
    key: str or None
        An optional key that uniquely identifies this component. If this is
        None, and the component's arguments are changed, the component will
        be re-mounted in the Streamlit frontend and lose its current state.
    Returns
    -------
    dict
        User info
    """

    user_info = _login_button(client_id=clientId, domain=domain, audience=audience, key=key, default=0)

    if not user_info:
        return False
    elif isAuth(response = user_info, domain=domain, audience=audience):
        return user_info
    else:
        print('Auth failed: invalid token')
        raise 


def isAuth(response, domain, audience):
    return getVerifiedSubFromToken(token = response['token'], domain=domain, audience=audience) == response['sub']


def getVerifiedSubFromToken(token, domain, audience):
    well_known_url = f"https://{domain}/.well-known/jwks.json"
    req = request.Request(well_known_url, headers={'User-Agent': 'Mozilla'})   #can be any user agent, but needs one included
    opened_url = request.urlopen(req)
    jwks = json.loads(opened_url.read())
    unverified_header = jwt.get_unverified_header(token)
    rsa_key = {}
    for key in jwks["keys"]:
        if key["kid"] == unverified_header["kid"]:
            rsa_key = {
                "kty": key["kty"],
                "kid": key["kid"],
                "use": key["use"],
                "n": key["n"],
                "e": key["e"]
            }
    if rsa_key:
        try:
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=["RS256"],
                audience=audience,
                issuer=f'https://{domain}/'
            )
        except jwt.ExpiredSignatureError:
            raise 
        except jwt.JWTClaimsError:
            raise 
        except Exception:
            raise 

        return payload['sub']




if not _RELEASE:
    # NOTE: if running as not _RELEASE with the dev server, create a .env file with clientId, domain, and audience values
    import streamlit as st
    from dotenv import load_dotenv
    import os
    load_dotenv()

    clientId = os.environ['clientId']
    domain = os.environ['domain']
    audience = os.environ['audience']
    st.subheader("Login component")
    # user_info = login_button(clientId, domain=domain, audience=audience)                                        #debug
    st.write('User info')
    # st.write(user_info)
    if st.button('rerun'):
        st.experimental_rerun()
