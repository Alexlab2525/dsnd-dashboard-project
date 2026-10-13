from fasthtml.common import Form
from .combined_component import CombinedComponent


class FormGroup(CombinedComponent):
    """Wraps child components inside an HTML <form>."""

    action: str = "/"
    method: str = "get"

    def __call__(self, entity_id, model):
        children = self.call_children(entity_id, model)
        return Form(*children, action=self.action, method=self.method)
