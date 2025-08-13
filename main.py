#!/usr/bin/env python3

"""FastAPI application for Hunter.io API - because even web services need the Force."""

import os

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException

from hunter_client import HunterClient
from hunter_service import perform_domain_search, perform_email_finder, perform_email_verifier
from models import DomainSearchRequest, EmailFinderRequest, EmailVerifierRequest

# I did not use the BIGGER application approach for this simple challenge
# But I am well aware of it and would use it in a real-world application


load_dotenv()

app = FastAPI(title='Done by Spaceman Y2K38', version='1.38.77')

api_key_name = os.getenv('HUNTER_API_KEY')

if not api_key_name:
    raise ValueError('HUNTER_API_KEY environment variable is required')

client = HunterClient(api_key_name)

HTTP_INTERNAL_ERROR = 500


@app.post('/api/domain-search')
def domain_search(search_request: DomainSearchRequest):
    """Search for emails in a domain - like the Jedi Council searching for answers."""
    try:
        return perform_domain_search(client, search_request)
    except Exception as error:
        raise HTTPException(status_code=HTTP_INTERNAL_ERROR, detail=str(error))


@app.post('/api/email-finder')
def email_finder(finder_request: EmailFinderRequest):
    """Find email for a person - like Bran seeing through the eyes of ravens."""
    try:
        return perform_email_finder(client, finder_request)
    except Exception as error:
        raise HTTPException(status_code=HTTP_INTERNAL_ERROR, detail=str(error))


@app.post('/api/email-verifier')
def email_verifier(verifier_request: EmailVerifierRequest):
    """Verify an email address - like Jon Snow knowing nothing, but learning."""
    try:
        return perform_email_verifier(client, verifier_request)
    except Exception as error:
        raise HTTPException(status_code=HTTP_INTERNAL_ERROR, detail=str(error))
