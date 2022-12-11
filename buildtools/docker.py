import docker

class Image:

    def __init__(self, config_path, tag):
        self.config_path = config_path
        self.tag = tag

    def build(self):
        client = docker.from_env()

        image, build_log = client.images.build(
            path='./',
            dockerfile='./app/Dockerfile',
            buildargs={
                "FRENDCONFIG": self.config_path
            },
            tag=self.tag)

        for line in build_log:
            if 'stream' in line.keys():
                print(line['stream'], end='')

    def push(self, registry, login=None):

        client = docker.from_env()

        if type(login) == tuple:
            docker_username, docker_password = login
            loginres = client.login(username=docker_username, password=docker_password, registry=registry)

        result = client.images.push(
            repository=self.tag
        )
        print(result)