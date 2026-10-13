from fasthtml.common import Div, Label, Input
from .base_component import BaseComponent


class Radio(BaseComponent):
    """Radio buttons for switching between Employee / Team view."""

    def build_component(self, entity_id, model):
        t = model.name
        return Div(
            Label(Input(type="radio", name="entity_type", value="employee",
                        checked=(t == "employee"), onchange="this.form.submit()"), " Employee"),
            Label(Input(type="radio", name="entity_type", value="team",
                        checked=(t == "team"),     onchange="this.form.submit()"), " Team"),
            cls="radio-group",
        )
