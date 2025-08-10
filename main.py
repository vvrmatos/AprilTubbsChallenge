#!/usr/bin/env python3

from fastapi import FastAPI, HTTPException
from hunter_client import HunterClient
from models import DomainSearchRequest, EmailFinderRequest, EmailVerifierRequest
import os
from dotenv import load_dotenv
from hunter_service import perform_domain_search, perform_email_finder, perform_email_verifier

# I did not use the BIGGER application approach for this simple challenge
# But I am well aware of it and would use it in a real-world application


load_dotenv()

app = FastAPI(title="Done by Spaceman Y2K38", version="1.38.77")

api_key_name = os.getenv("HUNTER_API_KEY")

if not api_key_name:
    raise ValueError("HUNTER_API_KEY environment variable is required")

client = HunterClient(api_key_name)

HTTP_INTERNAL_ERROR = 500


@app.post("/api/domain-search")
def domain_search(search_request: DomainSearchRequest):
    try:
        return perform_domain_search(client, search_request)
    except Exception as error:
        raise HTTPException(status_code=HTTP_INTERNAL_ERROR, detail=str(error))


@app.post("/api/email-finder")
def email_finder(finder_request: EmailFinderRequest):
    try:
        return perform_email_finder(client, finder_request)
    except Exception as error:
        raise HTTPException(status_code=HTTP_INTERNAL_ERROR, detail=str(error))


@app.post("/api/email-verifier")
def email_verifier(verifier_request: EmailVerifierRequest):
    try:
        return perform_email_verifier(client, verifier_request)
    except Exception as error:
        raise HTTPException(status_code=HTTP_INTERNAL_ERROR, detail=str(error))
