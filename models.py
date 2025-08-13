#!/usr/bin/env python3

"""Pydantic models for the Hunter.io API - because even data needs structure, like the Death Star."""

from typing import Optional

from pydantic import BaseModel, Field


class DomainSearchRequest(BaseModel):
    """Request model for domain search - like searching for Red Kryptonite in Smallville."""

    domain: str = Field(..., example='microsoft.com', description='Domain to search for emails')
    limit: Optional[int] = Field(None, example=5, description='Maximum number of results')
    search_type: Optional[str] = Field(
        None,
        example='personal',
        description='Type of email (personal, generic, or all)',
    )


class EmailFinderRequest(BaseModel):
    """Request model for email finder - like Arya's list of names to find."""

    domain: str = Field(..., example='microsoft.com', description='Domain to search in')
    first_name: str = Field(..., example='Satya', description='First name of the person')
    last_name: str = Field(..., example='Nadella', description='Last name of the person')


class EmailVerifierRequest(BaseModel):
    """Request model for email verification - like Obi-Wan checking if it's a trap."""

    email: str = Field(..., example='test@example.com', description='Email address to verify')
