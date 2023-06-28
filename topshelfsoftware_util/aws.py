"""Facilitates interaction with AWS using boto3 clients."""

from boto3.session import Session as Boto3Session
from botocore.client import BaseClient
from botocore.exceptions import ClientError as BotoClientError

from topshelfsoftware_util.common import fmt_json
from topshelfsoftware_util.log import get_logger
logger = get_logger(__name__)


def create_boto3_client(service_name: str, region: str = None) -> BaseClient:
    """Create a low-level service client by name.

    Parameters
    ----------
    service_name: str
        Name of the AWS service.
    
    region: str, optional
        Region where service abides.
        Default is `None`.
    """
    logger.debug(f"creating boto3 client: {service_name}")
    try:
        session = Boto3Session(region_name=region)
        client = session.client(service_name=service_name)
    except BotoClientError as e:
        logger.error(f"failed to create client: {service_name}. Reason: {e}")
        raise e
    logger.debug("boto3 client successfully created")
    return client


def get_ssm_value(name: str, region: str = None) -> str:
    """Retrieve the value of an SSM parameter.

    Parameters
    ----------
    name: str
        Name of the SSM parameter.
    
    region: str, optional
        Region where service abides.
        Default is `None`.
    """
    logger.debug(f"getting ssm: {name}")
    try:
        ssm_client = create_boto3_client(service_name="ssm", region=region)
        ssm_resp = ssm_client.get_parameter(Name=name)
        logger.debug(f"resp: {fmt_json(ssm_resp)}")
        val = ssm_resp["Parameter"]["Value"]
    except BotoClientError as e:
        logger.error(f"failed to retrieve ssm parameter: {name}. Reason: {e}")
        raise e
    except KeyError as e:
        logger.error(f"failed to retrieve parameter value from ssm response: {name}. Reason: {e}")
        raise e
    logger.debug(f"ssm parameter value: {val}")
    return val
    


def get_secret_value(secret_id: str, region: str = None) -> str:
    """Retrieve the value of a managed secret.

    Parameters
    ----------
    secret_id: str
        The ARN or name of the secret to retrieve.
    
    region: str, optional
        Region where service abides.
        Default is `None`.
    """
    logger.debug(f"getting secret: {secret_id}")
    try:
        secret_client = create_boto3_client(service_name="secretsmanager", region=region)
        secret_resp = secret_client.get_secret_value(SecretId=secret_id)
        logger.debug(f"resp: {fmt_json(secret_resp)}")
        val = secret_resp["SecretString"]
    except BotoClientError as e:
        logger.error(f"failed to retrieve secret: {secret_id}. Reason: {e}")
        raise e
    except KeyError as e:
        logger.error(f"failed to retrieve string from secretsmanager response: {secret_id}. Reason: {e}")
        raise e
    logger.debug("secret string: <redacted>")
    return val
