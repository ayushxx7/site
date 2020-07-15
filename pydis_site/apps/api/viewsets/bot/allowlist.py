from rest_framework.viewsets import ModelViewSet

from pydis_site.apps.api.models.bot.allowlist import AllowList
from pydis_site.apps.api.serializers import AllowListSerializer


class AllowListViewSet(ModelViewSet):
    """
    View providing CRUD operations on items whitelisted or blacklisted by our bot.

    ## Routes
    ### GET /bot/allowlists
    Returns all allowlist items in the database.

    #### Response format
    >>> [
    ...     {
    ...         'id': "2309268224",
    ...         'created_at': "01-01-2020 ...",
    ...         'updated_at': "01-01-2020 ...",
    ...         'type': "file_format",
    ...         'allowed': 'true',
    ...         'content': ".jpeg",
    ...     },
    ...     ...
    ... ]

    #### Status codes
    - 200: returned on success

    ### POST /bot/allowedlists
    Adds a single allowedlist item to the database.

    #### Request body
    >>> {
    ...         'type': str,
    ...         'allowed': bool,
    ...         'content': str,
    ... }

    #### Status codes
    - 201: returned on success
    - 400: if one of the given fields is invalid

    ### DELETE /bot/allowedlists/<title:str>
    Deletes the tag with the given `title`.

    #### Status codes
    - 204: returned on success
    - 404: if a tag with the given `title` does not exist
    """

    serializer_class = AllowListSerializer
    queryset = AllowList.objects.all()