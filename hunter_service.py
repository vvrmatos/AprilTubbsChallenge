#!/usr/bin/env python3

from hunter_client import HunterClient
from models import DomainSearchRequest, EmailFinderRequest, EmailVerifierRequest


def perform_domain_search(client: HunterClient, search_request: DomainSearchRequest):
    return client.domain_search(
        domain=search_request.domain,
        limit=search_request.limit,
        type=search_request.type
    )


def perform_email_finder(client: HunterClient, finder_request: EmailFinderRequest):
    return client.email_finder(
        domain=finder_request.domain,
        first_name=finder_request.first_name,
        last_name=finder_request.last_name
    )


def perform_email_verifier(client: HunterClient, verifier_request: EmailVerifierRequest):
    return client.email_verifier(email=verifier_request.email)
