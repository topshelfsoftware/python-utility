"""Facilitates interaction with AWS using boto3 clients."""

from boto3.session import Session as Boto3Session
from botocore.client import BaseClient

from trp_custom_util.common import fmt_json
from trp_custom_util.log import get_logger
logger = get_logger(__name__)


def create_boto3_client(service_name: str,
                        region: str = "us-west-1") -> BaseClient:
    """Create a low-level service client by name.

    Parameters
    ----------
    service_name: str
        Name of the AWS service.
        
    region: str, optional
        Region where service abides.
        Default is `us-west-1`.
    """
    try:
        logger.debug(f"creating boto3 client: {service_name}")
        session = Boto3Session()
        return session.client(
            service_name=service_name,
            region_name=region
        )
    except Exception as e:
        logger.error(f"failed to create client: {service_name}. Reason: {e}")
        raise e


def get_ssm_value(client: BaseClient, name: str) -> str:
    """Retrieve the value of an SSM parameter.

    Parameters
    ----------
    client: botocore.client.BaseClient
        SSM client.
    
    name: str
        Name of the SSM parameter.
    """
    try:
        logger.debug(f"getting ssm: {name}")

        ssm_resp = client.get_parameter(Name=name)
        logger.debug(f"resp: {fmt_json(ssm_resp)}")

        val = ssm_resp['Parameter']['Value']
        logger.debug(f"return: {val}")
        return val
    except Exception as e:
        logger.error(f"failed to get secret: {name}. Reason: {e}")
        raise e


def get_secret_value(client: BaseClient, secret_id: str) -> str:
    """Retrieve the value of a managed secret.

    Parameters
    ----------
    client: botocore.client.BaseClient
        SecretsManager client.
    
    secret_id: str
        The ARN or name of the secret to retrieve.
    """
    try:
        logger.debug(f"getting secret: {secret_id}")

        secret_resp = client.get_secret_value(SecretId=secret_id)
        logger.debug(f"resp: {fmt_json(secret_resp)}")

        val = secret_resp["SecretString"]
        logger.debug("return: <redacted>")
        return val
    except Exception as e:
        logger.error(f"failed to get secret: {secret_id}. Reason: {e}")
        raise e
