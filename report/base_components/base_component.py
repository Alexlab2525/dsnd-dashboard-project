class BaseComponent:
    """Abstract base for all dashboard HTML components."""

    def build_component(self, entity_id, model):
        raise NotImplementedError(
            f"{self.__class__.__name__} must implement build_component()"
        )

    def component_data(self, entity_id, model):
        raise NotImplementedError(
            f"{self.__class__.__name__} must implement component_data() if it uses data."
        )

    def __call__(self, entity_id, model):
        return self.build_component(entity_id, model)
