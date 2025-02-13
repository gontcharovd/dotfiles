import subprocess
from libqtile.widget import base


class VPNWidget(base.ThreadPoolText):
    """A custom widget to display VPN status using nmcli."""

    defaults = [
        ('update_interval', 5, 'Update interval in seconds.'),
    ]

    def __init__(self, **config):
        # Initialize the base class with the provided config
        base.ThreadPoolText.__init__(self, '', **config)
        # Add default values to the config
        self.add_defaults(VPNWidget.defaults)

    def poll(self):
        """Poll the VPN status."""
        try:
            result = subprocess.run(
                ['nmcli', '-t', '-f', 'TYPE,STATE', 'con', 'show', '--active'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            connections = result.stdout.split('\n')
            for conn in connections:
                if conn == 'vpn:activated':
                    return 'VPN Active'
            return 'VPN<span foreground="red"> Inactive</span>'
        except Exception as e:
            return f'VPN: Error ({e})'
