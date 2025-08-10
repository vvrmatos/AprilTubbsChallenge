#!/usr/bin/env python3

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
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self.base_url = "https://api.hunter.io/v2"

    def domain_search(
        self,
        domain: str,
        limit: Optional[int] = None,
        type: Optional[str] = None,
    ) -> DomainSearchResult:
        request_params = {"domain": domain, "api_key": self.api_key}

        if limit is not None:
            request_params["limit"] = str(limit)
        if type is not None:
            request_params["type"] = type

        response = requests.get(
            f"{self.base_url}/domain-search",
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
        request_params = {
            "domain": domain,
            "first_name": first_name,
            "last_name": last_name,
            "api_key": self.api_key,
        }

        response = requests.get(
            f"{self.base_url}/email-finder",
            params=request_params,
            timeout=REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()

    def email_verifier(
        self,
        email: str,
    ) -> EmailVerifierResult:
        request_params = {"email": email, "api_key": self.api_key}

        response = requests.get(
            f"{self.base_url}/email-verifier",
            params=request_params,
            timeout=REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()
