#!/usr/bin/env python3

"""Service layer for Hunter.io operations - the bridge between the Force and the API."""

from hunter_client import HunterClient
from models import DomainSearchRequest, EmailFinderRequest, EmailVerifierRequest


def perform_domain_search(client: HunterClient, search_request: DomainSearchRequest):
    """Perform domain search - like Clark Kent investigating in Metropolis."""
    return client.domain_search(
        domain=search_request.domain,
        limit=search_request.limit,
        search_type=search_request.search_type,
    )


def perform_email_finder(client: HunterClient, finder_request: EmailFinderRequest):
    """Perform email finder - like Arya crossing names off her list."""
    return client.email_finder(
        domain=finder_request.domain,
        first_name=finder_request.first_name,
        last_name=finder_request.last_name,
    )


def perform_email_verifier(client: HunterClient, verifier_request: EmailVerifierRequest):
    """Perform email verification - like Luke trusting his feelings about the Force."""
    return client.email_verifier(email=verifier_request.email)
