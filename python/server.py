from fastapi import FastAPI, HTTPException, Response
from datetime import datetime
from pydantic import BaseModel
from starlette.responses import StreamingResponse


import uvicorn

app = FastAPI()

class FileStat(BaseModel):
    create_datetime: str
    size: int
    mimetype: str
    name: str


@app.get("/file/{uuid}/stat/")
def stat(uuid: str):
    # Here you would implement logic to retrieve file metadata
    # For demonstration purposes, let's just return dummy data
    return FileStat(
        create_datetime=datetime.now().isoformat(),
        size=1024,
        mimetype="text/plain",
        name="example.txt"
    )

@app.get("/file/{uuid}/read/")
def read(uuid: str):
    # Here you would implement logic to retrieve file content
    # For demonstration purposes, let's just return dummy data
    content = b"Example file content"
    if content:
        headers = {
            "Content-Disposition": f"attachment; filename=example.txt",
            "Content-Type": "text/plain"
        }
        return StreamingResponse(iter([content]), headers=headers)
    else:
        raise HTTPException(status_code=404, detail="File not found")

if __name__ == "__main__":
    uvicorn.run(app="server:app", port=8000, reload=True, workers=1)