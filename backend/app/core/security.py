from fastapi import HTTPException, status


def require_api_key(api_key: str | None) -> None:
    if api_key != "demo-key":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid API key")
