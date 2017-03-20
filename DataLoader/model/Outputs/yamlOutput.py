
from DataLoader.model.Abstract import iOutputs
from odm2api.ODM2.models import *
# import pyyaml
import yaml
from yodaloader.YAML.yamlFunctions import YamlFunctions


class yamlOutput(iOutputs):

    def save(self, session, file_path):
        tables = self.parseObjects()
        data = []
        for t in tables:
            for o in session.query(t).all():
                data.append(o)

        yaml.dump_all(data, open(file_path, 'w'))


    def accept(self):
        raise NotImplementedError()

