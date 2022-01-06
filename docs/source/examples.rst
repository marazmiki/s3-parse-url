Examples
========

.. warning::

    Sometimes, Amazon can generate secret access keys containing special chars 
    like /. If so, you should prepare a safe version of the key by quoting these 
    chars manually (in the example you should get %25). Feel free to use this 
    handy snippet to get a safe  (i.e. quoted) secret access key.
    Example:

    .. code::

        echo "pass\/\/ord" | python -c "import sys; from urllib.parse import quote_plus; print(quote_plus(sys.stdin.read().strip()))"
        pass%5C%2F%5C%2Ford

.. code::

    import typing
    import aiobotocore
    from s3_parse_dsn import s3_parse_dsn


    async def upload_to_s3():
        dsn = s3_parse_dsn("s3://my-awesome-bucket?region=us-east-1")

        async with aiobotocore.get_session().create_client("s3", **self.bits) as s3:
            await s3.put_object(Bucket=dsn.bucket,
                                Key=key,
                                Body=data)
            return await self.presign_url(key)

        async with dsn.get_aiobotocore_client() as s3:
            await s3.put_object(Bucket=dsn.bucket,
                                Key="my-file.txt",
                                Body="")

    import asyncio

    from s3_parse_url import parse_s3_url
    from s3_parse_url.ext.clients import get_aiobotocore_client, get_boto3_client

    BUCKET = "s3-direct-upload-python"
    DSN = ("s3://AKIA****MLUD:ysJq****53nes"
           "@" + BUCKET + "?region=us-west-1")

    KEY = "weather_measurements.csv"

    s3url = parse_s3_url(DSN)


    params = {
        "Key": KEY,
        "Bucket": s3url.bucket_name,
        "ResponseContentDisposition": "inline; filename=" + KEY,
    }


    async def test_aiobotocore():
        async with get_aiobotocore_client(s3url) as cl:
            url = await cl.generate_presigned_url("get_object", Params=params)
            print("AIO:  ", url)


    def test_boto3():
        cl = get_boto3_client(s3url)
        url = cl.generate_presigned_url("get_object", Params=params)
        print("BOTO3:", url)


    asyncio.run(test_aiobotocore())
    test_boto3()
