from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from config import HASH_TYPES
from typing import Dict, Any
import uvicorn
import re


class HashDetector:
    def __init__(self) -> None:
        self.hash_types = HASH_TYPES

    def detect(self, hash_str) -> Dict[str, Any]:
        if not hash_str:
            return {'type': 'UNKNOWN', 'desc': 'Unknown hash', 'length': 0, 'hashcat': 'UNKNOWN'}
        
        hash_str = hash_str.strip().lower()
        length = len(hash_str)
        
        for name, props in self.hash_types.items():
            if length == props['length'] and re.match(props['pattern'], hash_str):
                return {'type': name, 'desc': props['desc'], 'length': length, 'hashcat': props['hashcat']}
        
        return {'type': 'UNKNOWN', 'desc': 'Unknown hash', 'length': length, 'hashcat': 'UNKNOWN'}


app = FastAPI(title="Hash Analyzer API", version="1.0")
detector = HashDetector()

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get('/', tags=['- HTML'])
def main():
    return FileResponse('static/index.html')


@app.get("/api/detect/{hash_str}", tags=['- GET'])
def detect_hash_path(hash_str: str) -> Dict[str, Any]:
    try:
        return detector.detect(hash_str)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis error: {str(e)}")


@app.get("/api/detect", tags=['- GET'])
def detect_hash_query(hash_str: str) -> Dict[str, Any]:
    try:
        return detector.detect(hash_str)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis error: {str(e)}")


@app.get("/health", tags=['- GET'])
def health_check() -> Dict:
    return {"status": "ok", "message": "Hash Analyzer API is running"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)