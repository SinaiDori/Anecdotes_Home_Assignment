from plugin import Plugin
from authentication import connectivity_test
from evidence_collection import collect_evidence


class DummyJsonPlugin(Plugin):
    def __init__(self, name, base_url, credentials):
        super().__init__(name, base_url, credentials)
        self.login_url = self.base_url + '/' + 'auth/login'
        self.posts_url = self.base_url + '/' + 'posts'
        self.auth_url = self.base_url + '/' + 'auth/me'

    def execute(self):
        token = connectivity_test(self.login_url, self.credentials)
        collect_evidence(self.posts_url, self.auth_url, token, limit=60)
