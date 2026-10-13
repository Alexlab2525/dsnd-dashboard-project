from fasthtml.common import Div


class CombinedComponent:
    """Engine that builds a list of BaseComponents inside a <div>."""

    children: list = []

    def call_children(self, entity_id, model) -> list:
        built = []
        for child in self.children:
            try:
                from fasthtml.common import FT
                if isinstance(child, FT):
                    built.append(child)
                    continue
            except ImportError:
                pass
            built.append(child(entity_id, model))
        return built

    def outer_div(self, children: list, div_args: dict = None):
        if div_args is None:
            div_args = {}
        return Div(*children, **div_args)

    def __call__(self, entity_id, model):
        children = self.call_children(entity_id, model)
        return self.outer_div(children)
