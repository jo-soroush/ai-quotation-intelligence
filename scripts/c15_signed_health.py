"""Future approved live /health smoke via standard AWS credentials and SigV4.

Do not run during local C15 implementation. This contacts the real HTTPS API.
"""

import argparse
import json
import re
from urllib.request import HTTPRedirectHandler, Request, build_opener

import boto3
from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest


class _NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, request, fp, code, message, headers, newurl):
        raise RuntimeError("health smoke redirect refused")


def check_health(api_id: str, region: str) -> tuple[int, dict[str, str]]:
    if not re.fullmatch(r"[a-z0-9]{10}", api_id):
        raise ValueError("invalid API Gateway identifier")
    if not re.fullmatch(r"[a-z]{2}-[a-z]+-\d", region):
        raise ValueError("invalid AWS region")
    url = f"https://{api_id}.execute-api.{region}.amazonaws.com/health"
    credentials = boto3.Session(region_name=region).get_credentials()
    if credentials is None:
        raise RuntimeError("standard AWS credentials unavailable")
    request = AWSRequest(method="GET", url=url)
    SigV4Auth(credentials.get_frozen_credentials(), "execute-api", region).add_auth(request)
    signed = request.prepare()
    with build_opener(_NoRedirect).open(
        Request(url, headers=dict(signed.headers.items()), method="GET"), timeout=10,
    ) as response:
        status = response.status
        body = json.loads(response.read())
    if status != 200 or body != {"status": "ok"}:
        raise RuntimeError("deployed health response differs from C13 contract")
    return status, body


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--api-id", required=True)
    parser.add_argument("--region", required=True)
    args = parser.parse_args()
    status, body = check_health(args.api_id, args.region)
    print(json.dumps({"status": status, "body": body}, sort_keys=True))


if __name__ == "__main__":
    main()
