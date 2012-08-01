class JinjaEnv(object):
    jinja_env = None
    
    @classmethod
    def set(self, env):
        self.jinja_env = env

    @classmethod
    def get(self):
        return self.jinja_env