#!/usr/bin/env python3

"""Hunter.io API client - because even Superman needs to find emails in Metropolis."""

from typing import Dict, List, Optional, Union

import requests

REQUEST_TIMEOUT = 30

EmailData = Dict[str, Union[str, int]]
EmailList = List[EmailData]
DomainSearchResult = Dict[str, Union[str, int, EmailList]]
EmailFinderResult = Dict[str, Union[str, int, EmailData]]
EmailVerifierData = Dict[str, Union[str, int, bool]]
EmailVerifierResult = Dict[str, Union[str, int, EmailVerifierData]]


class HunterClient:
    """The Force is strong with this one - your gateway to Hunter.io API."""

    def __init__(self, api_key: str) -> None:
        """Initialize the Hunter client - like Luke learning to use the Force.

        Args:
            api_key: Your Hunter.io API key (the key to the Death Star plans).
        """
        self.api_key = api_key
        self.base_url = 'https://api.hunter.io/v2'

    def domain_search(
        self,
        domain: str,
        limit: Optional[int] = None,
        search_type: Optional[str] = None,
    ) -> DomainSearchResult:
        """Search for emails in a domain - like Clark Kent investigating in Smallville.

        Args:
            domain: Domain to search for emails (the town to investigate).
            limit: Maximum number of results (how many leads to follow).
            search_type: Type of search to perform (investigation method).

        Returns:
            Domain search results - the truth is out there, and so are the emails!
        """
        request_params = {'domain': domain, 'api_key': self.api_key}

        if limit is not None:
            request_params['limit'] = str(limit)
        if search_type is not None:
            request_params['type'] = search_type

        response = requests.get(
            '{0}/domain-search'.format(self.base_url),
            params=request_params,
            timeout=REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()

    def email_finder(
        self,
        domain: str,
        first_name: str,
        last_name: str,
    ) -> EmailFinderResult:
        """Find email address for a person - like Arya's list, but for emails.

        Args:
            domain: Domain to search in (the realm to explore).
            first_name: Person's first name (the character's identity).
            last_name: Person's last name (the family name).

        Returns:
            Email finder results - winter is coming, but emails are found!
        """
        request_params = {
            'domain': domain,
            'first_name': first_name,
            'last_name': last_name,
            'api_key': self.api_key,
        }

        response = requests.get(
            '{0}/email-finder'.format(self.base_url),
            params=request_params,
            timeout=REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()

    def email_verifier(
        self,
        email: str,
    ) -> EmailVerifierResult:
        """Verify if an email address is valid - like Obi-Wan checking if it's a trap.

        Args:
            email: Email address to verify (the suspicious message to investigate).

        Returns:
            Email verification results - may the validation be with you!
        """
        request_params = {'email': email, 'api_key': self.api_key}

        response = requests.get(
            '{0}/email-verifier'.format(self.base_url),
            params=request_params,
            timeout=REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()
