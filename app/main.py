from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import secrets
import string
import httpx

app = FastAPI()

# base model code


class PasswordRequest(BaseModel):
    length: int
    include_symbols: bool = False
    include_numbers: bool = True
    include_lowercase: bool = True
    include_uppercase: bool = True


@app.post("/generate-password")
async def generate_password(request: PasswordRequest):
    if request.length < 6 or request.length > 128:
        raise HTTPException(
            status_code=400, detail="Password length must be between 6 and 128.")

    characters = ""
    if request.include_symbols:
        characters += string.punctuation
    if request.include_numbers:
        characters += string.digits
    if request.include_lowercase:
        characters += string.ascii_lowercase
    if request.include_uppercase:
        characters += string.ascii_uppercase

    if not characters:
        raise HTTPException(
            status_code=400, detail="At least one character type must be selected.")

    password = ''.join(secrets.choice(characters)
                       for i in range(request.length))
    return {"password": password, "length": len(password)}

# This is the new part for integrating the third-party cryptocurrency API


@app.get("/bitcoin-price")
async def bitcoin_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        result = response.json()
        price = result["bitcoin"]["usd"]
    return {"bitcoin_price": price}
