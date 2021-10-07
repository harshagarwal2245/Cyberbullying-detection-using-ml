"""
to get function identified by pytest always write function name starting with 
test example test_env
function should always contain assert function if assert is true test is passed
"""

import json
import logging
import os
import joblib
import pytest
from prediction_service.prediction import form_response, api_response 
import prediction_service


input_data={
    "correct_data":
    {"Hi this is good tweet"},
    "incorrect_data":{"dang...i need to stop eatting cheese. Damn you kraft!"}
}

def test_form_response(data=input_data["correct_data"]):
    res=form_response(data)
    assert 0 <= res <= 1

def test_api_response(data=input_data["correct_data"]):
    res=api_response(data)
    assert 0 <= res["response"] <= 1

