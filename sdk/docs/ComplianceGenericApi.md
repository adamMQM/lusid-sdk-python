# lusid.ComplianceGenericApi

All URIs are relative to *https://fbn-ci.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_compliance_template**](ComplianceGenericApi.md#get_compliance_template) | **GET** /api/compliance/templates/{scope}/{code} | [EARLY ACCESS] GetComplianceTemplate: Get the requested compliance template.
[**list_compliance_templates**](ComplianceGenericApi.md#list_compliance_templates) | **GET** /api/compliance/templates | [EARLY ACCESS] ListComplianceTemplates: Get a specific compliance template


# **get_compliance_template**
> ComplianceTemplate get_compliance_template(scope, code, as_at=as_at)

[EARLY ACCESS] GetComplianceTemplate: Get the requested compliance template.

Use this endpoint to fetch a specific compliance template.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid import ApiClientFactory
from lusid.rest import ApiException
from lusid.models.compliance_template import ComplianceTemplate
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
    api_instance = api_client_factory.build(lusid.ComplianceGenericApi)
    scope = 'scope_example' # str | Scope of TemplateID
    code = 'code_example' # str | Code of TemplateID
    as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The time at which to get results from. Default : latest (optional)

    try:
        # [EARLY ACCESS] GetComplianceTemplate: Get the requested compliance template.
        api_response = await api_instance.get_compliance_template(scope, code, as_at=as_at)
        print("The response of ComplianceGenericApi->get_compliance_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceGenericApi->get_compliance_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of TemplateID | 
 **code** | **str**| Code of TemplateID | 
 **as_at** | **datetime**| Optional. The time at which to get results from. Default : latest | [optional] 

### Return type

[**ComplianceTemplate**](ComplianceTemplate.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested compliance template. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_compliance_templates**
> PagedResourceListOfComplianceTemplate list_compliance_templates(as_at=as_at, page=page, start=start, limit=limit, filter=filter)

[EARLY ACCESS] ListComplianceTemplates: Get a specific compliance template

Use this endpoint to fetch a list of all available compliance template ids.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid import ApiClientFactory
from lusid.rest import ApiException
from lusid.models.paged_resource_list_of_compliance_template import PagedResourceListOfComplianceTemplate
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
    api_instance = api_client_factory.build(lusid.ComplianceGenericApi)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The time at which to get results from. Default : latest (optional)
    page = 'page_example' # str | Optional. The pagination token to use to continue listing compliance runs from a previous call to list compliance runs.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, and asAt fields              must not have changed since the original request. Also, if set, a start value cannot be provided. (optional)
    start = 56 # int | Optional. When paginating, skip this number of results. (optional)
    limit = 56 # int | Optional. When paginating, limit the number of returned results to this many. (optional)
    filter = 'filter_example' # str | Optional. Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)

    try:
        # [EARLY ACCESS] ListComplianceTemplates: Get a specific compliance template
        api_response = await api_instance.list_compliance_templates(as_at=as_at, page=page, start=start, limit=limit, filter=filter)
        print("The response of ComplianceGenericApi->list_compliance_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceGenericApi->list_compliance_templates: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| Optional. The time at which to get results from. Default : latest | [optional] 
 **page** | **str**| Optional. The pagination token to use to continue listing compliance runs from a previous call to list compliance runs.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, and asAt fields              must not have changed since the original request. Also, if set, a start value cannot be provided. | [optional] 
 **start** | **int**| Optional. When paginating, skip this number of results. | [optional] 
 **limit** | **int**| Optional. When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Optional. Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**PagedResourceListOfComplianceTemplate**](PagedResourceListOfComplianceTemplate.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of compliance templates available. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

