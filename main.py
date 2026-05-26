from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

app = FastAPI(title="AutoAgent Sales API", version="0.1.0")

# مدل داده برای درخواست چت مشتری
class ChatMessage(BaseModel):
    user_id: str
    message: str

# مدل داده برای پاسخ سیستم
class BotResponse(BaseModel):
    reply: str
    action_required: Optional[str] = None # مثلا: "generate_invoice"

# دیتابیس فرضی محصولات برای دمو
PRODUCTS = {
    "web_design": {"name": "Professional Web Design", "price": 500},
    "ai_bot": {"name": "AI Sales Bot Integration", "price": 300},
}

@app.get("/")
async def root():
    return {"status": "Online", "message": "AutoAgent Sales System is running."}

@app.post("/chat", response_model=BotResponse)
async def handle_chat(chat: ChatMessage):
    user_text = chat.message.lower()
    
    # منطق هوش مصنوعی ساده (در آینده به Claude API متصل می‌شود)
    if "سلام" in user_text or "hello" in user_text:
        return BotResponse(reply="سلام! من منشی هوشمند شرکت هستم. چطور می‌توانم در خرید خدمات به شما کمک کنم؟")
    
    elif "قیمت" in user_text or "price" in user_text:
        return BotResponse(
            reply="خدمات ما شامل طراحی وب (۵۰۰ دلار) و پیاده‌سازی هوش مصنوعی (۳۰۰ دلار) است. کدام مورد مد نظر شماست؟"
        )
    
    elif "فاکتور" in user_text or "invoice" in user_text:
        # اینجا ایجنت تشخیص می‌دهد که باید فرآیند مالی را شروع کند
        return BotResponse(
            reply="حتماً. در حال آماده‌سازی پیش‌فاکتور برای شما هستم. لطفا نام کامل خود را بفرمایید.",
            action_required="initiate_billing"
        )
    
    else:
        # پاسخ عمومی در صورتی که نیاز به پردازش LLM داشته باشد
        return BotResponse(
            reply="پیام شما را دریافت کردم. اجازه بدهید دقیق‌تر بررسی کنم و به شما پاسخ دهم."
        )

# بخشی برای مدیریت اسناد مالی (بعداً تکمیل می‌شود)
@app.post("/billing/generate")
async def generate_invoice(user_id: str, product_id: str):
    if product_id not in PRODUCTS:
        raise HTTPException(status_code=404, detail="Product not found")
    
    product = PRODUCTS[product_id]
    # در این بخش کد تولید PDF فاکتور قرار می‌گیرد
    return {
        "message": "Invoice generated successfully",
        "invoice_details": product,
        "download_url": f"/downloads/invoice_{user_id}.pdf"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
