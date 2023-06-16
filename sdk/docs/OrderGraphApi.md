# lusid.OrderGraphApi

All URIs are relative to *https://fbn-ci.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_order_graph_blocks**](OrderGraphApi.md#list_order_graph_blocks) | **GET** /api/ordergraph/blocks | [EXPERIMENTAL] ListOrderGraphBlocks: Lists blocks that pass the filter provided, and builds a summary picture of the state of their associated order entities.
[**list_order_graph_placements**](OrderGraphApi.md#list_order_graph_placements) | **GET** /api/ordergraph/placements | [EXPERIMENTAL] ListOrderGraphPlacements: Lists placements that pass the filter provided, and builds a summary picture of the state of their associated order entities.


# **list_order_graph_blocks**
> PagedResourceListOfOrderGraphBlock list_order_graph_blocks(as_at=as_at, pagination_token=pagination_token, sort_by=sort_by, limit=limit, filter=filter, property_keys=property_keys)

[EXPERIMENTAL] ListOrderGraphBlocks: Lists blocks that pass the filter provided, and builds a summary picture of the state of their associated order entities.

Lists all blocks of orders, subject to the filter, along with the IDs of orders, placements, allocations and  executions in the block, the total quantities of each, and a simple text field describing the overall state.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid import ApiClientFactory
from lusid.rest import ApiException
from lusid.models.paged_resource_list_of_order_graph_block import PagedResourceListOfOrderGraphBlock
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
    api_instance = api_client_factory.build(lusid.OrderGraphApi)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | See https://support.lusid.com/knowledgebase/article/KA-01832/ (optional)
    pagination_token = 'pagination_token_example' # str | See https://support.lusid.com/knowledgebase/article/KA-01915/ (optional)
    sort_by = ['sort_by_example'] # List[str] | Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName. (optional)
    limit = 56 # int | See https://support.lusid.com/knowledgebase/article/KA-01915/ (optional)
    filter = '' # str | See https://support.lusid.com/knowledgebase/article/KA-01914/ (optional) (default to '')
    property_keys = ['property_keys_example'] # List[str] | Must be block-level properties. See https://support.lusid.com/knowledgebase/article/KA-01855/ (optional)

    try:
        # [EXPERIMENTAL] ListOrderGraphBlocks: Lists blocks that pass the filter provided, and builds a summary picture of the state of their associated order entities.
        api_response = await api_instance.list_order_graph_blocks(as_at=as_at, pagination_token=pagination_token, sort_by=sort_by, limit=limit, filter=filter, property_keys=property_keys)
        print("The response of OrderGraphApi->list_order_graph_blocks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderGraphApi->list_order_graph_blocks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| See https://support.lusid.com/knowledgebase/article/KA-01832/ | [optional] 
 **pagination_token** | **str**| See https://support.lusid.com/knowledgebase/article/KA-01915/ | [optional] 
 **sort_by** | [**List[str]**](str.md)| Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName. | [optional] 
 **limit** | **int**| See https://support.lusid.com/knowledgebase/article/KA-01915/ | [optional] 
 **filter** | **str**| See https://support.lusid.com/knowledgebase/article/KA-01914/ | [optional] [default to &#39;&#39;]
 **property_keys** | [**List[str]**](str.md)| Must be block-level properties. See https://support.lusid.com/knowledgebase/article/KA-01855/ | [optional] 

### Return type

[**PagedResourceListOfOrderGraphBlock**](PagedResourceListOfOrderGraphBlock.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Blocks in scope. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_order_graph_placements**
> PagedResourceListOfOrderGraphPlacement list_order_graph_placements(as_at=as_at, pagination_token=pagination_token, sort_by=sort_by, limit=limit, filter=filter, property_keys=property_keys)

[EXPERIMENTAL] ListOrderGraphPlacements: Lists placements that pass the filter provided, and builds a summary picture of the state of their associated order entities.

Lists all order placements, subject to the filter, along with the IDs of the block and order that the  placement is for, each placement's quantity, the IDs of all allocations and executions in the placement  and the total quantities of those, and a simple text field describing the overall state of the placement.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import lusid
from lusid import ApiClientFactory
from lusid.rest import ApiException
from lusid.models.paged_resource_list_of_order_graph_placement import PagedResourceListOfOrderGraphPlacement
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
    api_instance = api_client_factory.build(lusid.OrderGraphApi)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | See https://support.lusid.com/knowledgebase/article/KA-01832/ (optional)
    pagination_token = 'pagination_token_example' # str | See https://support.lusid.com/knowledgebase/article/KA-01915/ (optional)
    sort_by = ['sort_by_example'] # List[str] | Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName. (optional)
    limit = 56 # int | See https://support.lusid.com/knowledgebase/article/KA-01915/ (optional)
    filter = '' # str | See https://support.lusid.com/knowledgebase/article/KA-01914/ (optional) (default to '')
    property_keys = ['property_keys_example'] # List[str] | Must be placement properties. See https://support.lusid.com/knowledgebase/article/KA-01855/ (optional)

    try:
        # [EXPERIMENTAL] ListOrderGraphPlacements: Lists placements that pass the filter provided, and builds a summary picture of the state of their associated order entities.
        api_response = await api_instance.list_order_graph_placements(as_at=as_at, pagination_token=pagination_token, sort_by=sort_by, limit=limit, filter=filter, property_keys=property_keys)
        print("The response of OrderGraphApi->list_order_graph_placements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderGraphApi->list_order_graph_placements: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| See https://support.lusid.com/knowledgebase/article/KA-01832/ | [optional] 
 **pagination_token** | **str**| See https://support.lusid.com/knowledgebase/article/KA-01915/ | [optional] 
 **sort_by** | [**List[str]**](str.md)| Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName. | [optional] 
 **limit** | **int**| See https://support.lusid.com/knowledgebase/article/KA-01915/ | [optional] 
 **filter** | **str**| See https://support.lusid.com/knowledgebase/article/KA-01914/ | [optional] [default to &#39;&#39;]
 **property_keys** | [**List[str]**](str.md)| Must be placement properties. See https://support.lusid.com/knowledgebase/article/KA-01855/ | [optional] 

### Return type

[**PagedResourceListOfOrderGraphPlacement**](PagedResourceListOfOrderGraphPlacement.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Placements in scope. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

