# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:51:19 2020

@author: win10
"""
from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class Score(BaseModel):
    sentence: str 
    # skewness: float 
    # curtosis: float 
    # entropy: float