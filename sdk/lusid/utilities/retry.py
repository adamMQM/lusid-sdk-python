import functools
from asyncio import sleep

from lusid import ApiException
from lusid.api_client import ApiClient


def retry(fn, retries=3):
    @functools.wraps(fn)
    async def __retry(*args, **kwargs):
        if not isinstance(retries, int):
            raise ValueError(f"retries should be an int, found {type(retries)}")
        # remove the retries param from the kwargs
        kwargs.pop("retries", None)

        tries = 0
        while tries < retries + 1:
            try:
                return await fn(*args, **kwargs)
            except ApiException as ex:
                tries += 1
                retry_after = ex.headers.get("Retry-After")

                # have done max number of retries
                if tries == retries:
                    raise

                # try after delay
                elif retry_after is not None:
                    if not isinstance(retry_after, float):
                        try:
                            retry_after = float(retry_after)
                        except ValueError:
                            raise ValueError(
                                f"invalid Retry-After header value: {retry_after}"
                            )

                    sleep(retry_after)

                # no retry header
                else:
                    raise

    return __retry


class RetryingClient(ApiClient):
    def __init__(
        self,
        configuration=None,
        header_name=None,
        header_value=None,
        cookie=None,
        pool_threads=1,
        retries=3,
    ):
        super().__init__(configuration, header_name, header_value, cookie, pool_threads)
        self.default_retries = retries

    async def call_api(
        self,
        resource_path,
        method,
        path_params=None,
        query_params=None,
        header_params=None,
        body=None,
        post_params=None,
        files=None,
        response_types_map=None,
        auth_settings=None,
        async_req=None,
        _return_http_data_only=None,
        collection_formats=None,
        _preload_content=True,
        _request_timeout=None,
        _host=None,
        _request_auth=None,
        retries=3,
    ):
        call_api_fn = retry(super().call_api, retries=retries or self.default_retries)

        return await call_api_fn(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body,
            post_params=post_params,
            files=files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=async_req,
            _return_http_data_only=_return_http_data_only,
            collection_formats=collection_formats,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            _host=_host,
            _request_auth=_request_auth,
        )
