import uvicorn
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from typing import List
from textract import extract_text_from_image

app = FastAPI()


@app.post("/upload/")
async def upload_files(files: List[UploadFile] = File(...)):
    file_names = {}
    for file in files:
        contents = await file.read()
        file_name = file.filename
        with open(file_name, "wb") as f:
            f.write(contents)
        result = extract_text_from_image(file_name)
        file_names[file_name] = result
    return JSONResponse(content={"result": file_names})


if __name__ == "__main__":
    uvicorn.run(app=app, host='0.0.0.0', port=8001)
