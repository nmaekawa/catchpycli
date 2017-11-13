# json objects for client testing


from random import randint

from anno.anno_defaults import CATCH_JSONLD_CONTEXT_IRI
from anno.tests.conftest import get_past_datetime


PLATFORM_NAME = 'fake_test_platform'
CONTEXT_ID = 'context_id_for_{}'.format(PLATFORM_NAME)
COLLECTION_ID = 'collection_id_for_{}'.format(CONTEXT_ID)
DEFAULT_USER = 'fake_user_id'

def make_annotation_json_object():
    created_at = get_past_datetime(5)  # created 5h ago
    anno_obj = {
        '@context': CATCH_JSONLD_CONTEXT_IRI,
        'type': 'Annotation',
        'schema_version': 'catch v1.0',
        'permissions': {
            'can_read': [],
            'can_update': [DEFAULT_USER],
            'can_delete': [DEFAULT_USER],
            'can_admin': [DEFAULT_USER],
        },
        'created': created_at,
        'modified': created_at,
        'creator': {
            'id': DEFAULT_USER,
            'name': 'name_of_{}'.format(DEFAULT_USER),
        },
        'platform': {
            'platform_name': 'fake_test_platform',
            'context_id': 'fake_test_context',
            'collection_id': 'fake_test_collection',
            'target_source_id': 'internal_reference_444',
        },
        'body': {
            'type': 'List',
            'items': [{
                'type': 'TextualBody',
                'purpose': 'commenting',
                'format': 'text/html',
                'value': 'text of annotation body',
            }],
        },
        'target': {
            'type': 'List',
            'items': [{
                'type': 'Text',
                'source': 'http://fake_target_url.com',
                'selector': {
                    'type': 'Choice',
                    'items': [{
                        'type': 'RangeSelector',
                        'startSelector': {
                            'type': 'XPathSelector', 'value': 'xxx'},
                        'endSelector': {
                            'type': 'XPathSelector', 'value': 'yyy'},
                        'refinedBy': [{
                            'type': 'TextPositionSelector',
                            'start': randint(10, 300),
                            'end': randint(350, 750),
                        }]
                    }, {
                        'type': 'TextQuoteSelector',
                        'exact': 'exact_text_for_quote_selector',
                    }],
                },
            }],
        }
    }
    return anno_obj


def make_tag_object(tagname):
    return {'type': 'TextualBody',
            'purpose': 'tagging',
            'format': 'text/html',
            'value': tagname }



