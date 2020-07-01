from sanic_openapi import doc


class DefaultResponse:
    message = doc.String(description="Response message")
    sucess = doc.Boolean(description="Boolean indicating message success")
