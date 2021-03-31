"""
    Sat4Envi backend API

    The API documentation of the backend.  Access to definition group `public` is unrestricted. To access group `provider` you need extra permissions and group `private` isn't made available publicly.  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from py4envi_openapi_client.api_client import ApiClient, Endpoint as _Endpoint
from py4envi_openapi_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from py4envi_openapi_client.model.search_response import SearchResponse


class SearchApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __get_count(
            self,
            product_type,
            **kwargs
        ):
            """Get count of total scene results  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_count(product_type, async_req=True)
            >>> result = thread.get()

            Args:
                product_type (str):

            Keyword Args:
                sensing_from (str): [optional]
                sensing_to (str): [optional]
                ingestion_from (str): [optional]
                ingestion_to (str): [optional]
                satellite_platform (str): [optional]
                processing_level (str): [optional]
                polarisation (str): [optional]
                sensor_mode (str): [optional]
                relative_orbit_number (str): [optional]
                absolute_orbit_number (str): [optional]
                collection (str): [optional]
                timeliness (str): [optional]
                instrument (str): [optional]
                footprint (str): [optional]
                product_level (str): [optional]
                cloud_cover (str): [optional]
                sort_by (str): [optional]
                order (str): [optional]
                limit (str): [optional]
                offset (str): [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                int
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['product_type'] = \
                product_type
            return self.call_with_http_info(**kwargs)

        self.get_count = _Endpoint(
            settings={
                'response_type': (int,),
                'auth': [
                    'bearer-token'
                ],
                'endpoint_path': '/api/v1/search/count',
                'operation_id': 'get_count',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'product_type',
                    'sensing_from',
                    'sensing_to',
                    'ingestion_from',
                    'ingestion_to',
                    'satellite_platform',
                    'processing_level',
                    'polarisation',
                    'sensor_mode',
                    'relative_orbit_number',
                    'absolute_orbit_number',
                    'collection',
                    'timeliness',
                    'instrument',
                    'footprint',
                    'product_level',
                    'cloud_cover',
                    'sort_by',
                    'order',
                    'limit',
                    'offset',
                ],
                'required': [
                    'product_type',
                ],
                'nullable': [
                    'sensing_from'
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'product_type':
                        (str,),
                    'sensing_from':
                        (str,),
                    'sensing_to':
                        (str,),
                    'ingestion_from':
                        (str,),
                    'ingestion_to':
                        (str,),
                    'satellite_platform':
                        (str,),
                    'processing_level':
                        (str,),
                    'polarisation':
                        (str,),
                    'sensor_mode':
                        (str,),
                    'relative_orbit_number':
                        (str,),
                    'absolute_orbit_number':
                        (str,),
                    'collection':
                        (str,),
                    'timeliness':
                        (str,),
                    'instrument':
                        (str,),
                    'footprint':
                        (str,),
                    'product_level':
                        (str,),
                    'cloud_cover':
                        (str,),
                    'sort_by':
                        (str,),
                    'order':
                        (str,),
                    'limit':
                        (str,),
                    'offset':
                        (str,),
                },
                'attribute_map': {
                    'product_type': 'productType',
                    'sensing_from': 'sensingFrom',
                    'sensing_to': 'sensingTo',
                    'ingestion_from': 'ingestionFrom',
                    'ingestion_to': 'ingestionTo',
                    'satellite_platform': 'satellitePlatform',
                    'processing_level': 'processingLevel',
                    'polarisation': 'polarisation',
                    'sensor_mode': 'sensorMode',
                    'relative_orbit_number': 'relativeOrbitNumber',
                    'absolute_orbit_number': 'absoluteOrbitNumber',
                    'collection': 'collection',
                    'timeliness': 'timeliness',
                    'instrument': 'instrument',
                    'footprint': 'footprint',
                    'product_level': 'productLevel',
                    'cloud_cover': 'cloudCover',
                    'sort_by': 'sortBy',
                    'order': 'order',
                    'limit': 'limit',
                    'offset': 'offset',
                },
                'location_map': {
                    'product_type': 'query',
                    'sensing_from': 'query',
                    'sensing_to': 'query',
                    'ingestion_from': 'query',
                    'ingestion_to': 'query',
                    'satellite_platform': 'query',
                    'processing_level': 'query',
                    'polarisation': 'query',
                    'sensor_mode': 'query',
                    'relative_orbit_number': 'query',
                    'absolute_orbit_number': 'query',
                    'collection': 'query',
                    'timeliness': 'query',
                    'instrument': 'query',
                    'footprint': 'query',
                    'product_level': 'query',
                    'cloud_cover': 'query',
                    'sort_by': 'query',
                    'order': 'query',
                    'limit': 'query',
                    'offset': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_count
        )

        def __get_scenes(
            self,
            product_type,
            **kwargs
        ):
            """Search for scenes  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_scenes(product_type, async_req=True)
            >>> result = thread.get()

            Args:
                product_type (str):

            Keyword Args:
                sensing_from (str): [optional]
                sensing_to (str): [optional]
                ingestion_from (str): [optional]
                ingestion_to (str): [optional]
                satellite_platform (str): [optional]
                processing_level (str): [optional]
                polarisation (str): [optional]
                sensor_mode (str): [optional]
                relative_orbit_number (str): [optional]
                absolute_orbit_number (str): [optional]
                collection (str): [optional]
                timeliness (str): [optional]
                instrument (str): [optional]
                footprint (str): [optional]
                product_level (str): [optional]
                cloud_cover (str): [optional]
                sort_by (str): [optional]
                order (str): [optional]
                limit (str): [optional]
                offset (str): [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                [SearchResponse]
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['product_type'] = \
                product_type
            return self.call_with_http_info(**kwargs)

        self.get_scenes = _Endpoint(
            settings={
                'response_type': ([SearchResponse],),
                'auth': [
                    'bearer-token'
                ],
                'endpoint_path': '/api/v1/search',
                'operation_id': 'get_scenes',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'product_type',
                    'sensing_from',
                    'sensing_to',
                    'ingestion_from',
                    'ingestion_to',
                    'satellite_platform',
                    'processing_level',
                    'polarisation',
                    'sensor_mode',
                    'relative_orbit_number',
                    'absolute_orbit_number',
                    'collection',
                    'timeliness',
                    'instrument',
                    'footprint',
                    'product_level',
                    'cloud_cover',
                    'sort_by',
                    'order',
                    'limit',
                    'offset',
                ],
                'required': [
                    'product_type',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'product_type':
                        (str,),
                    'sensing_from':
                        (str,),
                    'sensing_to':
                        (str,),
                    'ingestion_from':
                        (str,),
                    'ingestion_to':
                        (str,),
                    'satellite_platform':
                        (str,),
                    'processing_level':
                        (str,),
                    'polarisation':
                        (str,),
                    'sensor_mode':
                        (str,),
                    'relative_orbit_number':
                        (str,),
                    'absolute_orbit_number':
                        (str,),
                    'collection':
                        (str,),
                    'timeliness':
                        (str,),
                    'instrument':
                        (str,),
                    'footprint':
                        (str,),
                    'product_level':
                        (str,),
                    'cloud_cover':
                        (str,),
                    'sort_by':
                        (str,),
                    'order':
                        (str,),
                    'limit':
                        (str,),
                    'offset':
                        (str,),
                },
                'attribute_map': {
                    'product_type': 'productType',
                    'sensing_from': 'sensingFrom',
                    'sensing_to': 'sensingTo',
                    'ingestion_from': 'ingestionFrom',
                    'ingestion_to': 'ingestionTo',
                    'satellite_platform': 'satellitePlatform',
                    'processing_level': 'processingLevel',
                    'polarisation': 'polarisation',
                    'sensor_mode': 'sensorMode',
                    'relative_orbit_number': 'relativeOrbitNumber',
                    'absolute_orbit_number': 'absoluteOrbitNumber',
                    'collection': 'collection',
                    'timeliness': 'timeliness',
                    'instrument': 'instrument',
                    'footprint': 'footprint',
                    'product_level': 'productLevel',
                    'cloud_cover': 'cloudCover',
                    'sort_by': 'sortBy',
                    'order': 'order',
                    'limit': 'limit',
                    'offset': 'offset',
                },
                'location_map': {
                    'product_type': 'query',
                    'sensing_from': 'query',
                    'sensing_to': 'query',
                    'ingestion_from': 'query',
                    'ingestion_to': 'query',
                    'satellite_platform': 'query',
                    'processing_level': 'query',
                    'polarisation': 'query',
                    'sensor_mode': 'query',
                    'relative_orbit_number': 'query',
                    'absolute_orbit_number': 'query',
                    'collection': 'query',
                    'timeliness': 'query',
                    'instrument': 'query',
                    'footprint': 'query',
                    'product_level': 'query',
                    'cloud_cover': 'query',
                    'sort_by': 'query',
                    'order': 'query',
                    'limit': 'query',
                    'offset': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_scenes
        )
