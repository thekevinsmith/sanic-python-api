from sanic_jwt import Configuration


class TestJWT(Configuration):
    super(Configuration)
    access_token_name: str = "access_token"
    algorithm: str = "HS256"
    auth_mode: bool = True
    authorization_header: str = "authorization"
    authorization_header_prefix: str = "Bearer"
    authorization_header_refresh_prefix: str = "Refresh"
    claim_aud = None
    claim_iat: bool = False
    claim_iss = None
    claim_nbf: bool = False
    claim_nbf_delta: int = 0
    cookie_domain: str = ""
    cookie_httponly: bool = True
    cookie_refresh_token_name: str = "refresh_token"
    cookie_set: bool = False
    cookie_strict: bool = True
    cookie_access_token_name: str = "access_token"
    debug: bool = False
    expiration_delta: int = 60 * 5 * 6
    leeway: int = 60 * 3
    refresh_token_enabled: bool = False
    refresh_token_name: str = "refresh_token"
    private_key = None
    scopes_enabled: bool = False
    scopes_name: str = "scopes"
    secret: str = "This is a big secret. Shhhhh"
    strict_slashes: bool = False
    user_id: str = "user_id"
    verify_exp: bool = True
    defaults: dict = dict()
