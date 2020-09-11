import json
from assets import models


class NewAsset(object):
    def __init__(self,request,data):
        self.request = request
        self.data = data

    def add_to_new_assets_zone(self):

        defaults = {
            'data': json.dumps(self.data),
            'asset_type': self.data.get('asset_type'),
            'manufacturer': self.data.get('manufacturer'),
            'model': self.data.get('model'),
            'ram_size': int(str([a['capacity'] for a in self.data.get('ram')]).strip("[").strip("]")),
            'disk_size': int(str([b for b in [a['capacity'] for a in self.data.get('physical_disk_driver')] if b !='']).strip("[").strip("]")),
            'cpu_model': self.data.get('cpu_model'),
            'cpu_count': self.data.get('cpu_count'),
            'cpu_core_count': self.data.get('cpu_core_count'),
            'os_distribution': self.data.get('os_distribution'),
            'os_release': self.data.get('os_release'),
            'os_type': self.data.get('os_type'),

        }
        models.NewAssetApprovalZone.objects.update_or_create(sn=self.data['sn'], defaults=defaults)

        return '资产已加入/跟新待审批区'