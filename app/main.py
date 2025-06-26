from datetime import datetime
from fastapi import FastAPI, Response, HTTPException
import os

from fastapi.responses import HTMLResponse

app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)

DAY_IMAGE_MAP = {
    0: "sunday.webp",
    1: "monday.jpg",
    2: "tuesday.webp",
    3: "wednesday.jpg",
    5: "friday.webp",
    6: "saturday.jpg"
}

STATIC_FOLDER = "app/static"  

@app.get("/")
def root():
    weekday = int(datetime.today().strftime('%w'))
    
    image_filename = DAY_IMAGE_MAP.get(weekday)

    if image_filename is None:
        return HTMLResponse(content=f"""
       <!DOCTYPE html>
<html>
  <head>
    <title>Tuesday API</title>
  </head>
  <body style="margin:0; padding:0; display:flex; justify-content:center; align-items:center; height:100vh; background-color:#111;">
    <h1 style="
      font-size:120px;
      font-weight:bold;
      font-family:sans-serif;
      background: repeating-linear-gradient(
        45deg,
        #ff6b6b,
        #ff6b6b 20px,
        #feca57 20px,
        #feca57 40px,
        #48dbfb 40px,
        #48dbfb 60px
      );
      -webkit-background-clip: text;
      color: transparent;
      text-align: center;
      ">
      Nope. Come back another Tuesday.
    </h1>
  </body>
</html>

        """, status_code=200)


    image_path = os.path.join(STATIC_FOLDER, image_filename)
    
    try:
        if image_filename.endswith(".jpg") or image_filename.endswith(".jpeg"):
            media_type = "image/jpeg"
        elif image_filename.endswith(".webp"):
            media_type = "image/webp"
        else:
            media_type = "application/octet-stream"  

        with open(image_path, "rb") as file:
            image_data = file.read()
        
        return Response(content=image_data, media_type=media_type)

   
    except:
        return HTMLResponse(content=f"""
       <!DOCTYPE html>
<html>
  <head>
    <title>Tuesday API</title>
  </head>
  <body style="margin:0; padding:0; display:flex; justify-content:center; align-items:center; height:100vh; background-color:#111;">
    <h1 style="
      font-size:120px;
      font-weight:bold;
      font-family:sans-serif;
      background: repeating-linear-gradient(
        45deg,
        #ff6b6b,
        #ff6b6b 20px,
        #feca57 20px,
        #feca57 40px,
        #48dbfb 40px,
        #48dbfb 60px
      );
      -webkit-background-clip: text;
      color: transparent;
      text-align: center;
      ">
      Nope. Come back another Time.
    </h1>
  </body>
</html>

        """, status_code=200)

        
