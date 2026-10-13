from fasthtml.common import Table, Thead, Tbody, Tr, Th, Td, P
from .base_component import BaseComponent


class DataTable(BaseComponent):
    """HTML table built from a pandas DataFrame."""

    def component_data(self, entity_id, model):
        return model.event_counts(entity_id)

    def build_component(self, entity_id, model):
        df = self.component_data(entity_id, model)
        if df is None or df.empty:
            return P("No event data available.", cls="no-data")
        header = Tr(*[Th(col.replace("_", " ").title()) for col in df.columns])
        rows   = [Tr(*[Td(str(v)) for v in row]) for row in df.itertuples(index=False)]
        return Table(Thead(header), Tbody(*rows), cls="data-table")
