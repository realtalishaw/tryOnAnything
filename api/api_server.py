from fastapi import FastAPI, Header, HTTPException
import redis
from modules.image_handler import ImageHandler
from modules.pre_processing import HumanPreProcessing, GarmentPreProcessing
from modules.garment_warping import GarmentWarping
from modules.try_on_module import TryOnModule
from modules.post_processing import PostProcessing
from utils.logger import Logger

# Initialize Redis client
r = redis.Redis(host='localhost', port=6379, db=0)

app = FastAPI()
logger = Logger()

async def validate_api_key(x_api_key: str):
    stored_key = r.get("test_api_key")
    if stored_key is None:
        raise HTTPException(status_code=401, detail="API Key not configured in Redis")

    if x_api_key != stored_key.decode('utf-8'):
        raise HTTPException(status_code=401, detail="Invalid API Key")

async def process_request(user_token, garment_image, human_model):
    """
    Encapsulates the various processing steps.
    """
    try:
        # Initialize classes
        #image_handler = ImageHandler()
        #human_pre_processing = HumanPreProcessing()
        #garment_pre_processing = GarmentPreProcessing()
        #garment_warping = GarmentWarping()
        #try_on_module = TryOnModule()
        #post_processing = PostProcessing()

        # Image Handling
        #processed_garment_image, processed_human_image = image_handler.handle_images(garment_image, human_model)

        # Pre-Processing - parallel
        #human_data = human_pre_processing.process(processed_human_image)
        #garment_data = garment_pre_processing.process(processed_garment_image)

        # Garment Warping
        #warped_garment = garment_warping.warp_garment(human_data, garment_data)

        # Try-On
        #final_coarse_image = try_on_module.perform_try_on(warped_garment, human_data, garment_data)

        # Post-Processing
        #final_image = post_processing.upscale_and_enhance(final_coarse_image)
        #final_image_with_watermark = post_processing.add_watermark(final_image, 'path/to/watermark.png')

        # Upload final image to S3 and get URI
        #final_image_uri = image_handler.upload_to_s3(final_image_with_watermark, user_token)

        #return {"final_image_uri": final_image_uri}
        return {"message": "This is a placeholder message since methods are not implemented yet."}

    except Exception as e:
        logger.log_error(f"Error processing request: {e}")  
        return {"error": "An error occurred while processing your request."}


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
    
    # handle request
    return await process_request(user_token, garment_image, human_model)
