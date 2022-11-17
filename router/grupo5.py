from typing import Optional, List
import re
from unittest import result
from fastapi import FastAPI, File, Form, UploadFile, Request, Header
from fastapi import APIRouter, Response, Form
from fastapi.responses import HTMLResponse
from pandas import DataFrame
from pyparsing import And         #Permite dividir las rutas de la app
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_401_UNAUTHORIZED
#from werkzeug.security import generate_password_hash, check_password_hash
#import panel as pn
from datetime import date
from fastapi.templating import Jinja2Templates

grupo5=FastAPI()

templates = Jinja2Templates(directory="templates")

@grupo5.get("/grupo5/", response_class=HTMLResponse)
async def root(request:Request, hx_request:Optional[str] = Header(None), option: str='' ):

    context = {'request':request }
    if hx_request:
        if option =='semana1':
            return templates.TemplateResponse("semana1.html",context)
        if option =='semana2':
            return templates.TemplateResponse("semana2.html",context)
        if option =='semana3':
            return templates.TemplateResponse("semana3.html",context)            
        if option =='semana4':
            return templates.TemplateResponse("semana4.html",context)            
        #else:
            #return templates.TemplateResponse("grupo5.html",context)
        if option =='item1-sem1':
            return templates.TemplateResponse("item1-semana1-introduccion.html", context)
        if option =='item2-sem1':
            return templates.TemplateResponse("item2-semana1-inmobiliaria.html", context)    
        if option =='item3-sem1':
            return templates.TemplateResponse("item3-semana1-objetivos.html", context)            
        if option =='item4-sem1':
            return templates.TemplateResponse("item4-semana1-alcances.html", context)
        if option =='item5-sem1':
            return templates.TemplateResponse("item5-semana1-repositorio.html", context)
        if option =='item6-sem1':
            return templates.TemplateResponse("item6-semana1-stack-tecno.html", context)    
    return templates.TemplateResponse("grupo5.html", context)