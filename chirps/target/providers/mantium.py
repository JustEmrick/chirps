"""Logic for interfacing with the Mantium asset."""
from logging import getLogger

from asset.models import BaseTarget
from django.db import models
from fernet_fields import EncryptedCharField
from mantium_client.api_client import MantiumClient
from mantium_spec.api.applications_api import ApplicationsApi

logger = getLogger(__name__)


class MantiumTarget(BaseTarget):
    """Implementation of a Mantium asset."""

    app_id = models.CharField(max_length=256)
    client_id = models.CharField(max_length=256)
    client_secret = EncryptedCharField(max_length=256)
    top_k = models.IntegerField(default=100)

    # Name of the file in the ./asset/static/ directory to use as a logo
    html_logo = 'asset/mantiumai-logo.jpg'
    html_name = 'Mantium'
    html_description = 'Mantium Knowledge Vault'

    def search(self, query: str, max_results: int) -> list[str]:
        """Search the vector database"""
        logger.debug('Starting Mantium Target search', extra={'id': self.id})
        client = MantiumClient(client_id=self.client_id, client_secret=self.client_secret)
        apps_api = ApplicationsApi(client)

        query_request = {'query': query}
        results = apps_api.query_application(self.app_id, query_request)

        documents = [doc['content'] for doc in results['documents']]
        logger.debug('Mantium asset search complete', extra={'id': self.id})
        return documents
