from pulpcore.plugin import PulpPluginAppConfig


class PulpCertGuardPluginAppConfig(PulpPluginAppConfig):
    """App config for cert guard plugin."""

    name = 'pulp_certguard.app'
    label = 'certguard'
    version = '1.3.1.dev'
