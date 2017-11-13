"""
catchpycli.endpoints.annos
--------------------------
http calls to annotations api (annos)


client is a catchpycli.CatchpyCli object
all methods return a requests.Response or raise a requests.HTTPError
"""


class Annos(object):

    @classmethod
    def create(cls, client, anno_obj, requesting_user='user', compat=False):
        anno_id = ''
        if 'id' in anno_obj and anno_obj['id']:
            anno_id = anno_obj['id']

        token = client.make_authorization_token(requesting_user)
        path = 'annos/create' if compat else 'annos'
        r = client.post(
            path='/'.join([path, anno_id]),
            data=anno_obj,
            extra_headers={'Authorization': 'token {}'.format(token)})
        return r


    @classmethod
    def update(cls, client, anno_obj, requesting_user='user', compat=False):
        if 'id' not in anno_obj or not anno_obj['id']:
            raise Exception  # must have an id

        token = client.make_authorization_token(requesting_user)
        path = 'annos/update' if compat else 'annos'
        r = client.put(
            path='/'.join([path, anno_obj['id']]),
            data=anno_obj,
            extra_headers={'Authorization': 'token {}'.format(token)})
        return r


    @classmethod
    def read(cls, client, anno_id, requesting_user='user', compat=False):
        token = client.make_authorization_token(requesting_user)
        path = 'annos/read' if compat else 'annos'
        r = client.get(
            path='/'.join([path, anno_id]),
            extra_headers={'Authorization': 'token {}'.format(token)})
        return r


    @classmethod
    def delete(cls, client, anno_id, requesting_user='user', compat=False):
        token = client.make_authorization_token(requesting_user)
        path = 'annos/delete' if compat else 'annos'
        r = client.delete(
            path='/'.join([path, anno_id]),
            extra_headers={'Authorization': 'token {}'.format(token)})
        return r


    @classmethod
    def search(cls, client, params, requesting_user='user', compat=False):
        token = client.make_authorization_token(requesting_user)
        path = 'annos/search' if compat else 'annos'
        r = client.get(
            path=path,
            params=params,
            extra_headers={'Authorization': 'token {}'.format(token)})
        return r


