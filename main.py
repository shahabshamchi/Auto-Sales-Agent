from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat_with_customer(request: ChatRequest):
    # اینجا در آینده به Claude یا Llama متصل می‌شود
    user_message = request.message
    
    # منطق فرضی برای تشخیص نیاز به فاکتور
    if "invoice" in user_message.lower():
        response = "Sure! I am preparing your invoice. Please provide your billing details."
    else:
        response = f"Hello! How can I assist you with our products today?"
        
    return {"reply": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
