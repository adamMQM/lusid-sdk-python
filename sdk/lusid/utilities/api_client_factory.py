from lusid.utilities.api_client_builder import ApiClientBuilder
from lusid.utilities.proxy_config import ProxyConfig
from lusid.utilities.api_configuration import ApiConfiguration


class ApiClientFactory:
    """
    The ApiClientFactory is responsible for providing the ability to create any of the LUSID APIs using the provided
    credentials. It will use the same ApiClient across all of the APIs.

    """
    def __init__(self, **kwargs):
        """
        Iniitalise an ApiClientFactory by passing the token, api_url and app_name, or by
        passing in the api_secrets_filename

        :param str token: Bearer token used to initialise the API
        :param str api_secrets_filename: Name of secrets file (including full path)
        :param str api_url: LUSID API url
        :param str app_name: Application name (optional)
        :param str certificate_filename: Name of the certificate file (.pem, .cer or .crt)
        :param str proxy_url: The url of the proxy to use including the port e.g. http://myproxy.com:8888
        :param str proxy_username: The username for the proxy to use
        :param str proxy_password: The password for the proxy to use
        :param str correlation_id: Correlation id for all calls made from the returned LUSID API instances
        :param bool tcp_keep_alive: A flag for controlling if the API client uses TCP keep-alive probes
        """

        builder_kwargs = {}

        if "token" in kwargs and str(kwargs["token"]) != "None":

            # If there is a token use it along with the specified proxy details if specified
            config = ApiConfiguration(
                api_url=kwargs.get("api_url", None),
                certificate_filename=kwargs.get("certificate_filename", None),
                proxy_config=ProxyConfig(
                    address=kwargs.get("proxy_url", None),
                    username=kwargs.get("proxy_username", None),
                    password=kwargs.get("proxy_password", None),
                ) if kwargs.get("proxy_url", None) is not None else None,
                app_name=kwargs.get("app_name", None)
            )

            builder_kwargs["api_configuration"] = config
            builder_kwargs["token"] = kwargs["token"]

        # Otherwise use a secrets file if it exists
        builder_kwargs["api_secrets_filename"] = kwargs.get("api_secrets_filename", None)

        # add the correlation id if specified
        builder_kwargs["correlation_id"] = kwargs.get("correlation_id", None)

        # add the id provider response handler if specified
        builder_kwargs["id_provider_response_handler"] = kwargs.get("id_provider_response_handler", None)

        builder_kwargs["tcp_keep_alive"] = kwargs.get("tcp_keep_alive", False)

        # Call the client builder, this will result in using either a token, secrets file or environment variables
        self.api_client = ApiClientBuilder.build(**builder_kwargs)

    def build(self, metaclass):
        """
        :param type metaclass:  type of the LUSID API to create
        :return: Initalised LUSID API for the type passed in
        """

        return metaclass(self.api_client)
    
    async def __aenter__(self):
        await self.api_client.__aenter__()
        return self

    async def __aexit__(self, exc_type, exc_value, exc_tb):
        await self.api_client.__aexit__(exc_type, exc_value, exc_tb)