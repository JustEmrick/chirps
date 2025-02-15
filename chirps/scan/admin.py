"""Registration point of the admin interface for the scan app."""
from django.contrib import admin

from .models import Finding, Result, Scan, ScanAsset, ScanAssetFailure

admin.site.register(Scan)
admin.site.register(Result)
admin.site.register(Finding)
admin.site.register(ScanAsset)
admin.site.register(ScanAssetFailure)
