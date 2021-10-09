import pytest

from s3_parse_url import parse_s3_url
from s3_parse_url.ext import clients
from s3_parse_url.ext.clients import (get_aiobotocore_client, get_boto3_client,
                                      get_boto_client_kwargs,
                                      import_module_if_installed)


@pytest.mark.parametrize(
    argnames="module_name, expected_result",
    argvalues=[
        ("pytest", pytest),
        ("module_that_does_not_exist", None)
    ]
)
def test_import_module_if_installed(module_name, expected_result):
    assert import_module_if_installed(module_name) == expected_result


@pytest.mark.parametrize(
    argnames="library_installed",
    argvalues=[True, False],
    ids=["installed", "not installed"]
)
@pytest.mark.parametrize(
    argnames="method",
    argvalues=[get_aiobotocore_client, get_boto3_client],
    ids=["aio-boto3", "boto3"]
)
def test_get_client_instance(monkeypatch, library_installed, method):
    s3_url = "s3://xxx:yyy@my-bucket?region=us-west-1"
    if library_installed:
        assert method(s3_url)
    else:
        monkeypatch.setattr(clients, "aiobotocore", None)
        monkeypatch.setattr(clients, "boto3", None)
        with pytest.raises(ValueError):
            method(s3_url)


def test_boto_client_kwargs():
    s3_url = "s3://xxx:yyy@my-bucket?region=us-west-1"
    assert get_boto_client_kwargs(s3_url) == {
        "aws_access_key_id": "xxx",
        "aws_secret_access_key": "yyy",
        "endpoint_url": None,
        "region_name": "us-west-1",
    }


def test_boto_client_kwargs_datasource_input():
    parsed = parse_s3_url("s3://xxx:yyy@my-bucket?region=us-west-1")
    assert get_boto_client_kwargs(parsed) == {
        "aws_access_key_id": "xxx",
        "aws_secret_access_key": "yyy",
        "endpoint_url": None,
        "region_name": "us-west-1",
    }
