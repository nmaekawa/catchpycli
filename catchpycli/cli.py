"""
catchpycli.cli
--------------
command line interface for catchpy api client
"""

import os
import click
import django
from django.conf import settings
from dotenv import load_dotenv


#
# set django context
#

# if dotenv file, load it
dotenv_path = os.environ.get('CATCHPY_DOTENV_PATH', None)
click.echo('dotenv path is ({})'.format(dotenv_path))
if dotenv_path:
    load_dotenv(dotenv_path)

# define settings if not in environment
if os.environ.get("DJANGO_SETTINGS_MODULE", None) is None:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "catchpy.settings.dev")

django.setup()


#
# now we can import django app modules
#
from anno.json_models import Catcha
from consumer.catchjwt import encode_catchjwt


from catchpycli import data
from catchpycli.client import CatchpyCli
from catchpycli.endpoints.annos import Annos


@click.group()
def cli():
    pass


@cli.command()
@click.option('--base_url', required=True, help='include http/https')
@click.option('--api_key', required=True)
@click.option('--secret_key', required=True)
@click.option('--use_annotatorjs', default=False)
@click.option('--verbose', default=True)
def cleanup(
    base_url, api_key, secret_key,
    use_annotatorjs, verbose):

    cli = CatchpyCli(base_url=base_url, api_key=api_key, secret_key=secret_key)

    # search by tag
    params = {'platform': data.PLATFORM_NAME}
    resp_search = Annos.search(
        cli, params=params, requesting_user='__admin__')
    response_search_json = resp_search.json()
    assert response_search_json is not None

    if click.confirm('about to delete {} annotations'.format(
        response_search_json['size'])):
        for anno_obj in response_search_json['rows']:
            resp_delete = Annos.delete(
                    cli, anno_id=anno_obj['id'],
                    requesting_user=anno_obj['creator']['id'])
            response_delete = resp_delete.json()
            click.echo('deleted anno_id: {}'.format(response_delete['id']))
        click.echo('cleanup DONE!')
    else:
        click.echo('Aborting...')


@cli.command()
@click.option('--base_url', required=True, help='include http/https')
@click.option('--api_key', required=True)
@click.option('--secret_key', required=True)
@click.option('--use_annotatorjs', default=False)
@click.option('--verbose', default=True)
def smoke_test(
    base_url, api_key, secret_key,
    use_annotatorjs, verbose):

    cli = CatchpyCli(base_url=base_url, api_key=api_key, secret_key=secret_key)

    anno_obj = data.make_annotation_json_object()

    # create new annotation
    resp = Annos.create(
        cli, anno_obj, requesting_user=anno_obj['creator']['id'])
    response_json = resp.json()
    assert response_json is not None
    assert 'id' in response_json
    anno_obj['id'] = response_json['id']
    assert Catcha.are_similar(anno_obj, response_json)

    # update annotation: add tag
    fake_tag_name = 'fake_test_{}'.format(anno_obj['id'])
    tag = data.make_tag_object(fake_tag_name)
    anno_obj['body']['items'].append(tag)

    # update annotation with new tags
    resp = Annos.update(
        cli, anno_obj, requesting_user=anno_obj['creator']['id'])
    response_json = resp.json()
    assert response_json is not None
    assert Catcha.are_similar(anno_obj, response_json)

    # create one more annotation
    anno_obj2 = data.make_annotation_json_object()
    anno_obj2['body']['items'][0]['value'] = 'different text for annotation 2'
    resp2 = Annos.create(
        cli, anno_obj2, requesting_user=anno_obj2['creator']['id'])
    response_json2 = resp2.json()
    assert response_json2 is not None
    assert 'id' in response_json2
    anno_obj2['id'] = response_json2['id']
    assert Catcha.are_similar(anno_obj2, response_json2)

    # search by tag
    params = {'tag': fake_tag_name}
    resp_search = Annos.search(
        cli, params=params, requesting_user=anno_obj['creator']['id'])
    response_search_json = resp_search.json()
    assert response_search_json is not None

    click.echo('response_search is {}'.format(response_search_json))

    assert response_search_json['total'] == 1
    assert len(response_search_json['rows']) == 1
    assert response_search_json['rows'][0]['id'] == anno_obj['id']
    assert Catcha.are_similar(
        response_search_json['rows'][0], anno_obj)

    # delete created annotation
    resp_delete = Annos.delete(
            cli, anno_id=anno_obj['id'],
            requesting_user=anno_obj['creator']['id'])
    response_delete = resp_delete.json()
    assert response_delete is not None
    assert Catcha.are_similar(anno_obj, response_delete)

    # read remaining annotation
    resp_read = Annos.read(
            cli, anno_id=anno_obj2['id'],
            requesting_user=anno_obj2['creator']['id'])
    response_read = resp_read.json()
    assert response_read is not None
    assert Catcha.are_similar(anno_obj2, response_read)

    # delete remaining annotation
    resp_delete = Annos.delete(
            cli, anno_id=anno_obj2['id'],
            requesting_user=anno_obj2['creator']['id'])
    response_delete = resp_delete.json()
    assert response_delete is not None
    assert Catcha.are_similar(anno_obj2, response_delete)


if __name__ == "__main__":
    cli()
