from fastapi import FastAPI, Header, HTTPException
import redis

# Initialize Redis client
r = redis.Redis(host='localhost', port=6379, db=0)

app = FastAPI()

async def validate_api_key(x_api_key: str):
    stored_key = r.get("test_api_key")
    if stored_key is None:
        raise HTTPException(status_code=401, detail="API Key not configured in Redis")

    if x_api_key != stored_key.decode('utf-8'):
        raise HTTPException(status_code=401, detail="Invalid API Key")



@app.post("/try-on/", summary="Virtual Try-On", description="Entry endpoint to Try On Anything model")
async def try_on(
        user_token: str,
        garment_image: str,
        human_model: str,
        x_api_key: str = Header(...)
    ):
    """
    Perform a virtual try-on by taking in a `user_token`, URIs of the garment and human images, and an API key.
    
    - **user_token**: Unique identifier for the user
    - **garment_image**: URI for the garment image
    - **human_model**: URI for the human model image
    - **x_api_key**: Security API key
    
    # Returns
    - Dict containing the received data for validation.
    """
    await validate_api_key(x_api_key)
    
    # Your code to handle the API request goes here
    return {"user_token": user_token, "garment_image": garment_image, "human_model": human_model, "x_api_key": x_api_key}
