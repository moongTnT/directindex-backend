from pydantic import BaseModel

class ThemeInfo(BaseModel):
    etf_tkr:str
    etf_name:str
    theme_kr:str
    ytd:float
    pdf_cnt:int
    top_stk_tkr:str
    theme_class:str