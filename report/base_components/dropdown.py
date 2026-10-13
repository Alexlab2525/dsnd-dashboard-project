from fasthtml.common import Select, Option
from .base_component import BaseComponent


class Dropdown(BaseComponent):
    """<select> element populated from model.names()."""

    def component_data(self, entity_id, model):
        return model.names()

    def build_component(self, entity_id, model):
        options_data = self.component_data(entity_id, model)
        options = [
            Option(name, value=str(oid), selected=(str(oid) == str(entity_id)))
            for oid, name in options_data
        ]
        return Select(*options, name="id", id="entity-dropdown")
