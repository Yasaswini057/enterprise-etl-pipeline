"""GitHub Issues API adapter that preserves the existing ticket input contract."""

import os

import requests

from config.logger import logger


GITHUB_API_URL = "https://api.github.com/repos/{repository}/issues"
GITHUB_REPOSITORY = os.getenv("GITHUB_REPOSITORY", "microsoft/vscode")
GITHUB_API_VERSION = "2022-11-28"
MAX_TICKETS = 30


def _build_ticket_record(issue, ticket_number):
    """Map a GitHub issue to the raw record shape used by the ticket transformer."""
    issue_number = issue.get("number", "unknown")
    issue_body = issue.get("body") or "No issue description provided."
    issue_state = issue.get("state", "unknown")
    created_at = issue.get("created_at", "")
    updated_at = issue.get("updated_at", "")

    return {
        # Sequential IDs preserve the existing T001 payment relationship.
        "id": ticket_number,
        "userId": ((ticket_number - 1) % 10) + 1,
        "title": issue.get("title", "Untitled GitHub issue"),
        "body": (
            f"GitHub issue #{issue_number}\n"
            f"Status: {issue_state}\n"
            f"Created: {created_at}\n"
            f"Updated: {updated_at}\n\n"
            f"{issue_body}"
        ),
        # Retain the requested issue fields for raw-data traceability.
        "subject": issue.get("title", "Untitled GitHub issue"),
        "status": issue_state,
        "created_at": created_at,
        "updated_at": updated_at,
    }


def fetch_tickets():
    """Fetch GitHub issues and return the unchanged raw ticket payload contract.

    Pull requests are excluded because GitHub's issues endpoint includes them in
    its response. A GitHub token is optional for this public repository, but it
    raises the API rate limit when supplied through ``GITHUB_TOKEN``.
    """
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": GITHUB_API_VERSION,
    }
    token = os.getenv("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"

    params = {
        "state": "all",
        "per_page": MAX_TICKETS,
        "sort": "updated",
        "direction": "desc",
    }

    try:
        response = requests.get(
            GITHUB_API_URL.format(repository=GITHUB_REPOSITORY),
            headers=headers,
            params=params,
            timeout=30,
        )
        response.raise_for_status()
        issues = response.json()

        if not isinstance(issues, list):
            raise ValueError("GitHub Issues API returned an unexpected response.")

        issues = [issue for issue in issues if "pull_request" not in issue]
        tickets = [
            _build_ticket_record(issue, index)
            for index, issue in enumerate(issues, start=1)
        ]

        if not tickets:
            raise ValueError(
                f"No issues were returned for GitHub repository {GITHUB_REPOSITORY}."
            )

        logger.info(
            "Fetched %s GitHub issues from repository %s.",
            len(tickets),
            GITHUB_REPOSITORY,
        )
        return {"posts": tickets}

    except (requests.RequestException, ValueError) as error:
        logger.exception(
            "GitHub ticket extraction failed for repository %s: %s",
            GITHUB_REPOSITORY,
            error,
        )
        raise RuntimeError(
            "Unable to fetch ticket data from the configured GitHub repository."
        ) from error
