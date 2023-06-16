# lusid.EntitiesApi

All URIs are relative to *https://fbn-ci.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_portfolio_changes**](EntitiesApi.md#get_portfolio_changes) | **GET** /api/entities/changes/portfolios | [EARLY ACCESS] GetPortfolioChanges: Get the next change to each portfolio in a scope.


# **get_portfolio_changes**
> ResourceListOfChange get_portfolio_changes(scope, effective_at, as_at=as_at)

[EARLY ACCESS] GetPortfolioChanges: Get the next change to each portfolio in a scope.

Gets the time of the next (earliest effective at) modification (correction and/or amendment) to each portfolio in a scope relative to a point in bitemporal time.  Includes changes from parent portfolios in different scopes.  Excludes changes from subcriptions (e.g corporate actions).

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid import ApiClientFactory
from lusid.rest import ApiException
from lusid.models.resource_list_of_change import ResourceListOfChange
from pprint import pprint

api_url = "https://fbn-ci.lusid.com/api"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.

access_token = os.getenv("ACCESS_TOKEN")


# Use the lusid ApiClientFactory to build Api instances with a configured api client
# The ApiClientFactory will use the api_url and token if passed as parameters
# Or the secrets in the secrets file at secrets_path
# Or configured environment variables 
# To configure an api_client to make calls to LUSID APIs
api_client_factory = ApiClientFactory(
    api_url=api_url, 
    token=access_token,
    secrets_path=secrets_path, 
    app_name=app_name
)
# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(lusid.EntitiesApi)
    scope = 'scope_example' # str | The scope
    effective_at = 'effective_at_example' # str | The effective date of the origin.
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The as-at date of the origin. (optional)

    try:
        # [EARLY ACCESS] GetPortfolioChanges: Get the next change to each portfolio in a scope.
        api_response = await api_instance.get_portfolio_changes(scope, effective_at, as_at=as_at)
        print("The response of EntitiesApi->get_portfolio_changes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->get_portfolio_changes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope | 
 **effective_at** | **str**| The effective date of the origin. | 
 **as_at** | **datetime**| The as-at date of the origin. | [optional] 

### Return type

[**ResourceListOfChange**](ResourceListOfChange.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | The details of the input related failure |  -  |
**200** | A list of portfolio changes in the requested scope relative to the specified time. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

