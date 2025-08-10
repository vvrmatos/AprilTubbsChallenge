#!/usr/bin/env python3

from pydantic import BaseModel, Field
from typing import Optional


class DomainSearchRequest(BaseModel):
    domain: str = Field(..., example="microsoft.com", description="Domain to search for emails")
    limit: Optional[int] = Field(None, example=5, description="Maximum number of results")
    type: Optional[str] = Field(None, example="personal", description="Type of email (personal, generic, or all)")


class EmailFinderRequest(BaseModel):
    domain: str = Field(..., example="microsoft.com", description="Domain to search in")
    first_name: str = Field(..., example="Satya", description="First name of the person")
    last_name: str = Field(..., example="Nadella", description="Last name of the person")


class EmailVerifierRequest(BaseModel):
    email: str = Field(..., example="test@example.com", description="Email address to verify")
