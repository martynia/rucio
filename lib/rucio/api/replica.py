# Copyright European Organization for Nuclear Research (CERN)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# You may not use this file except in compliance with the License.
# You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
#
# Authors:
# - Vincent Garonne, <vincent.garonne@cern.ch>, 2012-2013
# - Mario Lassnig, <mario.lassnig@cern.ch>, 2012

from rucio.api import permission
from rucio.core import replica
from rucio.common import exception


def list_replicas(dids, schemes=None):
    """
    List file replicas for a list of data identifiers.

    :param filters: dictionary of attributes by which the resulting
                    collection of replicas should be filtered
    """
    return replica.list_replicas(dids=dids, schemes=schemes)


def add_replicas(rse, files, issuer):
    """
    Bulk add file replicas.

    :param rse: The RSE name.
    :param files: The list of files.
    :param issuer: The issuer account.
    :param account: The account owner. If None, then issuer is selected.

    :returns: True is successful, False otherwise
    """
    kwargs = {'rse': rse}
    if not permission.has_permission(issuer=issuer, action='add_replicas', kwargs=kwargs):
        raise exception.AccessDenied('Account %s can not add file replicas on %s' % (issuer, rse))
    replica.add_replicas(rse=rse, files=files, account=issuer)


def delete_replicas(rse, files, issuer):
    """
    Bulk delete file replicas.

    :param rse: The RSE name.
    :param files: The list of files.
    :param issuer: The issuer account.
    :param account: The account owner. If None, then issuer is selected.

    :returns: True is successful, False otherwise
    """
    kwargs = {'rse': rse}
    if not permission.has_permission(issuer=issuer, action='delete_replicas', kwargs=kwargs):
        raise exception.AccessDenied('Account %s can not delete file replicas on %s' % (issuer, rse))
    replica.delete_replicas(rse=rse, files=files)
