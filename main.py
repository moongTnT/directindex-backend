import uvicorn
from starlette.middleware.cors import CORSMiddleware
from fastapi import FastAPI

origins=["*"] 

app = FastAPI()

dummy_theme_info = {
    0: {"etf_tkr": "BKCH", "etf_name": "GLOBAL X blockchain ETF", "theme_kr": "블록체인", "ytd": 140.78, "pdf_cnt": 30, "top_stk_tkr": "코인베이스글로벌A", "theme_class": "혁신기술"},
    1: {"etf_tkr": "BOTZ", "etf_name": "GLOBAL X robotics&artificial intelligence ETF", "theme_kr": "로보틱스&AI", "ytd": 140.78, "pdf_cnt": 30, "top_stk_tkr": "코인베이스글로벌A", "theme_class": "혁신기술"},
    2: {"etf_tkr": "AIQ", "etf_name": "GLOBAL X intelligence&technology ETF", "theme_kr": "AI&빅테크", "ytd": 140.78, "pdf_cnt": 30, "top_stk_tkr": "코인베이스글로벌A", "theme_class": "혁신기술"},
    3: {"etf_tkr": "AGNG", "etf_name": "GLOBAL X aging population ETF", "theme_kr": "인구고령화", "ytd": 140.78, "pdf_cnt": 30, "top_stk_tkr": "코인베이스글로벌A", "theme_class": "혁신기술"},
    4: {"etf_tkr": "AQWA", "etf_name": "GLOBAL X clean water ETF", "theme_kr": "청정수", "ytd": 140.78, "pdf_cnt": 30, "top_stk_tkr": "코인베이스글로벌A", "theme_class": "혁신기술"},
}

@app.get("/theme_info")
def get_theme_info():
    return dummy_theme_info

@app.get("/theme_info")
def get_pdf_info():
    return "I've got pdf_info"

if __name__=="__main__":
    uvicorn.run(app, port=8000)